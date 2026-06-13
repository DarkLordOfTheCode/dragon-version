from route_runner import run_route


def route24(player):
    result = run_route(player, "Route 24", "Route 25")
    if result == "lose":
        return "lose"
    from route25 import route25
    return route25(player)
