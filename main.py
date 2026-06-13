from pokemon import create_pokemon
from sprites import get_sprite


def create_player(starter_name):
    return {
        "name": "NH",
        "starter": starter_name,
        "party": [create_pokemon(starter_name, 10)],
        "bag": {
            "Poké Ball": 5,
            "Potion": 5,
            "Ether": 1,
        },
        "money": 0,
        "box": [],
    }


def pause():
    input("(Press Enter to continue...)")
    print()


def home_scene():
    print("=" * 40)
    print("    POKEMON DRAGON VERSION")
    print("=" * 40)
    print()
    pause()

    print("Mom: NH! NH, wake up!")
    print("Mom: You slept in — again.")
    print("Mom: Get downstairs. Breakfast is ready.")
    pause()

    print("NH: I'M UP! I'M UP!")
    print("NH: Today is the day. THE day.")
    print("NH: I've been waiting for this my whole life.")
    print("NH: I can't believe it's actually happening.")
    pause()

    print("Mom: It's happening after you eat.")
    print("Mom: Sit down.")
    pause()

    print("A: I'm not eating these eggs.")
    print("A: They're boiled. Why are they always boiled.")
    pause()

    print("NH: Same. These are not journey food.")
    print("NH: These are punishment food.")
    pause()

    print("Mom: You're both eating the eggs.")
    pause()

    print("...")
    pause()

    print("Dad: *sniff*")
    print("Dad: Good morning.")
    pause()

    print("NH: Dad! You look terrible.")
    pause()

    print("Dad: I'm fine. Just a cold.")
    print("Dad: *sniff*")
    print("Dad: Don't look at me like that.")
    pause()

    print("A: Your nose is completely blocked.")
    pause()

    print("Dad: It's a little blocked.")
    print("Dad: I said I'm fine.")
    pause()

    print("Mom: Sit down. I'll make you something warm.")
    pause()

    print("Dad: NH.")
    pause()

    print("NH: Yeah?")
    pause()

    print("Dad: Come back once in a while.")
    print("Dad: And when you get better at Pokémon...")
    print("Dad: I'll be waiting for you.")
    pause()

    print("NH: ...")
    print("NH: I'll hold you to that.")
    pause()

    print("Mom: Be safe.")
    pause()

    print("You leave home.")
    print()


def larch_scene():
    print("*knock knock*")
    pause()

    print("Mom: I'll get it.")
    pause()

    print("Professor Larch: Good morning. Is NH home?")
    pause()

    print("NH: Professor Larch!")
    pause()

    print("Professor Larch: There you are. I brought something for you.")
    print("Professor Larch: These three came from Eon Palace.")
    print("Professor Larch: They've been waiting for the right trainer.")
    print("Professor Larch: Choose your partner.")
    print()

    starters = [
        ("Frodger", "Dragon / Fire"),
        ("Buliz",   "Dragon / Water"),
        ("Falake",  "Dragon / Grass"),
    ]

    sprites = [get_sprite(name) for name, _ in starters]
    labels = [f"{i}. {name} ({typing})" for i, (name, typing) in enumerate(starters, 1)]
    gap = "    "
    col_width = max(
        max(len(line) for s in sprites for line in s),
        max(len(l) for l in labels)
    ) + 2

    for row in range(max(len(s) for s in sprites)):
        line = ""
        for s in sprites:
            cell = s[row] if row < len(s) else ""
            line += cell.ljust(col_width) + gap
        print(line)

    print()
    for label in labels:
        print(label.ljust(col_width) + gap, end="")
    print()
    print()

    choice = input("Enter 1, 2, or 3: ")
    print()

    if choice == "1":
        starter = "Frodger"
    elif choice == "2":
        starter = "Buliz"
    elif choice == "3":
        starter = "Falake"
    else:
        print("Invalid choice. Try again.")
        return larch_scene()

    print(f"Professor Larch: {starter}. A fine choice.")
    print()
    for line in get_sprite(starter):
        print("  " + line)
    print()
    print("Professor Larch: Take good care of each other.")
    pause()

    return starter


