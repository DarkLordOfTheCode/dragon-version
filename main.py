from pokemon import create_pokemon


def create_player(starter_name):
    return {
        "name": "NH",
        "party": [create_pokemon(starter_name, 5)],
        "bag": {
            "Poké Ball": 5,
            "Potion": 5,
            "Ether": 1,
        },
        "money": 0,
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

    print("Narmina: NH! NH, wake up!")
    print("Narmina: You slept in — again.")
    print("Narmina: Get downstairs. Breakfast is ready.")
    pause()

    print("NH: I'M UP! I'M UP!")
    print("NH: Today is the day. THE day.")
    print("NH: I've been waiting for this my whole life.")
    print("NH: I can't believe it's actually happening.")
    pause()

    print("Narmina: It's happening after you eat.")
    print("Narmina: Sit down.")
    pause()

    print("Aziza: I'm not eating these eggs.")
    print("Aziza: They're boiled. Why are they always boiled.")
    pause()

    print("NH: Same. These are not journey food.")
    print("NH: These are punishment food.")
    pause()

    print("Narmina: You're both eating the eggs.")
    pause()

    print("...")
    pause()

    print("Hasan: *sniff*")
    print("Hasan: Good morning.")
    pause()

    print("NH: Dad! You look terrible.")
    pause()

    print("Hasan: I'm fine. Just a cold.")
    print("Hasan: *sniff*")
    print("Hasan: Don't look at me like that.")
    pause()

    print("Aziza: Your nose is completely blocked.")
    pause()

    print("Hasan: It's a little blocked.")
    print("Hasan: I said I'm fine.")
    pause()

    print("Narmina: Sit down. I'll make you something warm.")
    pause()

    print("Hasan: NH.")
    pause()

    print("NH: Yeah?")
    pause()

    print("Hasan: Come back once in a while.")
    print("Hasan: And when you get better at Pokémon...")
    print("Hasan: I'll be waiting for you.")
    pause()

    print("NH: ...")
    print("NH: I'll hold you to that.")
    pause()

    print("Narmina: Be safe.")
    pause()

    print("You leave home.")
    print()


def larch_scene():
    print("*knock knock*")
    pause()

    print("Narmina: I'll get it.")
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
    print("1. Frodger  (Dragon / Fire)")
    print("2. Buliz    (Dragon / Water)")
    print("3. Falake   (Dragon / Grass)")
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


if __name__ == "__main__":
    main()
