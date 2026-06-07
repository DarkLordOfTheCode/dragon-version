from route_runner import run_route


def route3(player):
    result = run_route(player, "Route 3", "Route 4")
    if result == "lose":
        return "lose"
    from route4 import route4
    return route4(player)
