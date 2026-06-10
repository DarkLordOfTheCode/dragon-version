from pokemon import create_pokemon
from gym_leaders import gym_leaders
from battle import battle
from sprites import show_battle_screen, hp_bar

CORAL = gym_leaders[2]


def pause():
    input("(Press Enter to continue...)")
    print()


def pokecenter(player):
    from pc import pc_box
    while True:
        print("=" * 40)
        print("  POKÉMON CENTER")
        print("=" * 40)
        print()
        print("  1. Heal Pokémon")
        print("  2. PC Box")
        print("  3. Leave")
        print()
        choice = input("Choose: ").strip()
        print()
        if choice == "1":
            for mon in player["party"]:
                mon["hp"] = mon["max_hp"]
            print("Nurse: Your Pokémon are fully healed!")
            print()
            pause()
        elif choice == "2":
            pc_box(player)
        elif choice == "3":
            return
        else:
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


def move_reminder(player):
    from learnsets import learnsets
    print()
    print("=" * 40)
    print("  MOVE REMINDER  (Free)")
    print("=" * 40)
    print()
    print("Which Pokémon?")
    print()
    for i, mon in enumerate(player["party"], 1):
        print(f"  {i}. {mon['name']} Lv.{mon['level']}")
    print(f"  {len(player['party']) + 1}. Leave")
    print()
    choice = input("Choose: ").strip()
    print()
    try:
        idx = int(choice) - 1
        if idx == len(player["party"]):
            return
        if not (0 <= idx < len(player["party"])):
            print("Invalid choice.")
            print()
            return
        mon = player["party"][idx]
        if mon["name"] not in learnsets:
            print(f"{mon['name']} has no moves to be reminded of.")
            print()
            return
        available = []
        for lv, moves in learnsets[mon["name"]].items():
            if lv <= mon["level"]:
                for move in moves:
                    if move not in mon["moves"] and move not in available:
                        available.append(move)
        if not available:
            print(f"{mon['name']} already knows all its available moves.")
            print()
            return
        print(f"Moves {mon['name']} can relearn:")
        print()
        for i, move in enumerate(available, 1):
            print(f"  {i}. {move}")
        print(f"  {len(available) + 1}. Cancel")
        print()
        choice = input("Choose: ").strip()
        print()
        try:
            midx = int(choice) - 1
            if midx == len(available):
                return
            if 0 <= midx < len(available):
                teach_move(player, available[midx])
            else:
                print("Invalid choice.")
                print()
        except ValueError:
            print("Invalid choice.")
            print()
    except ValueError:
        print("Invalid choice.")
        print()


def double_battle(player, sam_party, enemy_party):
    from battle import calculate_damage, enemy_attack, give_exp, switch_pokemon, use_healing_item, HEALING_ITEMS
    enemy_index = 0
    enemy_mon = enemy_party[enemy_index]
    sam_index = 0
    sam_mon = sam_party[sam_index]

    print(f"\n{enemy_mon['name']} was sent out!")
    player_mon = next(p for p in player["party"] if p["hp"] > 0)
    print(f"Go, {player_mon['name']}!")
    print(f"S sent out {sam_mon['name']}!")
    print()

    while True:
        show_battle_screen(player_mon, enemy_mon)
        if sam_mon["hp"] > 0:
            bar = hp_bar(sam_mon["hp"], sam_mon["max_hp"])
            print(f"  S's {sam_mon['name']} Lv.{sam_mon['level']}  {bar} {sam_mon['hp']}/{sam_mon['max_hp']}")
            print()

        print("What will you do?")
        print("  1. Fight")
        print("  2. Bag")
        print("  3. Pokémon")
        action = input("\nChoose: ").strip()
        print()

        if action == "1":
            if not player_mon["moves"]:
                print(f"{player_mon['name']} has no moves!")
                print()
                continue
            print("Choose a move:")
            for i, move in enumerate(player_mon["moves"], 1):
                print(f"  {i}. {move}")
            move_choice = input("Choose: ").strip()
            print()
            try:
                midx = int(move_choice) - 1
                if 0 <= midx < len(player_mon["moves"]):
                    move_name = player_mon["moves"][midx]
                    dmg, eff = calculate_damage(player_mon, move_name, enemy_mon)
                    enemy_mon["hp"] = max(0, enemy_mon["hp"] - dmg)
                    print(f"{player_mon['name']} used {move_name}!")
                    if eff == 0:
                        print("It had no effect...")
                    elif eff > 1:
                        print("It's super effective!")
                    elif eff < 1:
                        print("It's not very effective...")
                    print()
                else:
                    print("Invalid choice.")
                    print()
                    continue
            except ValueError:
                print("Invalid choice.")
                print()
                continue

        elif action == "2":
            result = use_healing_item(player, player_mon)
            if result == "no_items":
                print("No healing items.")
                print()
                continue

        elif action == "3":
            result = switch_pokemon(player, player_mon)
            if result:
                player_mon = result
            continue

        else:
            print("Invalid choice.")
            print()
            continue

        if enemy_mon["hp"] <= 0:
            print(f"{enemy_mon['name']} fainted!")
            give_exp(player_mon, enemy_mon)
            print()
            enemy_index += 1
            if enemy_index >= len(enemy_party):
                return "win"
            enemy_mon = enemy_party[enemy_index]
            print(f"Foe sent out {enemy_mon['name']}!")
            print()
            continue

        if sam_mon["hp"] > 0:
            sam_move = sam_mon["moves"][0] if sam_mon["moves"] else None
            if sam_move:
                dmg, eff = calculate_damage(sam_mon, sam_move, enemy_mon)
                enemy_mon["hp"] = max(0, enemy_mon["hp"] - dmg)
                print(f"S's {sam_mon['name']} used {sam_move}!")
                print()
                if enemy_mon["hp"] <= 0:
                    print(f"{enemy_mon['name']} fainted!")
                    give_exp(player_mon, enemy_mon)
                    print()
                    enemy_index += 1
                    if enemy_index >= len(enemy_party):
                        return "win"
                    enemy_mon = enemy_party[enemy_index]
                    print(f"Foe sent out {enemy_mon['name']}!")
                    print()
                    continue

        dmg, _ = enemy_attack(enemy_mon, player_mon)
        player_mon["hp"] = max(0, player_mon["hp"] - dmg)
        print(f"Enemy {enemy_mon['name']} used {enemy_mon['moves'][0] if enemy_mon['moves'] else 'Tackle'}!")
        print()

        if player_mon["hp"] <= 0:
            print(f"{player_mon['name']} fainted!")
            print()
            next_mon = next((p for p in player["party"] if p["hp"] > 0), None)
            if not next_mon:
                return "lose"
            player_mon = next_mon
            print(f"Go, {player_mon['name']}!")
            print()

        if sam_mon["hp"] <= 0:
            sam_index += 1
            if sam_index < len(sam_party):
                sam_mon = sam_party[sam_index]
                print(f"S sent out {sam_mon['name']}!")
                print()


