from pokemon import create_pokemon
from gym_leaders import gym_leaders
from battle import battle
from sprites import show_battle_screen, hp_bar

VANCE = gym_leaders[3]

MEGA_STONES = {
    "Frodger": "Frodgerite",
    "Buliz":   "Bulizite",
    "Falake":  "Falakeit",
}


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


def double_battle(player, partner_party, enemy_party, partner_name="Z"):
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


def zuma_arrival(player):
    print("=" * 40)
    print("  JUBILIFE CITY OUTSKIRTS")
    print("=" * 40)
    print()
    print("Before you can reach the city gates, someone")
    print("steps out from behind a column.")
    print()
    pause()

    print("Z: I've been waiting for you.")
    print()
    pause()

    print("NH: Who are you?")
    print()
    pause()

    print("Z: Z. I've been tracking Team Fairy's movements")
    print("Z: for the past six months. Jubilife's their next target.")
    print("Z: And you're the one Larch sent, aren't you.")
    print()
    pause()

    print("NH: Professor Larch didn't send me—")
    print()
    pause()

    print("Z: He's been watching you. So have I.")
    print("Z: You can't face what's coming without this.")
    print()
    pause()

    stone = MEGA_STONES.get(player.get("starter", ""), "a strange stone")
    print(f"Z: *holds out the {stone}*")
    print(f"Z: For your {player.get('starter', 'Pokémon')}. You'll know when to use it.")
    print()
    pause()

    player["bag"][stone] = player["bag"].get(stone, 0) + 1
    print(f"NH received the {stone}!")
    print()
    pause()

    print("Z: There's an airship docked at the northern platform.")
    print("Z: Team Fairy's. Your friend S is already planning something stupid.")
    print("Z: Go. I'll find you after.")
    print()
    pause()


def airship(player, state):
    print("=" * 40)
    print("  TEAM FAIRY AIRSHIP")
    print("=" * 40)
    print()
    print("The airship sits on the elevated platform,")
    print("pink and enormous. Team Fairy grunts patrol the gangway.")
    print()
    pause()

    print("S: *already halfway up the gangway*")
    print("S: Took you long enough.")
    print()
    pause()

    print("NH: We should have a plan.")
    print()
    pause()

    print("S: The plan is we go in and break everything.")
    print()
    pause()

    s_team = [create_pokemon("Charizard", 34), create_pokemon("Kingdra", 35)]

    # Deck fight
    print("Team Fairy Grunt: No entry — this airship is—")
    print()
    pause()

    print("S: Yeah. *sends out Charizard*")
    print()
    pause()

    result = double_battle(
        player, s_team,
        [create_pokemon("Snubbull", 31), create_pokemon("Clefairy", 30)],
        partner_name="S"
    )
    if result == "lose":
        return "lose"

    print()
    print("Inside. The corridors are wide and painted pink.")
    print("Crates labelled with coordinates NH doesn't recognise.")
    print()
    pause()

    print("Team Fairy Grunt: You're outnumbered. Stand down.")
    print()
    pause()

    result = double_battle(
        player, s_team,
        [create_pokemon("Granbull", 32), create_pokemon("Sylveon", 33)],
        partner_name="S"
    )
    if result == "lose":
        return "lose"

    print()
    print("S: *reads a shipping label*")
    print("S: These are Pokémon containment units. Industrial ones.")
    print()
    pause()

    print("NH: For what?")
    print()
    pause()

    print("S: Something big enough to need thirty of them.")
    print()
    pause()

    # Bridge
    print("The door to the bridge slides open.")
    print()
    pause()

    print("Team Fairy Admin Verona: You two are impressively foolish.")
    print()
    pause()

    print("S: We get that a lot.")
    print()
    pause()

    result = double_battle(
        player, s_team,
        [create_pokemon("Togekiss", 34), create_pokemon("Gardevoir", 35), create_pokemon("Sylveon", 33)],
        partner_name="S"
    )
    if result == "lose":
        return "lose"

    print()
    print("Team Fairy Admin Verona: *steps back*")
    print("Team Fairy Admin Verona: It doesn't matter.")
    print("Team Fairy Admin Verona: They're already here.")
    print()
    pause()

    print("The airship shudders. From the windows:")
    print("three more airships rising from the south.")
    print()
    pause()

    print("S: NH. We need to go. Now.")
    print()
    pause()

    print("You run. The gangway. The platform.")
    print("Below, on the street, the city is in chaos.")
    print()
    pause()

    print("NR: *out of breath, running toward you*")
    print("NR: There's a hundred of them — they came from—")
    print()
    pause()

    print("Team Fairy Grunts block all four exits.")
    print()
    pause()

    print("S: *looks at NR* How many can we take?")
    print()
    pause()

    print("NR: Not this many.")
    print()
    pause()

    print("NH: *steps forward*")
    print()
    pause()

    print("Team Fairy Commander: Stand down.")
    print("Team Fairy Commander: The two older ones come with us.")
    print("Team Fairy Commander: The kid goes free. Good optics.")
    print()
    pause()

    print("S: NH — ")
    print()
    pause()

    print("NR: Go. Find Z. She'll know what to do.")
    print()
    pause()

    print("Team Fairy Grunts take S and NR.")
    print("The three airships move north.")
    print("You're alone on the platform.")
    print()
    pause()

    state["airship_done"] = True
    return "done"


