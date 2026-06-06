import random
from battle import battle, calculate_damage, enemy_attack, give_exp, switch_pokemon, use_healing_item, HEALING_ITEMS
from pokemon import create_pokemon
from gym_leaders import gym_leaders
from sprites import show_battle_screen, hp_bar

WHITEOUT = gym_leaders[1]


def pause():
    input("(Press Enter to continue...)")
    print()


def double_battle(player, nico_party, enemy_party):
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
        show_battle_screen(player_mon, enemy_mon)
        if nico_mon["hp"] > 0:
            bar = hp_bar(nico_mon["hp"], nico_mon["max_hp"])
            print(f"  Nico's {nico_mon['name']} Lv.{nico_mon['level']}  {bar} {nico_mon['hp']}/{nico_mon['max_hp']}")
            print()

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

        if nico_mon["hp"] > 0 and enemy_mon["hp"] > 0:
            move_name = random.choice(nico_mon["moves"])
            damage, effectiveness = calculate_damage(nico_mon, move_name, enemy_mon)
            enemy_mon["hp"] = max(0, enemy_mon["hp"] - damage)
            print(f"  Nico's {nico_mon['name']} used {move_name}!")
            if effectiveness > 1:
                print("  It's super effective!")
            elif effectiveness < 1:
                print("  It's not very effective...")
            print(f"  {enemy_mon['name']} took {damage} damage. HP: {enemy_mon['hp']}/{enemy_mon['max_hp']}")
            print()

        if enemy_mon["hp"] <= 0:
            print(f"  {enemy_mon['name']} fainted!")
            give_exp(player_mon, enemy_mon, is_trainer=True)
            enemy_index += 1
            if enemy_index >= len(enemy_party):
                print("\nYou won!")
                return "win"
            enemy_mon = enemy_party[enemy_index]
            print(f"  {enemy_mon['name']} was sent out!")
            continue

        print()
        enemy_attack(enemy_mon, player_mon)
        print()

        if player_mon["hp"] <= 0:
            print(f"  {player_mon['name']} fainted!")
            next_mon = next((p for p in player["party"] if p["hp"] > 0), None)
            if next_mon is None:
                print("\nYou have no more Pokémon...")
                print("You blacked out.")
                return "lose"
            player_mon = next_mon
            print(f"Go, {player_mon['name']}!")

        if nico_mon["hp"] <= 0:
            print(f"  Nico's {nico_mon['name']} fainted!")
            nico_index += 1
            if nico_index < len(nico_party):
                nico_mon = nico_party[nico_index]
                print(f"  Nico sent out {nico_mon['name']}!")


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
    print("  GOLDENROD CITY")
    print("=" * 40)
    print()
    print("Goldenrod City is enormous — factories, broadcast")
    print("towers, crowds moving in every direction.")
    print("The whole city hums with electricity.")
    print()
    pause()

    print("At the centre of the city, one structure")
    print("dominates everything else.")
    print()
    pause()

    print("The Radio Tower.")
    print("It's absurdly tall — you can barely see the top.")
    print("And every floor is draped in pink Team Fairy flags.")
    print()
    pause()


def nico_reunite(player):
    print("A familiar voice from the crowd.")
    print()
    pause()

    print("Nico: I've been waiting for twenty minutes.")
    print()
    pause()

    print("NH: How did you even know I was coming today?")
    print()
    pause()

    print("Nico: I didn't. I've been here three days.")
    print()
    pause()

    print("NH: ...Three days.")
    print()
    pause()

    print("Nico: They won't let anyone near the tower.")
    print("Nico: Team Fairy took the whole thing. Every floor.")
    print("Nico: I've been waiting for someone worth going in with.")
    print()
    pause()

    print("NH: And nobody showed up for three days.")
    print()
    pause()

    print("Nico: You showed up.")
    print()
    pause()

    print("NH: Let's go.")
    print()
    pause()