def submarine(player):
    print("=" * 40)
    print("  TEAM FAIRY SUBMARINE")
    print("=" * 40)
    print()
    print("Down at the harbour, a black submarine sits")
    print("docked between two oil tankers. Team Fairy insignia")
    print("stamped on the side. No one seems to have noticed.")
    print()
    pause()

    print("S: *already there when you arrive*")
    print("S: Been watching it for an hour. Three grunts")
    print("S: on the dock, more inside. They're loading something.")
    print()
    pause()

    print("NH: What are they loading?")
    print()
    pause()

    print("S: Don't know. That's why we're going in.")
    print()
    pause()

    sam_team = [create_pokemon("Charizard", 30), create_pokemon("Kingdra", 28)]

    # Dock
    print("Team Fairy Grunt: Hey — this is a restricted dock!")
    print()
    pause()

    print("S: Great. *sends out Charizard*")
    print()
    pause()

    result = double_battle(
        player, sam_team,
        [create_pokemon("Clefairy", 25), create_pokemon("Snubbull", 25)]
    )
    if result == "lose":
        return "lose"

    print()
    print("Team Fairy Grunt: *into radio* We've got trainers on the dock—")
    print()
    pause()

    print("S: Inside. Now.")
    print()
    pause()

    # Inside the submarine
    print("The interior is cramped. Wiring everywhere.")
    print("Pink banners in a submarine. Somehow worse than the tower.")
    print()
    pause()

    print("Team Fairy Grunt: You shouldn't be in here.")
    print()
    pause()

    print("NH: What are you loading?")
    print()
    pause()

    print("Team Fairy Grunt: None of your—")
    print()
    pause()

    result = double_battle(
        player, sam_team,
        [create_pokemon("Granbull", 27), create_pokemon("Sylveon", 26)]
    )
    if result == "lose":
        return "lose"

    print()
    print("S: *finds manifest on a crate*")
    print("S: ...This is a lot of Pokéballs.")
    print()
    pause()

    print("NH: They're capturing something.")
    print()
    pause()

    print("S: Something big, by the looks of it.")
    print("S: We should tell Larch.")
    print()
    pause()

    # Commander
    print("A door opens at the far end of the corridor.")
    print()
    pause()

    print("Team Fairy Commander: You've seen too much.")
    print()
    pause()

    print("S: Yeah. We tend to do that.")
    print()
    pause()

    result = double_battle(
        player, sam_team,
        [create_pokemon("Togekiss", 29), create_pokemon("Gardevoir", 30)]
    )
    if result == "lose":
        return "lose"

    print()
    print("Team Fairy Commander: *steps back*")
    print("Team Fairy Commander: It doesn't matter. It's already done.")
    print()
    pause()

    print("The commander retreats. The submarine begins to submerge.")
    print()
    pause()

    print("S: Time to go.")
    print()
    pause()

    print("You and S make it off the dock before it sinks below the waterline.")
    print()
    pause()

    print("S: Whatever they're after — it's underwater.")
    print("S: We'll need to figure that out eventually.")
    print()
    pause()

    return "done"


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
        print("  3. Move Reminder (Free)")
        print("  4. Leave the mall")
        print()
        choice = input("Choose: ").strip()
        print()
        if choice == "1":
            mall_shop(player)
        elif choice == "2":
            mall_tm_shop(player)
        elif choice == "3":
            move_reminder(player)
        elif choice == "4":
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

    state = {"gym_beaten": False, "submarine_done": False}

    while True:
        print("=" * 40)
        print("  SLATEPORT CITY")
        print("=" * 40)
        print()
        print("What do you want to do?")
        print("  1. Gym")
        print("  2. Pokémon Center")
        print("  3. Mall")
        print("  4. Harbour — Team Fairy Submarine")
        print("  5. Head east")
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
            if state["submarine_done"]:
                print("The harbour is quiet. The submarine is gone.")
                print()
            else:
                result = submarine(player)
                if result == "lose":
                    return "lose"
                state["submarine_done"] = True

        elif choice == "5":
            if not state["gym_beaten"]:
                print("You should challenge the gym before moving on.")
                print()
            elif not state["submarine_done"]:
                print("Something is going on at the harbour.")
                print("You should check it out first.")
                print()
            else:
                print("You leave Slateport City heading east.")
                print()
                pause()
                from route13 import route13
                return route13(player)

        else:
            print("Invalid choice.")
            print()
