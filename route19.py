from route_runner import run_route

def route19(player):
    result = run_route(player, "Route 19", "Route 20")
    if result == "lose":
        return "lose"
    from route20 import route20
    return route20(player)
