from route_runner import run_route


def route23(player):
    result = run_route(player, "Route 23", "Route 24")
    if result == "lose":
        return "lose"
    from route24 import route24
    return route24(player)
