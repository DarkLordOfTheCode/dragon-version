from route_runner import run_route


def route4(player):
    result = run_route(player, "Route 4", "Route 5")
    if result == "lose":
        return "lose"
    from route5 import route5
    return route5(player)
