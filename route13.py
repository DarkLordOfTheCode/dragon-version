from route_runner import run_route

def route13(player):
    result = run_route(player, "Route 13", "Route 14")
    if result == "lose":
        return "lose"
    from route14 import route14
    return route14(player)
