from pokemon import create_pokemon
from gym_leaders import gym_leaders
from battle import battle
from sprites import show_battle_screen, hp_bar

ROOK = gym_leaders[4]


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


def street_shop(player):
    print()
    print("=" * 40)
    print("  STREET STALL")
    print("=" * 40)
    print()

    items = [
        ("Hyper Potion", 1200),
        ("Max Potion",   2500),
        ("Ultra Ball",   1200),
        ("Revive",       1500),
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
    print("  BACK-ALLEY TM DEALER")
    print("=" * 40)
    print()

    tms = [
        ("Night Slash", "Dark",     2000),
        ("Dark Pulse",  "Dark",     2500),
        ("Brick Break", "Fighting", 2000),
        ("Energy Ball", "Grass",    2000),
        ("Dragon Pulse","Dragon",   2500),
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


def double_battle(player, partner_party, enemy_party, partner_name="I"):
    from battle import calculate_damage, enemy_attack, give_exp, switch_pokemon, use_healing_item
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

        if partner_mon["hp"] > 0:
            partner_move = partner_mon["moves"][0] if partner_mon["moves"] else None
            if partner_move:
                dmg, eff = calculate_damage(partner_mon, partner_move, enemy_mon)
                enemy_mon["hp"] = max(0, enemy_mon["hp"] - dmg)
                print(f"{partner_name}'s {partner_mon['name']} used {partner_move}!")
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

        if partner_mon["hp"] <= 0:
            partner_index += 1
            if partner_index < len(partner_party):
                partner_mon = partner_party[partner_index]
                print(f"{partner_name} sent out {partner_mon['name']}!")
                print()


def convoy(player, state):
    print("=" * 40)
    print("  SOUTH DISTRICT — TEAM FAIRY CONVOY")
    print("=" * 40)
    print()
    print("The south district is gridlocked.")
    print("Three armoured cars, pink tarps draped over the cargo,")
    print("Team Fairy grunts on foot alongside each one.")
    print()
    pause()

    print("I: *steps out from a doorway*")
    print("I: They've been running these convoys all morning.")
    print("I: Whatever they're moving — they don't want anyone to see it.")
    print()
    pause()

    print("NH: *spots a length of steel pipe lying on the kerb*")
    print()
    pause()

    print("NH: *picks it up*")
    print()
    pause()

    print("I: ...What are you doing?")
    print()
    pause()

    print("NH: Watch.")
    print()
    pause()

    # --- CAR ONE ---
    print("Team Fairy Grunt: Get away from the convoy. Now.")
    print()
    input("(Press Enter to battle...)")
    print()

    result = battle(
        player,
        [create_pokemon("Houndour", 42), create_pokemon("Snubbull", 41)],
        is_wild=False
    )
    if result == "lose":
        return "lose"

    print()
    print("NH sets the pipe under the car's rear axle.")
    print()
    pause()

    print("NH: I.")
    print()
    pause()

    print("I: ...Yeah?")
    print()
    pause()

    print("NH: Push.")
    print()
    pause()

    print("The car tips.")
    print("It tips further.")
    print("And then it goes over with a sound like a small earthquake.")
    print()
    pause()

    print("I: *stares at it*")
    print("I: You just...")
    print()
    pause()

    print("NH: Two more.")
    print()
    pause()

    # --- CAR TWO ---
    print("Team Fairy Grunt: There are TWO of them—")
    print("Team Fairy Grunt 2: Take them both out!")
    print()
    input("(Press Enter to battle...)")
    print()

    i_team = [create_pokemon("Dragapult", 45), create_pokemon("Weavile", 43)]

    result = double_battle(
        player, i_team,
        [create_pokemon("Granbull", 43), create_pokemon("Sylveon", 44)],
        partner_name="I"
    )
    if result == "lose":
        return "lose"

    print()
    print("NH and I find their angle on the second car.")
    print("It goes over faster — they're getting better at this.")
    print()
    pause()

    # --- CAR THREE ---
    print("Team Fairy Commander: *steps out of the last car*")
    print("Team Fairy Commander: I will not let you flip this one.")
    print()
    pause()

    print("NH: *looks at I*")
    print()
    pause()

    print("I: I've got the pipe.")
    print()
    input("(Press Enter to battle...)")
    print()

    result = battle(
        player,
        [
            create_pokemon("Togekiss",  46),
            create_pokemon("Gardevoir", 45),
            create_pokemon("Mimikyu",   44),
        ],
        is_wild=False
    )
    if result == "lose":
        return "lose"

    print()
    print("The last car goes over.")
    print("The crate inside hits the asphalt and splits open.")
    print()
    pause()

    print("Something hard and pink rolls across the street.")
    print()
    pause()

    print("NH: *picks it up*")
    print("NH: What is this?")
    print()
    pause()

    print("I: *pulling papers from the car floor*")
    print("I: NH.")
    print()
    pause()

    print("I: Look at this seal.")
    print()
    pause()

    print("NH: *looks at the papers*")
    print()
    pause()

    print("I: That's the Senate's seal.")
    print()
    pause()

    print("NH: The Senate.")
    print()
    pause()

    print("I: These weren't Team Fairy's cars.")
    print("I: These were government vehicles.")
    print("I: The Senate has been running this.")
    print()
    pause()

    player["bag"]["Diancie Fragment"] = player["bag"].get("Diancie Fragment", 0) + 1
    print("NH received a Diancie Fragment!")
    print()
    pause()

    print("Neither of them says anything for a moment.")
    print()
    pause()

    print("I: We need to keep moving.")
    print()
    pause()

    print("Then, from above:")
    print()
    pause()

    print("Rook: *leans out of a window forty floors up*")
    print("Rook: Huh.")
    print()
    pause()

    print("Rook: Didn't think you'd actually flip those.")
    print()
    pause()

    print("Rook: Gym's open. Come find the top floor.")
    print()
    pause()

    state["convoy_done"] = True
    return "done"


def gym(player, state):
    print("=" * 40)
    print("  CASTELIA CITY GYM")
    print("=" * 40)
    print()
    print("The lobby of Castelia Tower.")
    print("Steel walls, no trophies — just an elevator and a sign:")
    print("ROOK — TOP FLOOR.")
    print()
    pause()

    # Floor 10 trainer
    print("Floor 10.")
    print()
    pause()

    print("Gym Trainer Mel: You want the top? You fight through every floor.")
    print()
    input("(Press Enter to battle...)")
    print()

    result = battle(
        player,
        [create_pokemon("Houndour", 43), create_pokemon("Krokorok", 44)],
        is_wild=False
    )
    if result == "lose":
        return "lose"

    print()
    print("Mel: Keep going.")
    print()
    pause()

    # Floor 25 trainer
    print("Floor 25.")
    print()
    pause()

    print("Gym Trainer Jay: Rook doesn't let people up unless they're worth his time.")
    print("Gym Trainer Jay: Prove you're worth it.")
    print()
    input("(Press Enter to battle...)")
    print()

    result = battle(
        player,
        [create_pokemon("Sneasel", 45), create_pokemon("Zoroark", 46)],
        is_wild=False
    )
    if result == "lose":
        return "lose"

    print()
    print("Jay: Top floor. Go.")
    print()
    pause()

    # Rook — top floor
    print("The elevator opens at the top.")
    print("Floor-to-ceiling windows. The whole city below.")
    print()
    pause()

    print("Rook: *leaning on the window ledge, not looking at you*")
    print("Rook: You made it. Not everyone does.")
    print()
    pause()

    print("Rook: I run this gym because this city needs someone who actually knows")
    print("Rook: how to fight. Not performed fights. Real ones.")
    print("Rook: *turns around*")
    print("Rook: Let's see if you've been in any.")
    print()
    input("(Press Enter to battle Rook...)")
    print()

    team = [create_pokemon(name, level) for name, level in ROOK["team"]]
    result = battle(player, team, is_wild=False)
    if result == "lose":
        return "lose"

    print()
    print("Rook: *nods*")
    print("Rook: Not bad. You fight like you've got something to prove.")
    print("Rook: Good. Means you'll keep going.")
    print()
    pause()

    player["money"] += ROOK["reward"]
    print("NH received the Shadow Badge!")
    print(f"Rook gave you ${ROOK['reward']}!")
    print()
    pause()

    state["gym_beaten"] = True
    return "done"


def castelia_city(player):
    print("=" * 40)
    print("  CASTELIA CITY")
    print("=" * 40)
    print()
    print("Castelia City. Towers of glass stacked so high they vanish into the haze.")
    print("The kind of place that never quiets down.")
    print()
    pause()

    state = {"convoy_done": False, "gym_beaten": False}

    while True:
        print("=" * 40)
        print("  CASTELIA CITY")
        print("=" * 40)
        print()
        print("What do you want to do?")
        print("  1. Gym")
        print("  2. Pokémon Center")
        print("  3. Street Stall")
        print("  4. TM Dealer")
        if not state["convoy_done"]:
            print("  5. South District — Team Fairy Convoy")
        else:
            print("  5. (Convoy cleared)")
        print("  6. Head east")
        print()
        choice = input("Choose: ").strip()
        print()

        if choice == "1":
            if state["gym_beaten"]:
                print("You already have the Shadow Badge.")
                print()
            elif not state["convoy_done"]:
                print("Rook: *from somewhere above*")
                print("Rook: Handle the south district first.")
                print("Rook: Then we'll talk.")
                print()
            else:
                result = gym(player, state)
                if result == "lose":
                    return "lose"

        elif choice == "2":
            pokecenter(player)

        elif choice == "3":
            street_shop(player)

        elif choice == "4":
            tm_vendor(player)

        elif choice == "5":
            if not state["convoy_done"]:
                result = convoy(player, state)
                if result == "lose":
                    return "lose"
            else:
                print("The south district is clear.")
                print()

        elif choice == "6":
            if not state["convoy_done"]:
                print("I: We can't leave while Team Fairy is running convoys through the city.")
                print()
            elif not state["gym_beaten"]:
                print("Rook: *from above*")
                print("Rook: You cleared the streets. Now clear my gym.")
                print("Rook: Then you can go.")
                print()
            else:
                print("You leave Castelia City heading east.")
                print()
                pause()
                return "done"

        else:
            print("Invalid choice.")
            print()
