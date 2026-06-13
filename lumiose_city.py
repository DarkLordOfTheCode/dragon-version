from pokemon import create_pokemon
from gym_leaders import gym_leaders
from battle import battle
from sprites import show_battle_screen, hp_bar

LYSARA = gym_leaders[5]


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


def boutique(player):
    print()
    print("=" * 40)
    print("  LUMIOSE BOUTIQUE")
    print("=" * 40)
    print()

    items = [
        ("Hyper Potion", 1200),
        ("Max Potion",   2500),
        ("Ultra Ball",   1200),
        ("Revive",       1500),
        ("Max Revive",   4000),
    ]

    while True:
        print(f"  Money: ${player['money']}")
        print()
        for i, (name, price) in enumerate(items, 1):
            print(f"  {i}. {name:<15} ${price}")
        print(f"  {len(items) + 1}. Leave")
        print()
        choice = input("Choose: ").strip()
        print()
        if choice == str(len(items) + 1):
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


def tm_vendor(player):
    print()
    print("=" * 40)
    print("  PRISM TOWER TM STAND")
    print("=" * 40)
    print()

    tms = [
        ("Flamethrower", "Fire",   2500),
        ("Fire Blast",   "Fire",   3000),
        ("Dragon Pulse", "Dragon", 2500),
        ("Draco Meteor", "Dragon", 3500),
        ("Energy Ball",  "Grass",  2000),
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


def double_battle(player, partner_party, enemy_party, partner_name="S"):
    from battle import calculate_damage, enemy_attack, give_exp, switch_pokemon, use_healing_item, HEALING_ITEMS
    enemy_index = 0
    enemy_mon = enemy_party[enemy_index]
    partner_index = 0
    partner_mon = partner_party[partner_index]

    print(f"\n{enemy_mon['name']} was sent out!")
    player_mon = next(p for p in player["party"] if p["hp"] > 0)
    print(f"Go, {player_mon['name']}!")
    print(f"{partner_name} sent out {partner_mon['name']}!")
    print()

    while True:
        show_battle_screen(player_mon, enemy_mon)
        if partner_mon["hp"] > 0:
            bar = hp_bar(partner_mon["hp"], partner_mon["max_hp"])
            print(f"  {partner_name}'s {partner_mon['name']} Lv.{partner_mon['level']}  {bar} {partner_mon['hp']}/{partner_mon['max_hp']}")
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
            heal_options = [(n, a) for n, a in HEALING_ITEMS.items() if player["bag"].get(n, 0) > 0]
            if not heal_options:
                print("No healing items.")
                print()
                continue
            for i, (name, _) in enumerate(heal_options, 1):
                print(f"  {i}. {name}  x{player['bag'].get(name, 0)}")
            print(f"  {len(heal_options) + 1}. Back")
            print()
            bag_choice = input("Choose: ").strip()
            print()
            try:
                bidx = int(bag_choice) - 1
                if bidx == len(heal_options):
                    continue
                if 0 <= bidx < len(heal_options):
                    item_name, heal_amount = heal_options[bidx]
                    use_healing_item(player, player_mon, item_name, heal_amount)
                else:
                    print("Invalid choice.")
                    print()
                    continue
            except (ValueError, IndexError):
                print("Invalid choice.")
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
            give_exp(player_mon, enemy_mon, is_trainer=True)
            print()
            enemy_index += 1
            if enemy_index >= len(enemy_party):
                return "win"
            enemy_mon = enemy_party[enemy_index]
            print(f"Foe sent out {enemy_mon['name']}!")
            print()
            continue

        if partner_mon["hp"] > 0:
            partner_move = partner_mon["moves"][0] if partner_mon["moves"] else None
            if partner_move:
                dmg, eff = calculate_damage(partner_mon, partner_move, enemy_mon)
                enemy_mon["hp"] = max(0, enemy_mon["hp"] - dmg)
                print(f"{partner_name}'s {partner_mon['name']} used {partner_move}!")
                print()
                if enemy_mon["hp"] <= 0:
                    print(f"{enemy_mon['name']} fainted!")
                    give_exp(player_mon, enemy_mon, is_trainer=True)
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

        if partner_mon["hp"] <= 0:
            partner_index += 1
            if partner_index < len(partner_party):
                partner_mon = partner_party[partner_index]
                print(f"{partner_name} sent out {partner_mon['name']}!")
                print()


def prism_tower(player, state):
    print("=" * 40)
    print("  PRISM TOWER")
    print("=" * 40)
    print()
    print("Lumiose is the City of Lights — but tonight it's dark.")
    print("The boulevards are black. The cafés are shuttered.")
    print("Only one thing is still lit: Prism Tower, blazing pink")
    print("at the centre of the city, humming like a hornet's nest.")
    print()
    pause()

    print("S: *waiting at the base of the tower, arms crossed*")
    print("S: There you are. They cut the whole grid an hour ago.")
    print("S: Team Fairy walked into the tower and took the power core.")
    print()
    pause()

    print("NH: The whole city? For one tower?")
    print()
    pause()

    print("S: They're not lighting the tower. They're draining the city")
    print("S: INTO it. Siphoning every watt in Lumiose up to the top.")
    print("S: Whatever they're charging up there, it's big.")
    print()
    pause()

    print("S: I'm coming with you. Let's go turn the lights back on.")
    print()
    pause()

    # --- Lobby: grunt ---
    print("Inside, the lobby lights flicker. A grunt blocks the lift.")
    print()
    print("Team Fairy Grunt: The tower's closed for... maintenance.")
    print()
    input("(Press Enter to battle...)")
    print()

    result = battle(
        player,
        [create_pokemon("Clefable", 50), create_pokemon("Granbull", 51)],
        is_wild=False
    )
    if result == "lose":
        return "lose"

    print()
    print("S: Lift's clear. Up we go.")
    print()
    pause()

    # --- Mid-tower: double battle ---
    print("Halfway up, the lift jolts to a stop. Two admins are")
    print("waiting on the gantry, cables snaking past their feet.")
    print()
    print("Team Fairy Grunt: You don't shut this down. Nobody does.")
    print()
    input("(Press Enter to battle...)")
    print()

    s_team = [create_pokemon("Alakazam", 53), create_pokemon("Zoroark", 54)]

    result = double_battle(
        player, s_team,
        [create_pokemon("Sylveon", 52), create_pokemon("Togekiss", 53)],
        partner_name="S"
    )
    if result == "lose":
        return "lose"

    print()
    print("S: *stepping over a cable* The hum's louder up here.")
    print()
    pause()

    # --- Summit: admin boss ---
    print("The lift doors open on the summit chamber.")
    print("The power core floats in a cradle of pink light, and")
    print("every cable in the city seems to feed into it.")
    print()
    pause()

    print("Team Fairy Admin: You came all the way up here to unplug a lamp?")
    print("Team Fairy Admin: The Senate pays for this power. We're just")
    print("Team Fairy Admin: collecting. Now get off my tower.")
    print()
    input("(Press Enter to battle the Admin...)")
    print()

    result = battle(
        player,
        [
            create_pokemon("Mimikyu",   54),
            create_pokemon("Gardevoir", 55),
            create_pokemon("Clefable",  56),
        ],
        is_wild=False
    )
    if result == "lose":
        return "lose"

    print()
    print("The Admin backs away from the cradle.")
    print()
    pause()

    print("S: *yanks the main cable free of the core*")
    print()
    pause()

    print("Far below, the city comes back on all at once —")
    print("a wave of light rolling out across Lumiose.")
    print()
    pause()

    print("S: *reading a console* It wasn't random. This power was")
    print("S: routed out of the city. South. Under a Senate authorisation.")
    print()
    pause()

    print("NH: The Senate again.")
    print()
    pause()

    print("S: That same Senate seal you turned up in Castelia. They're")
    print("S: charging something, somewhere, and they don't want it on the")
    print("S: grid where anyone could trace it.")
    print()
    pause()

    print("S: We can't chase it tonight. But Lumiose has its lights back —")
    print("S: and the gym just reopened. Go take your badge.")
    print()
    pause()

    state["tower_done"] = True
    return "done"


def gym(player, state):
    print("=" * 40)
    print("  LUMIOSE CITY GYM")
    print("=" * 40)
    print()
    print("The gym is a hall of mirrors and open flame.")
    print("Every wall throws your reflection back at you, lit gold.")
    print()
    pause()

    print("Gym Trainer Solène: Lysara says light reveals everything.")
    print("Gym Trainer Solène: Let's see what yours reveals.")
    print()
    input("(Press Enter to battle...)")
    print()

    result = battle(
        player,
        [create_pokemon("Houndoom", 52), create_pokemon("Turtonator", 53)],
        is_wild=False
    )
    if result == "lose":
        return "lose"

    print()
    print("Solène: She's at the end of the hall. Don't keep her waiting.")
    print()
    pause()

    print("Lysara stands in a column of firelight, perfectly still.")
    print()
    print(LYSARA["greeting"])
    print()
    input("(Press Enter to battle Lysara...)")
    print()

    team = [create_pokemon(name, level) for name, level in LYSARA["team"]]
    result = battle(player, team, is_wild=False)
    if result == "lose":
        return "lose"

    print()
    print("Lysara: *the firelight dims*")
    print("Lysara: You carried your own light in here. I couldn't burn it out.")
    print("Lysara: That's rarer than you know. Take this.")
    print()
    pause()

    player["money"] += LYSARA["reward"]
    print("NH received the Prism Badge!")
    print(f"Lysara gave you ${LYSARA['reward']}!")
    print()
    pause()

    state["gym_beaten"] = True
    return "done"


def lumiose_city(player):
    print("=" * 40)
    print("  LUMIOSE CITY")
    print("=" * 40)
    print()
    print("Lumiose City. Boulevards spoke out from a single tower")
    print("at the heart of it all — the brightest place in Draconia.")
    print("Or it would be, if the lights were on.")
    print()
    pause()

    state = {"tower_done": False, "gym_beaten": False}

    while True:
        print("=" * 40)
        print("  LUMIOSE CITY")
        print("=" * 40)
        print()
        print("What do you want to do?")
        print("  1. Gym")
        print("  2. Pokémon Center")
        print("  3. Boutique")
        print("  4. TM Stand")
        if not state["tower_done"]:
            print("  5. Prism Tower — Team Fairy")
        else:
            print("  5. (Prism Tower cleared)")
        print("  6. Head east")
        print()
        choice = input("Choose: ").strip()
        print()

        if choice == "1":
            if state["gym_beaten"]:
                print("You already have the Prism Badge.")
                print()
            elif not state["tower_done"]:
                print("The gym is dark — no power. Lysara won't battle until")
                print("the lights are back. Deal with Prism Tower first.")
                print()
            else:
                result = gym(player, state)
                if result == "lose":
                    return "lose"

        elif choice == "2":
            pokecenter(player)

        elif choice == "3":
            boutique(player)

        elif choice == "4":
            tm_vendor(player)

        elif choice == "5":
            if not state["tower_done"]:
                result = prism_tower(player, state)
                if result == "lose":
                    return "lose"
            else:
                print("Prism Tower is quiet. The city's lights are steady again.")
                print()

        elif choice == "6":
            if not state["tower_done"]:
                print("S: We're not leaving a whole city in the dark. Tower first.")
                print()
            elif not state["gym_beaten"]:
                print("Lysara: *from the gym doorway* Leaving without facing me?")
                print("Lysara: Earn the Prism Badge first.")
                print()
            else:
                print("You leave Lumiose City heading east.")
                print()
                pause()
                return "done"

        else:
            print("Invalid choice.")
            print()
