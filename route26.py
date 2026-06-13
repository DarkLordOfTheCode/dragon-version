from route_runner import run_route


def route26(player):
    result = run_route(player, "Route 26", "Route 27")
    if result == "lose":
        return "lose"
    from route27 import route27
    return route27(player)
