from route_runner import run_route


def route2(player):
    result = run_route(player, "Route 2", "Route 3")
    if result == "lose":
        return "lose"
    from route3 import route3
    return route3(player)