def dungeon(player, state):
    print("=" * 40)
    print("  TEAM FAIRY DUNGEON")
    print("=" * 40)
    print()
    print("Z is waiting at the northern gate.")
    print()
    pause()

    print("Z: I saw what happened. I know where they've taken them.")
    print("Z: Old fort outside the city. Team Fairy converted it.")
    print()
    pause()

    print("NH: Can we get in?")
    print()
    pause()

    print("Z: *shows a rough map* There's a service entrance.")
    print("Z: I'll take point. You cover me.")
    print()
    pause()

    z_team = [create_pokemon("Dramimic", 36)]

    # Entrance
    print("The fort is cold. Stone corridors lit by pink strip-lights.")
    print()
    pause()

    print("Team Fairy Guard: Halt — this is a restricted facility—")
    print()
    pause()

    print("Z: *Dramimic materialises beside her*")
    print()
    pause()

    result = double_battle(
        player, z_team,
        [create_pokemon("Clefairy", 33), create_pokemon("Snubbull", 32)],
        partner_name="Z"
    )
    if result == "lose":
        return "lose"

    print()
    print("Z: *checks her map* Cells are lower level.")
    print()
    pause()

    # Lower level
    print("Stairs down. The lighting gets worse.")
    print()
    pause()

    print("Team Fairy Guard: How did you get past—")
    print()
    pause()

    result = double_battle(
        player, z_team,
        [create_pokemon("Granbull", 34), create_pokemon("Sylveon", 35)],
        partner_name="Z"
    )
    if result == "lose":
        return "lose"

    print()
    print("A row of cells. Two of them occupied.")
    print()
    pause()

    print("S: *from behind bars* NH.")
    print("S: About time.")
    print()
    pause()

    print("NR: *next to S* How did you find us?")
    print()
    pause()

    print("Z: *breaks the lock* Questions later.")
    print()
    pause()

    print("You free them both.")
    print()
    pause()

    print("NR: There's something else here. Down the south corridor.")
    print("NR: They were moving a containment unit when we arrived.")
    print()
    pause()

    print("Z: Then we go south.")
    print()
    pause()

    print("NR: NH — whatever's in that unit...")
    print("NR: It's not small.")
    print()
    pause()

    # Boss fight
    print("The south corridor opens into a vaulted chamber.")
    print("A single containment unit in the centre, sealed.")
    print()
    pause()

    print("Team Fairy General Aldric: You shouldn't be down here.")
    print("Team Fairy General Aldric: None of you should.")
    print()
    pause()

    print("Z: What are you keeping in that unit?")
    print()
    pause()

    print("Team Fairy General Aldric: Insurance.")
    print("Team Fairy General Aldric: Now. Get out of my city.")
    print()
    pause()

    input("(Press Enter to battle Aldric...)")
    print()

    result = battle(
        player,
        [
            create_pokemon("Togekiss", 37),
            create_pokemon("Gardevoir", 38),
            create_pokemon("Sylveon", 36),
            create_pokemon("Granbull", 35),
        ],
        is_wild=False
    )
    if result == "lose":
        return "lose"

    print()
    print("Team Fairy General Aldric: *grips the containment unit*")
    print("Team Fairy General Aldric: You've bought yourselves a delay.")
    print("Team Fairy General Aldric: Nothing more.")
    print()
    pause()

    print("Aldric activates a smoke screen and disappears.")
    print("The containment unit is left behind — sealed, silent.")
    print()
    pause()

    print("Z: We need to move before reinforcements arrive.")
    print()
    pause()

    print("You get out. All four of you.")
    print()
    pause()

    print("NR: *outside, catching his breath*")
    print("NR: What was in that unit?")
    print()
    pause()

    print("Z: I don't know.")
    print("Z: But they didn't want us to see it.")
    print()
    pause()

    print("S: *looks at the sealed city*")
    print("S: Vance will know what to do. He's held this city before.")
    print()
    pause()

    state["dungeon_done"] = True
    return "done"


