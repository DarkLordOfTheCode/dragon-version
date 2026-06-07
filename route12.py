from route_runner import run_route


def route12(player):
    result = run_route(player, "Route 12", "Slateport City")
    if result == "lose":
        return "lose"
    return "done"
