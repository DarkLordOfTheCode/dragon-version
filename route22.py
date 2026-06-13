from route_runner import run_route


def route22(player):
    result = run_route(player, "Route 22", "Route 23")
    if result == "lose":
        return "lose"
    from route23 import route23
    return route23(player)
