# Shared Sky Buggy fast-travel, used by every city from Goldenrod onward.
# WORLD is the full exploration order (towns and routes interleaved).
# A city offers travel to everywhere explored BEFORE it via destinations_before().

WORLD = [
    ("Bakil City",     "route1",         "route1"),
    ("Route 1",        "route1",         "route1"),
    ("Saffron City",   "saffron_city",   "saffron_city"),
    ("Route 2",        "route2",         "route2"),
    ("Route 3",        "route3",         "route3"),
    ("Route 4",        "route4",         "route4"),
    ("Route 5",        "route5",         "route5"),
    ("Route 6",        "route6",         "route6"),
    ("Route 7",        "route7",         "route7"),
    ("Goldenrod City", "goldenrod_city", "goldenrod_city"),
    ("Route 8",        "route8",         "route8"),
    ("Route 9",        "route9",         "route9"),
    ("Route 10",       "route10",        "route10"),
    ("Route 11",       "route11",        "route11"),
    ("Route 12",       "route12",        "route12"),
    ("Slateport City", "slateport_city", "slateport_city"),
    ("Route 13",       "route13",        "route13"),
    ("Route 14",       "route14",        "route14"),
    ("Route 15",       "route15",        "route15"),
    ("Jubilife City",  "jubilife_city",  "jubilife_city"),
    ("Route 16",       "route16",        "route16"),
    ("Route 17",       "route17",        "route17"),
    ("Route 18",       "route18",        "route18"),
    ("Route 19",       "route19",        "route19"),
    ("Route 20",       "route20",        "route20"),
    ("Route 21",       "route21",        "route21"),
    ("Castelia City",  "castelia_city",  "castelia_city"),
    ("Route 22",       "route22",        "route22"),
    ("Route 23",       "route23",        "route23"),
    ("Route 24",       "route24",        "route24"),
    ("Route 25",       "route25",        "route25"),
    ("Route 26",       "route26",        "route26"),
    ("Route 27",       "route27",        "route27"),
    ("Lumiose City",   "lumiose_city",   "lumiose_city"),
    ("Hau'oli City",   "hauoli_city",    "hauoli_city"),
]


def pause():
    input("(Press Enter to continue...)")
    print()


def destinations_before(city_name):
    # Everywhere explored by the time you reach city_name (not including it).
    names = [d[0] for d in WORLD]
    return WORLD[:names.index(city_name)]


def bakil_home_visit(player):
    print("=" * 40)
    print("  BAKIL CITY — HOME")
    print("=" * 40)
    print()
    print("The Sky Buggy sets down on the dusty road outside your house.")
    print("The door opens before you even reach it.")
    print()
    pause()

    print("Mom: NH! You're home!")
    print("Mom: Look at you. Come here — let me look at you properly.")
    print()
    pause()

    print("Dad: *sniff*")
    print("Dad: Is that... NH?")
    print()
    pause()

    print("NH: Dad? You're STILL sick?")
    print()
    pause()

    print("Dad: It's the same cold. *sniff*")
    print("Dad: It's a strong one. Don't judge it.")
    print()
    pause()

    print("Mom: He won't rest. I keep telling him.")
    print()
    pause()

    print("Dad: *slowly gets up anyway*")
    print("Dad: Come here. ...You're really out there, aren't you.")
    print("Dad: I said I'd be waiting. *sniff* I meant it.")
    print("Dad: Win some badges. Come home when you can.")
    print()
    pause()

    print("Mom: Sit down, both of you. I'll make something warm.")
    print("Mom: ...And NH, your Pokémon look worn out. Let them rest a while.")
    print()
    pause()

    for mon in player["party"]:
        mon["hp"] = mon["max_hp"]
    print("Your team rested at home and recovered fully!")
    print()
    pause()

    print("After a warm meal, you head back out to the Sky Buggy.")
    print()
    pause()


def sky_buggy(player, destinations):
    while True:
        print("=" * 40)
        print("  SKY BUGGY")
        print("=" * 40)
        print()
        print("The Sky Buggy can take you anywhere you've already explored.")
        print("Where to?")
        for i, (name, _, _) in enumerate(destinations, 1):
            print(f"  {i}. {name}")
        print(f"  {len(destinations) + 1}. Stay here")
        print()
        choice = input("Choose: ").strip()
        print()

        if choice == str(len(destinations) + 1):
            print("You climb back out of the buggy.")
            print()
            return None

        if choice.isdigit() and 1 <= int(choice) <= len(destinations):
            name, module_name, func_name = destinations[int(choice) - 1]
            if name == "Bakil City":
                bakil_home_visit(player)
                continue
            print(f"The Sky Buggy lifts off and carries you to {name}.")
            print()
            pause()
            module = __import__(module_name)
            func = getattr(module, func_name)
            return func(player)

        print("Invalid choice.")
        print()
