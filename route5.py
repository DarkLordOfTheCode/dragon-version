from route_runner import run_route


def route5(player):
    result = run_route(player, "Route 5", "Route 6")
    if result == "lose":
        return "lose"
    from route6 import route6
    return route6(player)
