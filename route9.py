from route_runner import run_route


def route9(player):
    result = run_route(player, "Route 9", "Route 10")
    if result == "lose":
        return "lose"
    from route10 import route10
    return route10(player)
