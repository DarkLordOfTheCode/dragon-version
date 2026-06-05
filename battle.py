import random
from moves import moves as move_data
from pokemon import level_up

type_chart = {
    "Normal":   {"Rock": 0.5, "Steel": 0.5, "Ghost": 0},
    "Fire":     {"Fire": 0.5, "Water": 0.5, "Rock": 0.5, "Dragon": 0.5,
                 "Grass": 2, "Ice": 2, "Bug": 2, "Steel": 2},
    "Water":    {"Water": 0.5, "Grass": 0.5, "Dragon": 0.5,
                 "Fire": 2, "Ground": 2, "Rock": 2},
    "Grass":    {"Fire": 0.5, "Grass": 0.5, "Poison": 0.5, "Flying": 0.5,
                 "Bug": 0.5, "Dragon": 0.5, "Steel": 0.5,
                 "Water": 2, "Ground": 2, "Rock": 2},
    "Electric": {"Electric": 0.5, "Grass": 0.5, "Dragon": 0.5, "Ground": 0,
                 "Water": 2, "Flying": 2},
    "Ice":      {"Fire": 0.5, "Water": 0.5, "Ice": 0.5, "Steel": 0.5,
                 "Grass": 2, "Ground": 2, "Flying": 2, "Dragon": 2},
    "Fighting": {"Poison": 0.5, "Flying": 0.5, "Psychic": 0.5, "Bug": 0.5,
                 "Fairy": 0.5, "Ghost": 0,
                 "Normal": 2, "Ice": 2, "Rock": 2, "Dark": 2, "Steel": 2},
    "Poison":   {"Poison": 0.5, "Ground": 0.5, "Rock": 0.5, "Ghost": 0.5,
                 "Steel": 0,
                 "Grass": 2, "Fairy": 2},
    "Ground":   {"Grass": 0.5, "Bug": 0.5, "Flying": 0,
                 "Fire": 2, "Electric": 2, "Poison": 2, "Rock": 2, "Steel": 2},
    "Flying":   {"Electric": 0.5, "Rock": 0.5, "Steel": 0.5,
                 "Grass": 2, "Fighting": 2, "Bug": 2},
    "Psychic":  {"Psychic": 0.5, "Steel": 0.5, "Dark": 0,
                 "Fighting": 2, "Poison": 2},
    "Bug":      {"Fire": 0.5, "Fighting": 0.5, "Flying": 0.5, "Ghost": 0.5,
                 "Steel": 0.5, "Fairy": 0.5,
                 "Grass": 2, "Psychic": 2, "Dark": 2},
    "Rock":     {"Fighting": 0.5, "Ground": 0.5, "Steel": 0.5,
                 "Fire": 2, "Ice": 2, "Flying": 2, "Bug": 2},
    "Ghost":    {"Normal": 0, "Dark": 0.5,
                 "Psychic": 2, "Ghost": 2},
    "Dragon":   {"Steel": 0.5, "Fairy": 0,
                 "Dragon": 2},
    "Dark":     {"Fighting": 0.5, "Dark": 0.5, "Fairy": 0.5,
                 "Psychic": 2, "Ghost": 2},
    "Steel":    {"Fire": 0.5, "Water": 0.5, "Electric": 0.5, "Steel": 0.5,
                 "Ice": 2, "Rock": 2, "Fairy": 2},
    "Fairy":    {"Fire": 0.5, "Poison": 0.5, "Steel": 0.5,
                 "Fighting": 2, "Dragon": 2, "Dark": 2},
}


def get_effectiveness(move_type, defender_types):
    multiplier = 1.0
    for def_type in defender_types:
        multiplier *= type_chart.get(move_type, {}).get(def_type, 1.0)
    return multiplier


def calculate_damage(attacker, move_name, defender):
    move = move_data[move_name]
    power = move["power"]
    if move["category"] == "physical":
        atk = attacker["attack"]
        def_ = defender["defence"]
    else:
        atk = attacker["special"]
        def_ = defender["special"]
    level = attacker["level"]
    damage = int(((2 * level / 5 + 2) * power * atk / def_ / 50) + 2)
    effectiveness = get_effectiveness(move["type"], defender["types"])
    damage = int(damage * effectiveness * random.uniform(0.85, 1.0))
    return max(1, damage), effectiveness


def show_status(player_mon, enemy_mon):
    print(f"  {enemy_mon['name']} Lv.{enemy_mon['level']}   HP: {enemy_mon['hp']}/{enemy_mon['max_hp']}")
    print()
    print(f"  {player_mon['name']} Lv.{player_mon['level']}   HP: {player_mon['hp']}/{player_mon['max_hp']}")
    print("-" * 40)


def use_potion(player, player_mon):
    potions = player["bag"].get("Potion", 0)
    if potions == 0:
        print("You have no Potions!")
        return False
    heal = min(20, player_mon["max_hp"] - player_mon["hp"])
    if heal == 0:
        print(f"{player_mon['name']}'s HP is already full!")
        return False
    player_mon["hp"] += heal
    player["bag"]["Potion"] -= 1
    print(f"{player_mon['name']} recovered {heal} HP!")
    return True


