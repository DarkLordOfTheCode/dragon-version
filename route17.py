from route_runner import run_route

def route17(player):
    result = run_route(player, "Route 17", "Route 18")
    if result == "lose":
        return "lose"
    from route18 import route18
    return route18(player)
