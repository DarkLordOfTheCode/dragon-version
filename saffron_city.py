import random
from battle import battle
from pokemon import create_pokemon
from gym_leaders import gym_leaders

SABINA = gym_leaders[0]


def pause():
    input("(Press Enter to continue...)")
    print()


def arrive(player):
    print("=" * 40)
    print("  SAFFRON CITY")
    print("=" * 40)
    print()
    print("You step off the road and into Saffron City.")
    print("It's massive — towers of glass and steel,")
    print("crowds moving in every direction.")
    print()
    pause()

    print("At the northern gate, a figure in white and pink")
    print("leans against the barrier.")
    print()
    pause()

    print("Team Fairy Grunt: *steps forward*")
    print("Team Fairy Grunt: This road's closed. Move along.")
    print()
    pause()

    print("NH: Closed? Since when?")
    print()
    pause()

    print("Team Fairy Grunt: Since us. Back off.")
    print()
    pause()

    print("(The northern exit is blocked by Team Fairy.)")
    print()
    pause()


def train_on_route(player):
    from routes import routes
    wild_pokemon = routes["Route 1"]["wild_pokemon"]

    print("You head back down Route 1.")
    print()
    while True:
        print("1. Walk through tall grass")
        print("2. Return to Saffron City")
        choice = input("Choose: ").strip()
        print()
        if choice == "2":
            print("You head back to Saffron City.")
            print()
            return "done"
        elif choice == "1":
            if random.random() < 0.5:
                entry = random.choice(wild_pokemon)
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


