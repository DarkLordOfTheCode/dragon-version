from route_runner import run_route


def route6(player):
    result = run_route(player, "Route 6", "Route 7")
    if result == "lose":
        return "lose"
    from route7 import route7
    return route7(player)
