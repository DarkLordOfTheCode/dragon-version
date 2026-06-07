from route_runner import run_route


def route10(player):
    result = run_route(player, "Route 10", "Route 11")
    if result == "lose":
        return "lose"
    from route11 import route11
    return route11(player)