def shop(player):
    print()
    print("=" * 40)
    print("  FLOOR 1 — GENERAL STORE")
    print("=" * 40)
    print()

    items = [
        ("Potion",       300),
        ("Super Potion",  700),
        ("Poké Ball",    200),
        ("Great Ball",   600),
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
                    return
                old = mon["moves"][fidx]
                mon["moves"][fidx] = move_name
                print(f"{mon['name']} forgot {old} and learned {move_name}!")
                print()
            except (ValueError, IndexError):
                print("Invalid choice. TM not used.")
                print()
    except (ValueError, IndexError):
        print("Invalid choice.")
        print()


def tm_shop(player):
    print()
    print("=" * 40)
    print("  FLOOR 2 — TM SHOP")
    print("=" * 40)
    print()

    tms = [
        ("Shadow Ball",  "Ghost",    1500),
        ("Thunderbolt",  "Electric", 2000),
        ("Ice Beam",     "Ice",      2000),
        ("Rock Slide",   "Rock",     1500),
        ("Bulldoze",     "Ground",   1000),
        ("Flame Charge", "Fire",     1000),
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


def nico_encounter(player):
    print("=" * 40)
    print()
    print("A boy about your age pushes through the mall entrance.")
    print("He's got a scarf around his neck and a Poké Ball")
    print("already in his hand.")
    print()
    pause()

    print("???: Hey! You're NH, aren't you.")
    print()
    pause()

    print("NH: ...Do I know you?")
    print()
    pause()

    print("Nico: Nico. Word travels — everyone on Route 1 is")
    print("talking about the trainer who swept through.")
    print()
    pause()

    print("NH: I did break a little sweat.")
    print()
    pause()

    print("Nico: *laughs* Battle me. Right now.")
    print()
    pause()

    print("NH: You're not going to let me say no, are you.")
    print()
    pause()

    print("Nico: Absolutely not.")
    print()
    pause()

    nico_team = [
        create_pokemon("Gible", 10),
        create_pokemon("Caterpie", 8),
    ]
    result = battle(player, nico_team, is_wild=False)
    if result == "lose":
        return "lose"

    print()
    print("Nico: *stares at his Pokémon*")
    print("Nico: ...Okay. You're better than I thought.")
    print()
    pause()

    print("NH: Train harder.")
    print()
    pause()

    print("Nico: *grins* Rematch after the gym. Count on it.")
    print()
    pause()

    print("Nico ran off further into the mall.")
    print()
    pause()

    return "win"


def gym_battle(player):
    print()
    print("=" * 40)
    print("  SAFFRON CITY GYM")
    print("  (Mall — Lower Level)")
    print("=" * 40)
    print()
    print("The gym floor is polished white marble.")
    print("At the centre, Sabina stands with her eyes closed.")
    print()
    pause()

    print(SABINA["greeting"])
    print()
    pause()

    sabina_team = [create_pokemon(name, level) for name, level in SABINA["team"]]
    result = battle(player, sabina_team, is_wild=False)
    if result == "lose":
        return "lose"

    print()
    print("Sabina: *opens her eyes slowly*")
    print("Sabina: You fight with your whole self. I felt that.")
    print("Sabina: The Soul Badge is yours.")
    print()
    pause()

    player["money"] += SABINA["reward"]
    player["badges"] = player.get("badges", [])
    player["badges"].append("Soul Badge")
    print("NH received the Soul Badge!")
    print(f"Sabina gave you ${SABINA['reward']}!")
    print()
    pause()

    print("Sabina: One more thing.")
    print("Sabina: Something has been happening in this mall.")
    print("Sabina: Floor minus one. I've been hearing things.")
    print("Sabina: The door is now open. Be careful.")
    print()
    pause()

    return "win"


def team_fairy_hideout(player):
    print()
    print("=" * 40)
    print("  FLOOR -1 — TEAM FAIRY HIDEOUT")
    print("=" * 40)
    print()
    print("The staircase leads down into flickering pink light.")
    print("Boxes of supplies line the walls. A flag —")
    print("white with a pink star — hangs from the ceiling.")
    print()
    pause()

    print("Team Fairy Grunt: HEY! You're not supposed to be here!")
    print()
    pause()

    print("NH: And yet here I am.")
    print()
    pause()

    grunt_team = [
        create_pokemon("Clefairy", 14),
        create_pokemon("Snubbull", 14),
    ]
    result = battle(player, grunt_team, is_wild=False)
    if result == "lose":
        return "lose"

    print()
    print("Team Fairy Grunt: *into radio* We've been compromised.")
    print("Team Fairy Grunt: Fall back.")
    print()
    pause()

    print("The grunt shoves past you up the stairs.")
    print()
    pause()

    print("The hideout is abandoned. Crates, pink banners,")
    print("scattered documents — everyone's gone.")
    print()
    pause()

    print("NH: What were they doing here...")
    print()
    pause()

    print("You head back upstairs. The northern gate is unguarded.")
    print()
    pause()

    return "win"


def mall(player, state):
    print()
    print("=" * 40)
    print("  SAFFRON MALL")
    print("=" * 40)
    print()

    while True:
        print("Where do you want to go?")
        print("  1. Floor 1  — General Store")
        print("  2. Floor 2  — TM Shop")
        print("  3. Gym")
        if state["hideout_done"]:
            print("  4. Floor -1 — [CLEARED]")
        elif state["gym_beaten"]:
            print("  4. Floor -1 — [UNLOCKED]")
        else:
            print("  4. Floor -1 — [LOCKED]")
        print("  5. Leave the mall")
        print()
        choice = input("Choose: ").strip()
        print()

        if choice == "1":
            shop(player)
        elif choice == "2":
            tm_shop(player)
        elif choice == "3":
            if state["gym_beaten"]:
                print("You already have the Soul Badge.")
                print()
            else:
                result = gym_battle(player)
                if result == "lose":
                    return "lose"
                state["gym_beaten"] = True
        elif choice == "4":
            if not state["gym_beaten"]:
                print("The door is locked. A sign reads: 'Staff only.'")
                print()
            elif state["hideout_done"]:
                print("The hideout is empty. Nothing more to do here.")
                print()
            else:
                result = team_fairy_hideout(player)
                if result == "lose":
                    return "lose"
                state["hideout_done"] = True
        elif choice == "5":
            return "done"
        else:
            print("Invalid choice.")
            print()


def saffron_city(player):
    arrive(player)

    state = {
        "nico_met":    False,
        "gym_beaten":  False,
        "hideout_done": False,
    }

    while True:
        print("=" * 40)
        print("  SAFFRON CITY")
        print("=" * 40)
        print()
        print("What do you want to do?")
        print("  1. Enter the mall")
        print("  2. Go back to Route 1 to train")
        print("  3. Head to the northern exit")
        print()
        choice = input("Choose: ").strip()
        print()

        if choice == "1":
            if not state["nico_met"]:
                result = nico_encounter(player)
                if result == "lose":
                    return "lose"
                state["nico_met"] = True
            result = mall(player, state)
            if result == "lose":
                return "lose"

        elif choice == "2":
            result = train_on_route(player)
            if result == "lose":
                return "lose"

        elif choice == "3":
            if not state["hideout_done"]:
                print("Team Fairy Grunt: *steps in your way*")
                print("Team Fairy Grunt: Road's still closed.")
                print()
                if not state["gym_beaten"]:
                    print("(Beat the gym at the mall to make progress.)")
                else:
                    print("(Something is happening in the mall basement...)")
                print()
            else:
                print("The northern gate is open.")
                print("The Team Fairy grunt is gone.")
                print()
                pause()
                print("You leave Saffron City.")
                print()
                pause()
                return "done"

        else:
            print("Invalid choice.")
            print()
