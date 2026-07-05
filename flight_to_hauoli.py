from pokemon import create_pokemon
from battle import battle
from sprites import get_sprite


def pause():
    input("(Press Enter to continue...)")
    print()


def flight_to_hauoli(player):
    print("=" * 40)
    print("  LUMIOSE AIRFIELD")
    print("=" * 40)
    print()
    print("There's no coast road worth the days it would take. So the")
    print("whole gang piles onto the last light plane out of Lumiose,")
    print("bound south down the shoreline for Hau'oli.")
    print()
    pause()

    print("NR: I called the window. I ALWAYS get the window.")
    print("S: You get the window over the wing. You'll see a flap. Enjoy.")
    print("Z: *already asleep before the doors close*")
    print("I: *quietly, watching the runway* ...Small plane. Only one pilot.")
    print()
    pause()

    print("The engines wind up. Lumiose drops away behind you, all lit")
    print("boulevards, and then it's just black water and a line of coast.")
    print()
    pause()

    # --- The reveal ---
    print("Somewhere over the sea, a man stands up in the aisle. Team")
    print("Fairy coat — but the seal's been torn off it. He's holding the")
    print("cockpit key.")
    print()
    print("Admin Vesk: Don't get up. Nobody's flying this thing but me now.")
    print()
    pause()

    print("NH: You're one of theirs. Team Fairy.")
    print()
    print("Vesk: WAS. They think they're building something. A weapon, a")
    print("Vesk: future, whatever the Senate's paying for. *laughs* There is")
    print("Vesk: no future. There's just the drop, and everyone pretending")
    print("Vesk: there isn't. So I'm going to stop pretending. For all of us.")
    print()
    pause()

    print("I: He's aiming us at the water.")
    print("S: Then we take the cabin before he takes the cockpit. GO!")
    print()

    # --- Cabin: Vesk's holdouts ---
    print("Two loyalists unclip from their seats and block the aisle.")
    print()
    input("(Press Enter to battle...)")
    print()

    result = battle(
        player,
        [create_pokemon("Zoroark", 60), create_pokemon("Salazzle", 61)],
        is_wild=False
    )
    if result == "lose":
        return "lose"

    print()
    print("NR: Aisle's clear! NH, the door — he's locking himself in!")
    print()
    pause()

    # --- The dive: Vesk boss ---
    print("The nose drops. Bags, cups, a loose Poké Ball all slide forward")
    print("as the sea swings up to fill every window. Vesk braces himself")
    print("in the cockpit doorway, perfectly calm, and sends out everything")
    print("he has between you and the controls.")
    print()
    print("Vesk: Good. Fight. It won't matter in ninety seconds — but it's")
    print("Vesk: nice that someone still bothers.")
    print()
    input("(Press Enter to battle Vesk...)")
    print()

    result = battle(
        player,
        [
            create_pokemon("Mismagius", 60),
            create_pokemon("Gengar",    61),
            create_pokemon("Chandelure", 62),
            create_pokemon("Hydreigon", 64),
        ],
        is_wild=False
    )
    if result == "lose":
        return "lose"

    print()
    print("Vesk goes down against the doorframe, still smiling as I hauls")
    print("him out of the way. But the plane is already screaming toward")
    print("the water, and the yoke won't come back — it's jammed hard over.")
    print()
    pause()

    # --- The team-up save ---
    print("NH: It's too heavy! I can't pull it up alone!")
    print()
    print("I: Then don't. TOGETHER — NOW!")
    print()
    pause()

    print("Every window fills with wings. I's Dragapult phases through the")
    print("hull and shoulders the nose. NR's Garchomp digs its claws into a")
    print("wing. S, Z, the whole party's dragons pour out into the wind and")
    print("get UNDER the plane, and for one impossible second the fall turns")
    print("into a glide.")
    print()
    pause()

    print("The belly hits Hau'oli's shallows in a wall of white spray,")
    print("skids up the beach, and stops. Sea water. Sunlight. Silence.")
    print("Then, one by one, everyone starts laughing — the awful, shaking")
    print("laugh of people who should not be alive.")
    print()
    pause()

    print("Z: *finally awake* ...Are we there?")
    print("NR: I picked the window seat.")
    print("I: *pulling Vesk's arm over one shoulder* Someone call the Hau'oli")
    print("I: police. He can rant to them. We walk from here.")
    print()
    pause()

    print("Soaked, rattled, and somehow whole, the gang wades up onto the")
    print("white terraces of Hau'oli City.")
    print()
    pause()

    from hauoli_city import hauoli_city
    return hauoli_city(player)
