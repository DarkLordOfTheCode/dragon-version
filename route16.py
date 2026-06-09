from route_runner import run_route

def route16(player):
    result = run_route(player, "Route 16", "Route 17")
    if result == "lose":
        return "lose"
    from route17 import route17
    return route17(player)
