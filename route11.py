from route_runner import run_route


def route11(player):
    result = run_route(player, "Route 11", "Route 12")
    if result == "lose":
        return "lose"
    from route12 import route12
    return route12(player)
