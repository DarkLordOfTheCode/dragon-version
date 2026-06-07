from route_runner import run_route

def route15(player):
    result = run_route(player, "Route 15", "Jubilife City")
    if result == "lose":
        return "lose"
    from jubilife_city import jubilife_city
    return jubilife_city(player)
