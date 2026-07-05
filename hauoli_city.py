from pokemon import create_pokemon
from gym_leaders import gym_leaders
from battle import battle
from sprites import show_battle_screen, hp_bar, get_sprite
from sky_buggy import sky_buggy, destinations_before

TIDE = gym_leaders[6]


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


def market(player):
    print()
    print("=" * 40)
    print("  HAU'OLI BEACH MARKET")
    print("=" * 40)
    print()

    items = [
        ("Hyper Potion", 1200),
        ("Max Potion",   2500),
        ("Full Restore", 3000),
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
    print("  HAU'OLI TM STAND")
    print("=" * 40)
    print()

    tms = [
        ("Moonblast",     "Fairy",  3000),
        ("Dazzling Gleam", "Fairy", 2500),
        ("Sludge Bomb",   "Poison", 2500),
        ("Dragon Pulse",  "Dragon", 2500),
        ("Draco Meteor",  "Dragon", 3500),
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


def fairy_lab(player, state):
    print("=" * 40)
    print("  HAU'OLI BEACH — THE OLD CANNERY")
    print("=" * 40)
    print()
    print("Past the marina, where the beach turns to black rock, there's")
    print("a shuttered fish cannery. Everyone in Hau'oli says it's empty.")
    print("Everyone in Hau'oli is wrong. A pink glow leaks under its door,")
    print("and the whole building hums like a hornet's nest.")
    print()
    pause()

    print("A little Rattata bolts out of a gap in the wall and freezes")
    print("at your feet. Its fur has gone the wrong colour — washed-out,")
    print("faintly luminous. It shivers and runs for the sea.")
    print()
    pause()

    print("NH: ...That is NOT what a Rattata is supposed to look like.")
    print("NH: Okay. I'm going in.")
    print()
    pause()

    # --- Front room: grunt with test-subject Rattatas ---
    print("Inside: rows of glass tanks, each one holding a Rattata bathed")
    print("in pink light. A grunt looks up from a clipboard, annoyed.")
    print()
    print("Team Fairy Grunt: Staff only. This is a licensed research site.")
    print("Team Fairy Grunt: ...Fine. The hard way, then.")
    print()
    input("(Press Enter to battle...)")
    print()

    result = battle(
        player,
        [create_pokemon("Rattata", 58), create_pokemon("Rattata", 58), create_pokemon("Granbull", 60)],
        is_wild=False
    )
    if result == "lose":
        return "lose"

    print()
    print("Team Fairy Grunt: You don't understand what we're building here.")
    print()
    pause()

    # --- Lab floor: the scientist ---
    print("Deeper in, the tanks give way to one enormous cracked cylinder")
    print("at the centre of the floor. A scientist stands over the controls,")
    print("not even turning around.")
    print()
    print("Team Fairy Scientist: The Senate wanted a Fairy strong enough to")
    print("Team Fairy Scientist: end a Dragon. Rattata breed fast, so we had")
    print("Team Fairy Scientist: material to spare. Say hello to the result.")
    print()
    input("(Press Enter to battle...)")
    print()

    result = battle(
        player,
        [create_pokemon("Clefable", 60), create_pokemon("Sylveon", 61), create_pokemon("Mimikyu", 62)],
        is_wild=False
    )
    if result == "lose":
        return "lose"

    print()
    print("Team Fairy Scientist: *stepping back from the controls* Doesn't")
    print("Team Fairy Scientist: matter. It's already awake. It was always")
    print("Team Fairy Scientist: going to get loose eventually. Better you than me.")
    print()
    pause()

    # --- The boss: Ratichacha ---
    print("The great cylinder splits down its crack. Pink light floods the")
    print("room, and something climbs out on too many legs — a Rattata")
    print("stretched into a nightmare, whiskers like wires, eyes like lamps.")
    print()
    for line in get_sprite("Ratichacha"):
        print("      " + line)
    print()
    print("RATICHACHA: kii... kii-CHA!")
    print()
    input("(Press Enter to battle Ratichacha...)")
    print()

    result = battle(
        player,
        [create_pokemon("Ratichacha", 64)],
        is_wild=False
    )
    if result == "lose":
        return "lose"

    print()
    print("Ratichacha crashes back into the wreck of its tank and goes still,")
    print("the glow fading out of it. Its fur settles back to ordinary brown.")
    print("Just a very large, very tired Rattata now.")
    print()
    pause()

    print("The scientist is long gone. On the abandoned console, one file")
    print("is still open: a Senate authorisation, same seal as Castelia,")
    print("same routing as the Lumiose power theft. All pointing south.")
    print()
    pause()

    print("NH: South again. Whatever they're really building, it's not here.")
    print("NH: But it's not going to be a Rattata next time.")
    print()
    pause()

    state["lab_done"] = True
    return "done"


def gym(player, state):
    print("=" * 40)
    print("  HAU'OLI CITY GYM")
    print("=" * 40)
    print()
    print("The gym has no roof — just a wind-scoured deck on the cliffs")
    print("above the marina, ringed with wind socks snapping in the gale.")
    print()
    pause()

    print("Gym Trainer Kai: Tide runs the whole coast on feel. No plan.")
    print("Gym Trainer Kai: Beat me first — the wind up here eats beginners.")
    print()
    input("(Press Enter to battle...)")
    print()

    result = battle(
        player,
        [create_pokemon("Altaria", 58), create_pokemon("Noivern", 59)],
        is_wild=False
    )
    if result == "lose":
        return "lose"

    print()
    print("Kai: Ha! Alright. She's out on the far edge. Go on.")
    print()
    pause()

    print("Tide is standing right at the lip of the cliff, barefoot,")
    print("watching the sea. She doesn't turn around until you're close.")
    print()
    print(TIDE["greeting"])
    print()
    input("(Press Enter to battle Tide...)")
    print()

    team = [create_pokemon(name, level) for name, level in TIDE["team"]]
    result = battle(player, team, is_wild=False)
    if result == "lose":
        return "lose"

    print()
    print("Tide: *grinning, hair everywhere* Oh, that was GOOD. You read the")
    print("Tide: wind better than half my trainers. Here — you earned it.")
    print()
    pause()

    player["money"] += TIDE["reward"]
    print("NH received the Gale Badge!")
    print(f"Tide gave you ${TIDE['reward']}!")
    print()
    pause()

    state["gym_beaten"] = True
    return "done"


def hauoli_city(player):
    print("=" * 40)
    print("  HAU'OLI CITY")
    print("=" * 40)
    print()
    print("Hau'oli City spills down to the sea in white terraces — a")
    print("harbour town of markets, surf, and sun. After the dark of")
    print("Lumiose, the light off the water is almost too much.")
    print()
    pause()

    state = {"lab_done": False, "gym_beaten": False}

    while True:
        print("=" * 40)
        print("  HAU'OLI CITY")
        print("=" * 40)
        print()
        print("What do you want to do?")
        print("  1. Gym")
        print("  2. Pokémon Center")
        print("  3. Beach Market")
        print("  4. TM Stand")
        if not state["lab_done"]:
            print("  5. The old cannery — Team Fairy")
        else:
            print("  5. (Cannery shut down)")
        print("  6. Sky Buggy")
        print("  7. Head north to Hammerlocke")
        print()
        choice = input("Choose: ").strip()
        print()

        if choice == "1":
            if state["gym_beaten"]:
                print("You already have the Gale Badge.")
                print()
            else:
                result = gym(player, state)
                if result == "lose":
                    return "lose"

        elif choice == "2":
            pokecenter(player)

        elif choice == "3":
            market(player)

        elif choice == "4":
            tm_vendor(player)

        elif choice == "5":
            if not state["lab_done"]:
                result = fairy_lab(player, state)
                if result == "lose":
                    return "lose"
            else:
                print("The cannery is dark and quiet. The tanks are empty now.")
                print()

        elif choice == "6":
            result = sky_buggy(player, destinations_before("Hau'oli City"))
            if result == "lose":
                return "lose"
            if result is not None:
                return result

        elif choice == "7":
            if not state["lab_done"]:
                print("You can't just leave with that cannery still humming.")
                print("Whatever Team Fairy is doing in there, it comes first.")
                print()
            elif not state["gym_beaten"]:
                print("Tide: *calling down from the cliff* Leaving already?")
                print("Tide: Not before you've had a crack at me. Gale Badge first!")
                print()
            else:
                print("You leave Hau'oli City, following the coast road north")
                print("toward the walls of Hammerlocke.")
                print()
                pause()
                return "done"

        else:
            print("Invalid choice.")
            print()
