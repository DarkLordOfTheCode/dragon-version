import random
from battle import battle, calculate_damage, enemy_attack, give_exp, switch_pokemon, use_healing_item, HEALING_ITEMS
from pokemon import create_pokemon
from gym_leaders import gym_leaders
from sprites import get_sprite, hp_bar

SABINA = gym_leaders[0]


def pause():
    input("(Press Enter to continue...)")
    print()


def pokecenter(player):
    print("=" * 40)
    print("  POKÉMON CENTER")
    print("=" * 40)
    print()
    print("Nurse Joy: Welcome! We'll restore your")
    print("Pokémon to full health.")
    print()
    pause()
    for mon in player["party"]:
        mon["hp"] = mon["max_hp"]
    print("Your Pokémon have been healed!")
    print()
    pause()


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
    print("A familiar voice from somewhere inside the crowd.")
    print()
    pause()

    print("Nico: NH. WHAT.")
    print()
    pause()

    print("NH: Nico?!")
    print()
    pause()

    print("Nico: What are you doing in Saffron City?")
    print()
    pause()

    print("NH: What are YOU doing in Saffron City?")
    print()
    pause()

    print("Nico: I asked first.")
    print()
    pause()

    print("NH: Journey. Gyms. The whole thing.")
    print()
    pause()

    print("Nico: *stares*")
    print("Nico: Me too.")
    print()
    pause()

    print("NH: No way.")
    print()
    pause()

    print("Nico: I left three weeks ago. Didn't tell anyone.")
    print()
    pause()

    print("NH: You didn't tell anyone?")
    print()
    pause()

    print("Nico: I told my mum.")
    print("Nico: ...She cried.")
    print()
    pause()

    print("NH: Okay — since we're both here —")
    print()
    pause()

    print("Nico: Battle. Obviously.")
    print()
    pause()

    print("NH: I was going to say get food but sure.")
    print()
    pause()

    print("Nico: Food after. Battle now. I've been waiting")
    print("two years for this.")
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
    print("Nico: *looks at his Pokémon*")
    print("Nico: ...Okay.")
    print()
    pause()

    print("NH: You brought a Caterpie.")
    print()
    pause()

    print("Nico: He's got heart.")
    print()
    pause()

    print("NH: He went down in one hit.")
    print()
    pause()

    print("Nico: He's building character.")
    print("Nico: Rematch after the gym. Don't disappear.")
    print()
    pause()

    print("Nico pushed further into the mall.")
    print()
    pause()

    return "win"


def show_double_battle_screen(player_mon, nico_mon, enemy_mon):
    p_lines = get_sprite(player_mon["name"])
    n_lines = get_sprite(nico_mon["name"])
    e_lines = get_sprite(enemy_mon["name"])

    height = max(len(p_lines), len(n_lines), len(e_lines))
    while len(p_lines) < height:
        p_lines.append("")
    while len(n_lines) < height:
        n_lines.append("")
    while len(e_lines) < height:
        e_lines.append("")

    p_width = max((len(l) for l in p_lines), default=9)
    n_width = max((len(l) for l in n_lines), default=9)
    e_width = max((len(l) for l in e_lines), default=9)
    gap_in  = "  "
    gap_out = "       "

    print()
    for p_line, n_line, e_line in zip(p_lines, n_lines, e_lines):
        print(p_line.ljust(p_width) + gap_in + n_line.ljust(n_width) + gap_out + e_line.ljust(e_width))

    p_bar = hp_bar(player_mon["hp"], player_mon["max_hp"])
    n_bar = hp_bar(nico_mon["hp"], nico_mon["max_hp"])
    e_bar = hp_bar(enemy_mon["hp"], enemy_mon["max_hp"])
    p_label = f"  {player_mon['name']} Lv.{player_mon['level']}  {p_bar} {player_mon['hp']}/{player_mon['max_hp']}"
    n_label = f"  Nico's {nico_mon['name']} Lv.{nico_mon['level']}  {n_bar} {nico_mon['hp']}/{nico_mon['max_hp']}"
    e_label = f"  {enemy_mon['name']} Lv.{enemy_mon['level']}  {e_bar} {enemy_mon['hp']}/{enemy_mon['max_hp']}"
    print(p_label.ljust(p_width + len(gap_in)) + n_label.ljust(n_width + len(gap_out)) + e_label)
    print()


