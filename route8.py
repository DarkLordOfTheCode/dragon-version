from route_runner import run_route


def route8(player):
    result = run_route(player, "Route 8", "Route 9")
    if result == "lose":
        return "lose"
    from route9 import route9
    return route9(player)