def switch_pokemon(player, current_mon):
    available = [(i, p) for i, p in enumerate(player["party"])
                 if p is not current_mon and p["hp"] > 0]
    if not available:
        print("No other Pokémon to switch to!")
        return current_mon
    print("Choose a Pokémon:")
    for i, (_, p) in enumerate(available):
        print(f"  {i + 1}. {p['name']} Lv.{p['level']}  HP: {p['hp']}/{p['max_hp']}")
    choice = input("Enter number: ").strip()
    try:
        _, chosen = available[int(choice) - 1]
        print(f"Go, {chosen['name']}!")
        return chosen
    except (ValueError, IndexError):
        print("Invalid choice.")
        return current_mon


def try_catch(player, enemy_mon):
    balls = player["bag"].get("Poké Ball", 0)
    if balls == 0:
        print("You have no Poké Balls!")
        return False
    hp_ratio = enemy_mon["hp"] / enemy_mon["max_hp"]
    catch_chance = 0.3 + 0.5 * (1 - hp_ratio)
    player["bag"]["Poké Ball"] -= 1
    print("You threw a Poké Ball!")
    if random.random() < catch_chance:
        print(f"Gotcha! {enemy_mon['name']} was caught!")
        player["party"].append(enemy_mon)
        return True
    else:
        print(f"{enemy_mon['name']} broke free!")
        return False


def give_exp(player_mon, enemy_mon, is_trainer):
    exp_gain = enemy_mon["level"] * (9 if is_trainer else 6)
    player_mon["exp"] += exp_gain
    print(f"  {player_mon['name']} gained {exp_gain} EXP!")
    while player_mon["exp"] >= player_mon["exp_to_next"]:
        player_mon["exp"] -= player_mon["exp_to_next"]
        level_up(player_mon)
        print(f"  {player_mon['name']} grew to level {player_mon['level']}!")


def enemy_attack(enemy_mon, player_mon):
    move_name = random.choice(enemy_mon["moves"])
    damage, effectiveness = calculate_damage(enemy_mon, move_name, player_mon)
    player_mon["hp"] = max(0, player_mon["hp"] - damage)
    print(f"  {enemy_mon['name']} used {move_name}!")
    if effectiveness == 0:
        print("  It had no effect...")
    elif effectiveness > 1:
        print("  It's super effective!")
    elif effectiveness < 1:
        print("  It's not very effective...")
    print(f"  {player_mon['name']} took {damage} damage. HP: {player_mon['hp']}/{player_mon['max_hp']}")


def battle(player, enemy_party, is_wild=False):
    enemy_index = 0
    enemy_mon = enemy_party[enemy_index]

    if is_wild:
        print(f"\nA wild {enemy_mon['name']} appeared!")
    else:
        print(f"\n{enemy_mon['name']} was sent out!")

    player_mon = next(p for p in player["party"] if p["hp"] > 0)
    print(f"Go, {player_mon['name']}!")
    print()

    while True:
        show_status(player_mon, enemy_mon)

        print("What will you do?")
        print("  1. Fight")
        print("  2. Bag")
        print("  3. Pokémon")
        print("  4. Run")
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
            if is_wild:
                print("  1. Potion")
                print("  2. Poké Ball")
                bag_choice = input("Choose: ").strip()
                if bag_choice == "1":
                    used_turn = use_potion(player, player_mon)
                elif bag_choice == "2":
                    caught = try_catch(player, enemy_mon)
                    if caught:
                        return "catch"
                    used_turn = True
            else:
                used_turn = use_potion(player, player_mon)

        elif action == "3":
            new_mon = switch_pokemon(player, player_mon)
            if new_mon is not player_mon:
                player_mon = new_mon
                used_turn = True

        elif action == "4":
            print("You ran away!")
            return "run"

        else:
            print("Invalid choice.")
            continue

        if not used_turn:
            continue

        # Check if enemy fainted
        if enemy_mon["hp"] <= 0:
            print(f"\n  {enemy_mon['name']} fainted!")
            give_exp(player_mon, enemy_mon, is_trainer=not is_wild)
            enemy_index += 1
            if enemy_index >= len(enemy_party):
                print("\nYou won the battle!")
                return "win"
            enemy_mon = enemy_party[enemy_index]
            print(f"  {enemy_mon['name']} was sent out!")
            continue

        # Enemy's turn
        print()
        enemy_attack(enemy_mon, player_mon)
        print()

        # Check if player's Pokémon fainted
        if player_mon["hp"] <= 0:
            print(f"  {player_mon['name']} fainted!")
            next_mon = next((p for p in player["party"] if p["hp"] > 0), None)
            if next_mon is None:
                print("\nYou have no more Pokémon...")
                print("You blacked out.")
                return "lose"
            player_mon = next_mon
            print(f"Go, {player_mon['name']}!")