def haci_scene():
    print("Haci is waiting outside.")
    pause()

    print("Haci: NH!")
    print("Haci: I heard you were finally heading out.")
    print("Haci: Here. Take these — you'll need them.")
    pause()

    print("Haci gave you 5 Poké Balls!")
    print("Haci gave you 5 Potions!")
    print("Haci gave you 1 Ether!")
    pause()

    print("Haci: Don't waste the Ether.")
    print("Haci: And don't do anything stupid.")
    pause()


def main():
    home_scene()
    starter = larch_scene()
    haci_scene()
    player = create_player(starter)
    from route1 import route1
    result = route1(player)
    if result == "lose":
        print("Game over.")


def debug_start():
    import sys

    _places = [
        ("Bakil City",     "route1",         "route1"),
        ("Saffron City",   "saffron_city",   "saffron_city"),
        ("Goldenrod City", "goldenrod_city", "goldenrod_city"),
        ("Slateport City", "slateport_city", "slateport_city"),
        ("Jubilife City",  "jubilife_city",  "jubilife_city"),
        ("Castelia City",  "castelia_city",  "castelia_city"),
        ("Lumiose City",   "lumiose_city",   "lumiose_city"),
    ]
    _places += [(f"Route {n}", f"route{n}", f"route{n}") for n in range(1, 28)]
    locations = {str(i + 1): place for i, place in enumerate(_places)}

    preset_team = [
        ("Hydrapple", 50),
        ("Psyake",    50),
        ("Dragonite", 50),
        ("Dragapult", 50),
        ("Rayquaza",  50),
        ("Sceptile",  50),
    ]

    print("=" * 40)
    print("  DEBUG MODE")
    print("=" * 40)
    print()
    print("Pick a starting location:")
    for key, (name, _, _) in locations.items():
        print(f"  {key}. {name}")
    print()
    loc_choice = input("Choose: ").strip()
    print()

    if loc_choice not in locations:
        print("Invalid choice.")
        return

    loc_name, module_name, func_name = locations[loc_choice]

    player = {
        "name": "NH",
        "starter": "Frodger",
        "party": [],
        "bag": {
            "Poké Ball":    10,
            "Potion":       5,
            "Super Potion": 5,
            "Hyper Potion": 5,
            "Max Potion":   5,
            "Revive":       5,
            "Ultra Ball":   10,
        },
        "money": 9999999,
        "box": [],
    }

    print("Team options:")
    print("  1. Preset team (Hydrapple / Psyake / Dragonite / Dragapult / Rayquaza / Sceptile — all Lv.50)")
    print("  2. Build custom team")
    print()
    team_choice = input("Choose: ").strip()
    print()

    if team_choice == "1":
        for name, lvl in preset_team:
            mon = create_pokemon(name, lvl)
            player["party"].append(mon)
            print(f"  Added {mon['name']} Lv.{lvl}")
    else:
        print("Build your team. Enter Pokémon name and level (blank to stop).")
        print("Example:  Garchomp 50")
        print()
        while len(player["party"]) < 6:
            entry = input(f"  Slot {len(player['party']) + 1}: ").strip()
            if not entry:
                break
            parts = entry.rsplit(" ", 1)
            if len(parts) != 2:
                print("  Format: PokemonName Level")
                continue
            name, lvl = parts
            try:
                lvl = int(lvl)
            except ValueError:
                print("  Level must be a number.")
                continue
            try:
                mon = create_pokemon(name, lvl)
                player["party"].append(mon)
                print(f"  Added {mon['name']} Lv.{lvl}")
            except Exception as e:
                print(f"  Couldn't create {name}: {e}")

        if not player["party"]:
            print("No Pokémon added — adding Garchomp Lv.50 as default.")
            player["party"].append(create_pokemon("Garchomp", 50))

    print()
    print(f"Starting at {loc_name} with {len(player['party'])} Pokémon. Money: $9,999,999")
    print()
    input("(Press Enter to begin...)")
    print()

    module = __import__(module_name)
    func = getattr(module, func_name)
    result = func(player)
    if result == "lose":
        print("Game over.")


if __name__ == "__main__":
    import sys
    if "--debug" in sys.argv:
        debug_start()
    else:
        main()
