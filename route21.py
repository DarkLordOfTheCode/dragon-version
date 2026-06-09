import random
from battle import battle
from pokemon import create_pokemon
from routes import routes
from route_runner import tall_grass


def pause():
    input("(Press Enter to continue...)")
    print()


def route21(player):
    route = routes["Route 21"]

    print("=" * 40)
    print("  ROUTE 21")
    print("=" * 40)
    print()
    print(route["description"])
    print()
    pause()

    trainers = route["trainers"]
    wild_pokemon = route["wild_pokemon"]

    # First trainer
    trainer = trainers[0]
    print(trainer["greeting"])
    print()
    input("(Press Enter to battle...)")
    print()
    team = [create_pokemon(name, level) for name, level in trainer["team"]]
    result = battle(player, team, is_wild=False)
    if result == "lose":
        return "lose"
    print()
    print(trainer["defeat_text"])
    player["money"] += trainer["reward"]
    print(f"{trainer['name']} gave you ${trainer['reward']}!")
    print()
    pause()

    # Tall grass before the event
    print("There's tall grass ahead.")
    print()
    enter = input("Enter the tall grass? (y/n): ").strip().lower()
    print()
    if enter == "y":
        result = tall_grass(player, wild_pokemon)
        if result == "lose":
            return "lose"

    # Hydrapple event
    print("You hear a low hiss from deeper in the trees.")
    print()
    pause()

    print("Two Team Fairy grunts are crowding a Hydrapple against a boulder.")
    print("It isn't moving. It's watching them very carefully.")
    print()
    pause()

    print("Team Fairy Grunt: Come on. We just need one.")
    print("Team Fairy Grunt 2: It's not going to come quietly. Just grab it.")
    print()
    pause()

    print("NH steps out of the trees.")
    print()
    pause()

    print("Team Fairy Grunt: Back off. This doesn't involve you.")
    print()
    pause()

    print("NH: *looks at the Hydrapple*")
    print("NH: Yeah it does.")
    print()
    input("(Press Enter to battle...)")
    print()

    result = battle(
        player,
        [create_pokemon("Snubbull", 44), create_pokemon("Granbull", 46)],
        is_wild=False
    )
    if result == "lose":
        return "lose"

    print()
    print("The grunts run.")
    print()
    pause()

    print("The Hydrapple watches them go.")
    print("Then it turns to NH.")
    print()
    pause()

    print("NH: You're okay.")
    print()
    pause()

    print("The Hydrapple steps forward and bumps NH's hand with its head.")
    print()
    pause()

    starter_level = player["party"][0]["level"]
    hydrapple = create_pokemon("Hydrapple", starter_level)
    player["party"].append(hydrapple)
    print(f"Hydrapple (Lv.{starter_level}) joined the party!")
    print()
    pause()

    # Second trainer
    trainer = trainers[1]
    print(trainer["greeting"])
    print()
    input("(Press Enter to battle...)")
    print()
    team = [create_pokemon(name, level) for name, level in trainer["team"]]
    result = battle(player, team, is_wild=False)
    if result == "lose":
        return "lose"
    print()
    print(trainer["defeat_text"])
    player["money"] += trainer["reward"]
    print(f"{trainer['name']} gave you ${trainer['reward']}!")
    print()
    pause()

    print("The forest opens up.")
    print("Castelia City fills the horizon — towers of glass and concrete,")
    print("stacked so high they disappear into the haze.")
    print()
    pause()

    from castelia_city import castelia_city
    return castelia_city(player)
