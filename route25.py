from route_runner import run_route


def route25(player):
    result = run_route(player, "Route 25", "Route 26")
    if result == "lose":
        return "lose"
    from route26 import route26
    return route26(player)
