from route_runner import run_route


def route7(player):
    result = run_route(player, "Route 7", "Goldenrod City")
    if result == "lose":
        return "lose"
    from goldenrod_city import goldenrod_city
    return goldenrod_city(player)
