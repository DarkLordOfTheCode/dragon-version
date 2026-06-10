def pause():
    input("(Press Enter to continue...)")
    print()


def pc_box(player):
    if "box" not in player:
        player["box"] = []

    while True:
        print("=" * 40)
        print("  PC BOX")
        print("=" * 40)
        print()
        print(f"  Party: {len(player['party'])} Pokémon")
        print(f"  Box:   {len(player['box'])} Pokémon")
        print()
        print("  1. Deposit (party → box)")
        print("  2. Withdraw (box → party)")
        print("  3. View box")
        print("  4. Leave")
        print()
        choice = input("Choose: ").strip()
        print()

        if choice == "1":
            deposit(player)
        elif choice == "2":
            withdraw(player)
        elif choice == "3":
            view_box(player)
        elif choice == "4":
            return
        else:
            print("Invalid choice.")
            print()


def deposit(player):
    if len(player["party"]) <= 1:
        print("You can't deposit your last Pokémon.")
        print()
        return

    print("Deposit which Pokémon?")
    print()
    for i, mon in enumerate(player["party"], 1):
        print(f"  {i}. {mon['name']} Lv.{mon['level']}  HP: {mon['hp']}/{mon['max_hp']}")
    print(f"  {len(player['party']) + 1}. Cancel")
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
        if len(player["party"]) <= 1:
            print("You can't deposit your last Pokémon.")
            print()
            return
        mon = player["party"].pop(idx)
        player["box"].append(mon)
        print(f"{mon['name']} was sent to the box.")
        print()
    except ValueError:
        print("Invalid choice.")
        print()


def withdraw(player):
    if not player["box"]:
        print("The box is empty.")
        print()
        return

    if len(player["party"]) >= 6:
        print("Your party is full. Deposit a Pokémon first.")
        print()
        return

    print("Withdraw which Pokémon?")
    print()
    for i, mon in enumerate(player["box"], 1):
        print(f"  {i}. {mon['name']} Lv.{mon['level']}  HP: {mon['hp']}/{mon['max_hp']}")
    print(f"  {len(player['box']) + 1}. Cancel")
    print()
    choice = input("Choose: ").strip()
    print()
    try:
        idx = int(choice) - 1
        if idx == len(player["box"]):
            return
        if not (0 <= idx < len(player["box"])):
            print("Invalid choice.")
            print()
            return
        mon = player["box"].pop(idx)
        player["party"].append(mon)
        print(f"{mon['name']} was added to your party!")
        print()
    except ValueError:
        print("Invalid choice.")
        print()


def view_box(player):
    if not player["box"]:
        print("The box is empty.")
        print()
        return
    print("Box contents:")
    print()
    for i, mon in enumerate(player["box"], 1):
        moves_str = ", ".join(mon["moves"]) if mon["moves"] else "—"
        print(f"  {i}. {mon['name']} Lv.{mon['level']}  HP: {mon['hp']}/{mon['max_hp']}  [{moves_str}]")
    print()