def gym_double_battle(player, nico_party, enemy_party):
    enemy_index = 0
    enemy_mon = enemy_party[enemy_index]
    nico_index = 0
    nico_mon = nico_party[nico_index]

    print(f"\n{enemy_mon['name']} was sent out!")
    player_mon = next(p for p in player["party"] if p["hp"] > 0)
    print(f"Go, {player_mon['name']}!")
    print(f"Nico sent out {nico_mon['name']}!")
    print()

    while True:
        show_double_battle_screen(player_mon, nico_mon, enemy_mon)
        enemy_hp_before = enemy_mon["hp"]
        print("What will you do?")
        print("  1. Fight")
        print("  2. Bag")
        print("  3. Pokémon")
        action = input("\nChoose: ").strip()
        print()

        used_turn = False

        if action == "1":
            print("Choose a move:")
            for i, move_name in enumerate(player_mon["moves"]):
                print(f"  {i + 1}. {move_name}")
            move_choice = input("Enter number: ").strip()
            try:
                move_name = player_mon["moves"][int(move_choice) - 1]
                damage, effectiveness = calculate_damage(player_mon, move_name, enemy_mon)
                enemy_mon["hp"] = max(0, enemy_mon["hp"] - damage)
                print(f"\n  {player_mon['name']} used {move_name}!")
                if effectiveness == 0:
                    print("  It had no effect...")
                elif effectiveness > 1:
                    print("  It's super effective!")
                elif effectiveness < 1:
                    print("  It's not very effective...")
                print(f"  {enemy_mon['name']} took {damage} damage. HP: {enemy_mon['hp']}/{enemy_mon['max_hp']}")
                used_turn = True
            except (ValueError, IndexError):
                print("Invalid move.")

        elif action == "2":
            heal_options = [(n, a) for n, a in HEALING_ITEMS.items() if player["bag"].get(n, 0) > 0]
            if not heal_options:
                print("Nothing useful in your bag!")
            else:
                for i, (name, _) in enumerate(heal_options, 1):
                    print(f"  {i}. {name}  x{player['bag'].get(name, 0)}")
                print(f"  {len(heal_options) + 1}. Back")
                bag_choice = input("Choose: ").strip()
                print()
                try:
                    bidx = int(bag_choice) - 1
                    if 0 <= bidx < len(heal_options):
                        name, heal_amount = heal_options[bidx]
                        used_turn = use_healing_item(player, player_mon, name, heal_amount)
                except (ValueError, IndexError):
                    print("Invalid choice.")

        elif action == "3":
            new_mon = switch_pokemon(player, player_mon)
            if new_mon is not player_mon:
                player_mon = new_mon
                used_turn = True

        else:
            print("Invalid choice.")

        if not used_turn:
            continue

        # Nico auto-attacks
        if nico_mon["hp"] > 0 and enemy_hp_before > 0:
            move_name = random.choice(nico_mon["moves"])
            damage, effectiveness = calculate_damage(nico_mon, move_name, enemy_mon)
            print(f"  Nico's {nico_mon['name']} used {move_name}!")
            if enemy_mon["hp"] > 0:
                enemy_mon["hp"] = max(0, enemy_mon["hp"] - damage)
                if effectiveness > 1:
                    print("  It's super effective!")
                elif effectiveness < 1:
                    print("  It's not very effective...")
                print(f"  {enemy_mon['name']} took {damage} damage. HP: {enemy_mon['hp']}/{enemy_mon['max_hp']}")
            else:
                print(f"  But {enemy_mon['name']} had already fainted!")
            print()

        # Check enemy fainted
        if enemy_mon["hp"] <= 0:
            print(f"  {enemy_mon['name']} fainted!")
            give_exp(player_mon, enemy_mon, is_trainer=True)
            enemy_index += 1
            if enemy_index >= len(enemy_party):
                print("\nYou won the battle!")
                return "win"
            enemy_mon = enemy_party[enemy_index]
            print(f"  {enemy_mon['name']} was sent out!")
            continue

        # Enemy attacks a random target
        print()
        alive_targets = [t for t in [player_mon, nico_mon] if t["hp"] > 0]
        target = random.choice(alive_targets)
        enemy_attack(enemy_mon, target)
        print()

        # Check if player mon fainted
        if player_mon["hp"] <= 0:
            print(f"  {player_mon['name']} fainted!")
            next_mon = next((p for p in player["party"] if p["hp"] > 0), None)
            if next_mon is None:
                print("\nYou have no more Pokémon...")
                print("You blacked out.")
                return "lose"
            player_mon = next_mon
            print(f"Go, {player_mon['name']}!")

        # Check if Nico's mon fainted
        if nico_mon["hp"] <= 0:
            print(f"  Nico's {nico_mon['name']} fainted!")
            nico_index += 1
            if nico_index < len(nico_party):
                nico_mon = nico_party[nico_index]
                print(f"  Nico sent out {nico_mon['name']}!")


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

    print("Nico: *appears beside you*")
    print("Nico: Double battle?")
    print()
    pause()

    print("NH: You were already in here waiting.")
    print()
    pause()

    print("Nico: I wanted a good spot.")
    print()
    pause()

    print(SABINA["greeting"])
    print()
    pause()

    sabina_team = [create_pokemon(name, level) for name, level in SABINA["team"]]
    nico_team = [create_pokemon("Gible", 10), create_pokemon("Caterpie", 8)]
    result = gym_double_battle(player, nico_team, sabina_team)
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
        print("  2. Pokémon Center")
        print("  3. Go back to Route 1 to train")
        print("  4. Head to the northern exit")
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
            pokecenter(player)

        elif choice == "3":
            result = train_on_route(player)
            if result == "lose":
                return "lose"

        elif choice == "4":
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
