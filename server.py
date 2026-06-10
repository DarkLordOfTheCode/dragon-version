#!/usr/bin/env python3
"""
Web bridge for Pokémon Dragon Version.

Runs the real terminal game (main.py) inside a pseudo-terminal and streams
its output to the browser, while sending the browser's keystrokes back in.
This means the ENTIRE existing game is playable in HTML with no changes to
the game code itself.

Uses only the Python standard library. POSIX (Linux/macOS) only.

    python3 server.py            # then open http://localhost:8000
    python3 server.py 9000       # use a different port
"""
import os
import sys
import pty
import select
import struct
import fcntl
import termios
import threading
import base64
import queue
import subprocess
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs

GAME_DIR = os.path.dirname(os.path.abspath(__file__))
HOST = "0.0.0.0"
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
COLS, ROWS = 80, 40          # the game only needs ~40 cols; give it room
MAX_BUFFER = 200_000         # keep the last ~200KB so reloads show recent state


class Session:
    """One running instance of the game, wired to a pseudo-terminal."""

    def __init__(self):
        self.master_fd = None
        self.proc = None
        self.buffer = bytearray()
        self.clients = []           # one queue.Queue per connected browser tab
        self.lock = threading.Lock()

    def start(self, mode="new"):
        """Stop any running game, then launch a fresh one."""
        self.stop()

        master, slave = pty.openpty()
        # tell the terminal how big it is
        fcntl.ioctl(slave, termios.TIOCSWINSZ, struct.pack("HHHH", ROWS, COLS, 0, 0))

        env = dict(
            os.environ,
            PYTHONIOENCODING="utf-8",
            PYTHONUNBUFFERED="1",
            TERM="xterm",
            LANG="C.UTF-8",
        )
        args = ["python3", "-u", "main.py"]
        if mode == "debug":
            args.append("--debug")

        self.proc = subprocess.Popen(
            args,
            stdin=slave,
            stdout=slave,
            stderr=slave,
            cwd=GAME_DIR,
            env=env,
            start_new_session=True,
            close_fds=True,
        )
        os.close(slave)                 # the child holds the only copy now
        self.master_fd = master

        with self.lock:
            self.buffer = bytearray()

        threading.Thread(target=self._reader, daemon=True).start()

    def _reader(self):
        """Pump game output into the shared buffer and every connected tab."""
        fd = self.master_fd
        try:
            while True:
                r, _, _ = select.select([fd], [], [], 0.2)
                if fd not in r:
                    continue
                try:
                    data = os.read(fd, 4096)
                except OSError:
                    break
                if not data:
                    break
                self._broadcast(data)
        finally:
            self._broadcast(
                b"\r\n\r\n*** The adventure has ended. "
                b"Press NEW GAME to play again. ***\r\n"
            )

    def _broadcast(self, data):
        with self.lock:
            self.buffer += data
            if len(self.buffer) > MAX_BUFFER:
                del self.buffer[: len(self.buffer) - MAX_BUFFER]
            for q in list(self.clients):
                try:
                    q.put_nowait(bytes(data))
                except queue.Full:
                    pass

    def write(self, text):
        """Send keystrokes from the browser into the game."""
        if self.master_fd is not None:
            try:
                os.write(self.master_fd, text.encode("utf-8"))
            except OSError:
                pass

    def stop(self):
        if self.proc and self.proc.poll() is None:
            try:
                self.proc.terminate()
            except Exception:
                pass
        if self.master_fd is not None:
            try:
                os.close(self.master_fd)
            except OSError:
                pass
        self.master_fd = None

    def subscribe(self):
        q = queue.Queue(maxsize=1000)
        with self.lock:
            self.clients.append(q)
            backlog = bytes(self.buffer)
        return q, backlog

    def unsubscribe(self, q):
        with self.lock:
            if q in self.clients:
                self.clients.remove(q)


session = Session()


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def log_message(self, *args):
        pass  # keep the console quiet

    # ---- helpers ----
    def _send_file(self, name, ctype):
        path = os.path.join(GAME_DIR, name)
        try:
            with open(path, "rb") as f:
                body = f.read()
        except OSError:
            self.send_error(404)
            return
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _no_content(self):
        self.send_response(204)
        self.send_header("Content-Length", "0")
        self.end_headers()

    # ---- routes ----
    def do_GET(self):
        path = urlparse(self.path).path
        if path == "/":
            self._send_file("play.html", "text/html; charset=utf-8")
        elif path == "/title":
            self._send_file("index.html", "text/html; charset=utf-8")
        elif path == "/stream":
            self._stream()
        else:
            self.send_error(404)

    def do_POST(self):
        path = urlparse(self.path).path
        if path == "/input":
            length = int(self.headers.get("Content-Length", 0))
            data = self.rfile.read(length).decode("utf-8", "replace")
            session.write(data)
            self._no_content()
        elif path == "/restart":
            qs = parse_qs(urlparse(self.path).query)
            mode = qs.get("mode", ["new"])[0]
            session.start(mode)
            self._no_content()
        else:
            self.send_error(404)

    def _stream(self):
        """Server-Sent Events: game output, base64-encoded per chunk."""
        q, backlog = session.subscribe()
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.send_header("Cache-Control", "no-cache")
        self.send_header("Connection", "keep-alive")
        self.end_headers()
        try:
            self._sse(backlog)
            while True:
                try:
                    chunk = q.get(timeout=15)
                except queue.Empty:
                    self.wfile.write(b": ping\n\n")   # keep-alive comment
                    self.wfile.flush()
                    continue
                self._sse(chunk)
        except (BrokenPipeError, ConnectionResetError, OSError):
            pass
        finally:
            session.unsubscribe(q)

    def _sse(self, data):
        if not data:
            return
        payload = base64.b64encode(data)
        self.wfile.write(b"data: " + payload + b"\n\n")
        self.wfile.flush()


def main():
    session.start("new")
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    server.daemon_threads = True
    print(f"Pokémon Dragon Version — web bridge running")
    print(f"  Local:   http://localhost:{PORT}")
    print(f"  Network: http://<this-machine-ip>:{PORT}")
    print("Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down...")
    finally:
        session.stop()
        server.server_close()


if __name__ == "__main__":
    main()
