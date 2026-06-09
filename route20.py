from route_runner import run_route

def route20(player):
    result = run_route(player, "Route 20", "Route 21")
    if result == "lose":
        return "lose"
    from route21 import route21
    return route21(player)
