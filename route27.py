from route_runner import run_route


def route27(player):
    result = run_route(player, "Route 27", "Lumiose City")
    if result == "lose":
        return "lose"
    from lumiose_city import lumiose_city
    return lumiose_city(player)
