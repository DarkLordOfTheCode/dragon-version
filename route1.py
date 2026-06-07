import random
from routes import routes
from battle import battle
from pokemon import create_pokemon


def wild_encounter(player, wild_pokemon_list):
    roll = random.randint(1, 100)
    cumulative = 0
    chosen = None
    for entry in wild_pokemon_list:
        cumulative += entry["rate"]
        if roll <= cumulative:
            chosen = entry
            break
    if chosen is None:
        chosen = wild_pokemon_list[-1]

    level = random.randint(chosen["min_level"], chosen["max_level"])
    enemy = create_pokemon(chosen["name"], level)
    return battle(player, [enemy], is_wild=True)


def tall_grass(player, wild_pokemon_list):
    print("You step into the tall grass.")
    print()
    while True:
        print("1. Keep walking")
        print("2. Leave the tall grass")
        choice = input("Choose: ").strip()
        print()
        if choice == "2":
            print("You leave the tall grass.")
            print()
            break
        elif choice == "1":
            if random.random() < 0.5:
                result = wild_encounter(player, wild_pokemon_list)
                if result == "lose":
                    return "lose"
            else:
                print("You walked without running into anything.")
                print()
        else:
            print("Invalid choice.")


def route1(player):
    route = routes["Route 1"]
    trainers = route["trainers"]
    wild_pokemon = route["wild_pokemon"]

    print("=" * 40)
    print("  ROUTE 1")
    print("=" * 40)
    print()
    print(route["description"])
    print()
    input("(Press Enter to continue...)")
    print()

    # Teymur
    teymur = trainers[0]
    print(teymur["greeting"])
    print()
    input("(Press Enter to battle...)")
    print()
    teymur_team = [create_pokemon(name, level) for name, level in teymur["team"]]
    result = battle(player, teymur_team, is_wild=False)
    if result == "lose":
        return "lose"
    print()
    print(teymur["defeat_text"])
    player["money"] += teymur["reward"]
    print(f"{teymur['name']} gave you ${teymur['reward']}!")
    print()
    input("(Press Enter to continue...)")
    print()

    # Tall grass
    print("There's tall grass ahead.")
    print()
    enter = input("Enter the tall grass? (y/n): ").strip().lower()
    print()
    if enter == "y":
        result = tall_grass(player, wild_pokemon)
        if result == "lose":
            return "lose"

    # Nigar
    nigar = trainers[1]
    print(nigar["greeting"])
    print()
    input("(Press Enter to battle...)")
    print()
    nigar_team = [create_pokemon(name, level) for name, level in nigar["team"]]
    result = battle(player, nigar_team, is_wild=False)
    if result == "lose":
        return "lose"
    print()
    print(nigar["defeat_text"])
    player["money"] += nigar["reward"]
    print(f"{nigar['name']} gave you ${nigar['reward']}!")
    print()
    input("(Press Enter to continue...)")
    print()

    print("You arrive at Saffron City.")
    print()
    from saffron_city import saffron_city
    return saffron_city(player)
