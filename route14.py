from route_runner import run_route

def route14(player):
    result = run_route(player, "Route 14", "Route 15")
    if result == "lose":
        return "lose"
    from route15 import route15
    return route15(player)