def radio_tower(player):
    print("=" * 40)
    print("  GOLDENROD CITY RADIO TOWER")
    print("=" * 40)
    print()
    print("The lobby is empty — evacuated.")
    print("Pink banners hang from every railing.")
    print("Somewhere above, a broadcast crackles.")
    print()
    pause()

    nico_team = [create_pokemon("Gabite", 20), create_pokemon("Butterfree", 18)]

    # Floor 2
    print("Team Fairy Grunt: This tower is ours now. Turn back.")
    print()
    pause()

    print("NH: No.")
    print()
    pause()

    result = double_battle(
        player, nico_team,
        [create_pokemon("Clefairy", 18), create_pokemon("Snubbull", 18)]
    )
    if result == "lose":
        return "lose"

    print()
    print("Team Fairy Grunt: *into radio* Floor two is down.")
    print()
    pause()

    # Floor 4
    print("You push up to the fourth floor.")
    print("The view outside the windows is already unsettling —")
    print("you're higher than most of the city.")
    print()
    pause()

    print("Team Fairy Grunt: You actually made it up here?")
    print()
    pause()

    print("Nico: We actually made it up here.")
    print()
    pause()

    result = double_battle(
        player, nico_team,
        [create_pokemon("Clefable", 20), create_pokemon("Mimikyu", 19)]
    )
    if result == "lose":
        return "lose"

    print()
    print("Team Fairy Grunt: *stumbles back*")
    print("Team Fairy Grunt: How are they this strong...")
    print()
    pause()

    # Floor 7 - top
    print("The top floor.")
    print("The broadcast equipment fills the entire room —")
    print("screens, transmitters, a live signal going out.")
    print("At the centre, a woman in a long white coat.")
    print()
    pause()

    print("Clio: You've come a long way.")
    print("Clio: I'm almost impressed.")
    print()
    pause()

    print("NH: Turn it off.")
    print()
    pause()

    print("Clio: The broadcast? We're looking for someone.")
    print("Clio: Someone to lead us properly.")
    print("Clio: Larch was never enough.")
    print()
    pause()

    print("Nico: You built all of this just to run an ad?")
    print()
    pause()

    print("Clio: *smiles* Shut them down.")
    print()
    pause()

    result = double_battle(
        player, nico_team,
        [create_pokemon("Gardevoir", 23), create_pokemon("Sylveon", 22)]
    )
    if result == "lose":
        return "lose"

    print()
    print("Clio: *steps back*")
    print("Clio: ...")
    print("Clio: Fall back. All units, fall back.")
    print()
    pause()

    print("The broadcast cuts out.")
    print("The screens go dark.")
    print("Outside, the pink flags begin to come down.")
    print()
    pause()

    print("Nico: *looks at the blank screens*")
    print("Nico: That's it?")
    print()
    pause()

    print("NH: That's it.")
    print()
    pause()

    return "win"


def gym_battle(player):
    print()
    print("=" * 40)
    print("  GOLDENROD CITY GYM")
    print("=" * 40)
    print()
    print("The gym floor is wide open — a performance space.")
    print("Lights overhead. Bleachers on both sides.")
    print("Whiteout stands at the far end, arms crossed.")
    print()
    pause()

    print("Nico: *steps up beside you*")
    print("Nico: Might as well.")
    print()
    pause()

    print("NH: You're going to make this a habit.")
    print()
    pause()

    print("Nico: You say that like it's a bad thing.")
    print()
    pause()

    print(WHITEOUT["greeting"])
    print()
    pause()

    whiteout_team = [create_pokemon(name, level) for name, level in WHITEOUT["team"]]
    nico_team = [create_pokemon("Gabite", 22), create_pokemon("Butterfree", 20)]
    result = double_battle(player, nico_team, whiteout_team)
    if result == "lose":
        return "lose"

    print()
    print("Whiteout: *slow clap*")
    print("Whiteout: Now THAT was a show.")
    print("Whiteout: The Fog Badge is yours.")
    print()
    pause()

    player["money"] += WHITEOUT["reward"]
    player["badges"] = player.get("badges", [])
    player["badges"].append("Fog Badge")
    print("NH received the Fog Badge!")
    print(f"Whiteout gave you ${WHITEOUT['reward']}!")
    print()
    pause()

    return "win"


def goldenrod_city(player):
    arrive(player)
    nico_reunite(player)

    state = {"tower_done": False, "gym_beaten": False}

    while True:
        print("=" * 40)
        print("  GOLDENROD CITY")
        print("=" * 40)
        print()
        print("What do you want to do?")
        print("  1. Radio Tower")
        print("  2. Gym")
        print("  3. Pokémon Center")
        print("  4. Head north")
        print()
        choice = input("Choose: ").strip()
        print()

        if choice == "1":
            if state["tower_done"]:
                print("The tower is clear. The broadcast equipment")
                print("is dark. Nothing left to do here.")
                print()
            else:
                result = radio_tower(player)
                if result == "lose":
                    return "lose"
                state["tower_done"] = True

        elif choice == "2":
            if state["gym_beaten"]:
                print("You already have the Fog Badge.")
                print()
            else:
                result = gym_battle(player)
                if result == "lose":
                    return "lose"
                state["gym_beaten"] = True

        elif choice == "3":
            pokecenter(player)

        elif choice == "4":
            if not state["tower_done"]:
                print("Team Fairy still controls the Radio Tower.")
                print("You should deal with that first.")
                print()
            elif not state["gym_beaten"]:
                print("You haven't challenged the gym yet.")
                print()
            else:
                print("You leave Goldenrod City heading north.")
                print()
                pause()
                return "done"

        else:
            print("Invalid choice.")
            print()
