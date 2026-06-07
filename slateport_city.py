from pokemon import create_pokemon
from gym_leaders import gym_leaders
from battle import battle

CORAL = gym_leaders[2]


def pause():
    input("(Press Enter to continue...)")
    print()


def pokecenter(player):
    print("=" * 40)
    print("  POKÉMON CENTER")
    print("=" * 40)
    print()
    print("Nurse: Welcome! We'll restore your Pokémon to full health.")
    print()
    pause()
    for mon in player["party"]:
        mon["hp"] = mon["max_hp"]
    print("Nurse: Your Pokémon are fully healed!")
    print()
    pause()


def teach_move(player, move_name):
    print(f"Teach {move_name} to which Pokémon?")
    print()
    for i, mon in enumerate(player["party"], 1):
        moves_str = ", ".join(mon["moves"])
        print(f"  {i}. {mon['name']} Lv.{mon['level']}  [{moves_str}]")
    print(f"  {len(player['party']) + 1}. Cancel")
    print()
    choice = input("Choose: ").strip()
    print()
    try:
        idx = int(choice) - 1
        if idx == len(player["party"]):
            print("Cancelled.")
            print()
            return
        mon = player["party"][idx]
        if move_name in mon["moves"]:
            print(f"{mon['name']} already knows {move_name}.")
            print()
            return
        if len(mon["moves"]) < 4:
            mon["moves"].append(move_name)
            print(f"{mon['name']} learned {move_name}!")
            print()
        else:
            print(f"{mon['name']} wants to learn {move_name}.")
            print("It already knows 4 moves. Forget which one?")
            print()
            for i, m in enumerate(mon["moves"], 1):
                print(f"  {i}. {m}")
            print("  5. Cancel")
            print()
            forget = input("Choose: ").strip()
            print()
            try:
                fidx = int(forget) - 1
                if fidx == 4:
                    print("Cancelled. TM not used.")
                    print()
                elif 0 <= fidx < 4:
                    old = mon["moves"][fidx]
                    mon["moves"][fidx] = move_name
                    print(f"{mon['name']} forgot {old} and learned {move_name}!")
                    print()
                else:
                    print("Invalid choice. TM not used.")
                    print()
            except ValueError:
                print("Invalid choice. TM not used.")
                print()
    except ValueError:
        print("Invalid choice.")
        print()


def mall_shop(player):
    print()
    print("=" * 40)
    print("  SLATEPORT MALL — FLOOR 1")
    print("=" * 40)
    print()

    items = [
        ("Super Potion",  700),
        ("Hyper Potion", 1200),
        ("Great Ball",    600),
        ("Ultra Ball",   1200),
    ]

    while True:
        print(f"  Money: ${player['money']}")
        print()
        for i, (name, price) in enumerate(items, 1):
            print(f"  {i}. {name:<15} ${price}")
        print("  5. Leave")
        print()
        choice = input("Choose: ").strip()
        print()
        if choice == "5":
            return
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(items):
                name, price = items[idx]
                if player["money"] < price:
                    print("Not enough money.")
                    print()
                else:
                    player["money"] -= price
                    player["bag"][name] = player["bag"].get(name, 0) + 1
                    print(f"You bought {name}!")
                    print()
            else:
                print("Invalid choice.")
                print()
        except ValueError:
            print("Invalid choice.")
            print()


def mall_tm_shop(player):
    print()
    print("=" * 40)
    print("  SLATEPORT MALL — FLOOR 2 TM SHOP")
    print("=" * 40)
    print()

    tms = [
        ("Surf",         "Water",  2000),
        ("Hydro Pump",   "Water",  3000),
        ("Ice Beam",     "Ice",    2000),
        ("Dragon Pulse", "Dragon", 2500),
        ("Outrage",      "Dragon", 3500),
        ("Thunder",      "Electric", 3000),
    ]

    while True:
        print(f"  Money: ${player['money']}")
        print()
        for i, (name, type_, price) in enumerate(tms, 1):
            print(f"  {i}. TM {name:<14} ({type_:<8}) ${price}")
        print(f"  {len(tms) + 1}. Leave")
        print()
        choice = input("Choose: ").strip()
        print()
        if choice == str(len(tms) + 1):
            return
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(tms):
                name, type_, price = tms[idx]
                if player["money"] < price:
                    print("Not enough money.")
                    print()
                else:
                    player["money"] -= price
                    print(f"You bought TM {name}!")
                    print()
                    teach_move(player, name)
            else:
                print("Invalid choice.")
                print()
        except ValueError:
            print("Invalid choice.")
            print()


def mall(player):
    print()
    print("=" * 40)
    print("  SLATEPORT MALL")
    print("=" * 40)
    print()

    while True:
        print("Where do you want to go?")
        print("  1. Floor 1  — General Store")
        print("  2. Floor 2  — TM Shop")
        print("  3. Leave the mall")
        print()
        choice = input("Choose: ").strip()
        print()
        if choice == "1":
            mall_shop(player)
        elif choice == "2":
            mall_tm_shop(player)
        elif choice == "3":
            return
        else:
            print("Invalid choice.")
            print()


def slateport_city(player):
    print("=" * 40)
    print("  SLATEPORT CITY")
    print("=" * 40)
    print()
    print("The smell of the sea hits you immediately.")
    print("Slateport City — a port town built on the coast,")
    print("oil tankers in the harbour, seagulls overhead.")
    print()
    pause()

    state = {"gym_beaten": False}

    while True:
        print("=" * 40)
        print("  SLATEPORT CITY")
        print("=" * 40)
        print()
        print("What do you want to do?")
        print("  1. Gym")
        print("  2. Pokémon Center")
        print("  3. Mall")
        print("  4. Head east")
        print()
        choice = input("Choose: ").strip()
        print()

        if choice == "1":
            if state["gym_beaten"]:
                print("You already have the Tide Badge.")
                print()
            else:
                print("=" * 40)
                print("  SLATEPORT CITY GYM")
                print("=" * 40)
                print()
                print("The gym smells of saltwater. The floor is wet stone.")
                print()
                pause()
                print(CORAL["greeting"])
                print()
                input("(Press Enter to battle...)")
                print()
                team = [create_pokemon(name, level) for name, level in CORAL["team"]]
                result = battle(player, team, is_wild=False)
                if result == "lose":
                    return "lose"
                print()
                print("Coral: The tide turns. Well battled.")
                print("Coral: Take the Tide Badge. You've earned it.")
                print()
                player["money"] += CORAL["reward"]
                print("NH received the Tide Badge!")
                print(f"Coral gave you ${CORAL['reward']}!")
                print()
                pause()
                state["gym_beaten"] = True

        elif choice == "2":
            pokecenter(player)

        elif choice == "3":
            mall(player)

        elif choice == "4":
            if not state["gym_beaten"]:
                print("You should challenge the gym before moving on.")
                print()
            else:
                print("You leave Slateport City heading east.")
                print()
                pause()
                return "done"

        else:
            print("Invalid choice.")
            print()
