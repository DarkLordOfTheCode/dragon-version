import random
from battle import battle
from pokemon import create_pokemon
from routes import routes


def pause():
    input("(Press Enter to continue...)")
    print()


def pick_wild(wild_pokemon_list):
    roll = random.randint(1, 100)
    cumulative = 0
    for entry in wild_pokemon_list:
        cumulative += entry["rate"]
        if roll <= cumulative:
            return entry
    return wild_pokemon_list[-1]


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
            return "done"
        elif choice == "1":
            if random.random() < 0.5:
                entry = pick_wild(wild_pokemon_list)
                level = random.randint(entry["min_level"], entry["max_level"])
                enemy = create_pokemon(entry["name"], level)
                result = battle(player, [enemy], is_wild=True)
                if result == "lose":
                    return "lose"
            else:
                print("You walked without running into anything.")
                print()
        else:
            print("Invalid choice.")
            print()


def run_route(player, route_name, next_location):
    route = routes[route_name]

    print("=" * 40)
    print(f"  {route_name.upper()}")
    print("=" * 40)
    print()
    print(route["description"])
    print()
    pause()

    trainers = route["trainers"]
    wild_pokemon = route["wild_pokemon"]

    for i, trainer in enumerate(trainers):
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

        if i < len(trainers) - 1:
            print("There's tall grass ahead.")
            print()
            enter = input("Enter the tall grass? (y/n): ").strip().lower()
            print()
            if enter == "y":
                result = tall_grass(player, wild_pokemon)
                if result == "lose":
                    return "lose"

    print(f"You arrive at {next_location}.")
    print()
    return "done"
