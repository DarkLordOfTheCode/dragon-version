from route_runner import run_route

def route18(player):
    result = run_route(player, "Route 18", "Route 19")
    if result == "lose":
        return "lose"
    from route19 import route19
    return route19(player)