def jubilife_city(player):
    print("=" * 40)
    print("  JUBILIFE CITY")
    print("=" * 40)
    print()
    print("Jubilife City. Tall walls, older than any other city")
    print("in Draconia. The kind of place that has been fought over.")
    print()
    pause()

    state = {"airship_done": False, "dungeon_done": False, "gym_beaten": False}

    # Z arrival scene plays once on entry
    zuma_arrival(player)

    while True:
        print("=" * 40)
        print("  JUBILIFE CITY")
        print("=" * 40)
        print()
        print("What do you want to do?")
        print("  1. Gym")
        print("  2. Pokémon Center")
        if not state["airship_done"]:
            print("  3. Northern Platform — Team Fairy Airship")
        elif not state["dungeon_done"]:
            print("  3. Northern Gate — Rescue NR and S")
        else:
            print("  3. (Nothing to do here)")
        print("  4. Head north")
        print()
        choice = input("Choose: ").strip()
        print()

        if choice == "1":
            if state["gym_beaten"]:
                print("You already have the Iron Badge.")
                print()
            else:
                if not state["dungeon_done"]:
                    print("Vance: *at the door*")
                    print("Vance: Gym's closed. City's under threat.")
                    print("Vance: Come back when the streets are safe.")
                    print()
                else:
                    print("=" * 40)
                    print("  JUBILIFE CITY GYM")
                    print("=" * 40)
                    print()
                    print("The gym floor is stone. Military banners, not trophies.")
                    print()
                    pause()
                    print(VANCE["greeting"])
                    print()
                    input("(Press Enter to battle...)")
                    print()
                    team = [create_pokemon(name, level) for name, level in VANCE["team"]]
                    result = battle(player, team, is_wild=False)
                    if result == "lose":
                        return "lose"
                    print()
                    print("Vance: That's a fighter's instinct.")
                    print("Vance: Take the Iron Badge. You've earned a place in this war.")
                    print()
                    player["money"] += VANCE["reward"]
                    print("NH received the Iron Badge!")
                    print(f"Vance gave you ${VANCE['reward']}!")
                    print()
                    pause()
                    state["gym_beaten"] = True

        elif choice == "2":
            pokecenter(player)

        elif choice == "3":
            if not state["airship_done"]:
                result = airship(player, state)
                if result == "lose":
                    return "lose"
            elif not state["dungeon_done"]:
                result = dungeon(player, state)
                if result == "lose":
                    return "lose"
            else:
                print("You've already handled what needed handling here.")
                print()

        elif choice == "4":
            if not state["dungeon_done"]:
                print("You can't leave yet — NR and S are still being held.")
                print()
            elif not state["gym_beaten"]:
                print("Vance: Challenge the gym before you move on.")
                print("Vance: The north road is no place for someone without a badge.")
                print()
            else:
                print("You leave Jubilife City heading north.")
                print()
                pause()
                return "done"

        else:
            print("Invalid choice.")
            print()
