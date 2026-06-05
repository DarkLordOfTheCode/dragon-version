routes = {
    "Route 1": {
        "description": "A dusty path stretching north from Bakil City. Dragon whelps bask in the afternoon heat.",
        "wild_pokemon": [
            {"name": "Trapinch", "min_level": 3, "max_level": 5, "rate": 40},
            {"name": "Dreepy",   "min_level": 3, "max_level": 5, "rate": 40},
            {"name": "Gible",    "min_level": 4, "max_level": 6, "rate": 20},
        ],
        "trainers": [
            {
                "name": "Teymur",
                "class": "Young Trainer",
                "team": [("Trapinch", 4)],
                "greeting": "Teymur: Dragons are the best Pokémon ever! Come on, battle me!",
                "defeat_text": "Teymur: You're really good... I'm gonna train way harder.",
                "reward": 200,
            },
            {
                "name": "Nigar",
                "class": "Young Trainer",
                "team": [("Dreepy", 5)],
                "greeting": "Nigar: My Dreepy is a ghost AND a dragon. Nobody can beat that!",
                "defeat_text": "Nigar: Okay... maybe someone can beat that.",
                "reward": 250,
            },
        ],
    },

    "Route 2": {
        "description": "A wider road lined with tall grass. Trainers come here to catch their first Gible.",
        "wild_pokemon": [
            {"name": "Trapinch",  "min_level": 6, "max_level": 8,  "rate": 35},
            {"name": "Dinovinery","min_level": 6, "max_level": 8,  "rate": 25},
            {"name": "Pikachu",   "min_level": 5, "max_level": 8,  "rate": 25},
            {"name": "Gible",     "min_level": 7, "max_level": 9,  "rate": 14},
            {"name": "Vibrava",   "min_level": 8, "max_level": 10, "rate": 1},
        ],
        "trainers": [
            {
                "name": "Tural",
                "class": "Young Trainer",
                "team": [("Trapinch", 6), ("Pikachu", 6)],
                "greeting": "Tural: I caught a Pikachu AND a Trapinch! I'm basically unstoppable!",
                "defeat_text": "Tural: Okay... I might need a few more levels first.",
                "reward": 300,
            },
            {
                "name": "Aytən",
                "class": "Young Trainer",
                "team": [("Gible", 7), ("Dinovinery", 7)],
                "greeting": "Aytən: Gible is going to be a Garchomp one day. And then you'll be sorry.",
                "defeat_text": "Aytən: Just you wait. Garchomp. One day.",
                "reward": 350,
            },
            {
                "name": "Orxan",
                "class": "Young Trainer",
                "team": [("Pikachu", 7), ("Trapinch", 8)],
                "greeting": "Orxan: Dad says anyone heading to Saffron City must be serious. Are you serious?",
                "defeat_text": "Orxan: ...Yeah. You're serious.",
                "reward": 400,
            },
        ],
    },

    "Route 3": {
        "description": "The final stretch before Saffron City. Serious trainers only.",
        "wild_pokemon": [
            {"name": "Trapinch",  "min_level": 9,  "max_level": 11, "rate": 35},
            {"name": "Dinovinery","min_level": 9,  "max_level": 11, "rate": 25},
            {"name": "Pikachu",   "min_level": 8,  "max_level": 11, "rate": 25},
            {"name": "Gible",     "min_level": 10, "max_level": 12, "rate": 14},
            {"name": "Vibrava",   "min_level": 11, "max_level": 13, "rate": 1},
        ],
        "trainers": [
            {
                "name": "Nərmin",
                "class": "Young Trainer",
                "team": [("Trapinch", 9), ("Gible", 9)],
                "greeting": "Nərmin: Saffron's gym is just ahead! I'm going to win my first badge!",
                "defeat_text": "Nərmin: Hmm... maybe I should train on this route a bit longer.",
                "reward": 450,
            },
            {
                "name": "Kənan",
                "class": "Young Trainer",
                "team": [("Dreepy", 10), ("Pikachu", 9)],
                "greeting": "Kənan: Hey, do you know anything about Sabina? The gym leader? Is she scary?",
                "defeat_text": "Kənan: Great. I can't beat a random trainer. I'm definitely not ready for the gym.",
                "reward": 500,
            },
            {
                "name": "Dilarə",
                "class": "Young Trainer",
                "team": [("Gible", 11), ("Dinovinery", 10)],
                "greeting": "Dilarə: My brother beat Sabina last year. I'm going to beat her this year. Starting with you!",
                "defeat_text": "Dilarə: You're better than my brother was. That's actually a compliment.",
                "reward": 550,
            },
        ],
    },

    "Route 4": {
        "description": "Rolling hills north of Saffron City. Wild Pokémon are noticeably stronger here.",
        "wild_pokemon": [
            {"name": "Bagon",      "min_level": 14, "max_level": 17, "rate": 35},
            {"name": "Horsea",     "min_level": 14, "max_level": 17, "rate": 30},
            {"name": "Zorua",      "min_level": 14, "max_level": 16, "rate": 20},
            {"name": "Dinovinery", "min_level": 13, "max_level": 16, "rate": 15},
        ],
        "trainers": [
            {
                "name": "Aynur",
                "class": "Young Trainer",
                "team": [("Bagon", 14), ("Horsea", 14)],
                "greeting": "Aynur: I've been training on this route for weeks. You won't get past me!",
                "defeat_text": "Aynur: Okay... maybe I needed a few more weeks.",
                "reward": 700,
            },
            {
                "name": "Murad",
                "class": "Young Trainer",
                "team": [("Zorua", 15), ("Dinovinery", 15)],
                "greeting": "Murad: Zorua can disguise itself as anything. Good luck figuring out what you're fighting.",
                "defeat_text": "Murad: You didn't even seem confused. Impressive.",
                "reward": 750,
            },
            {
                "name": "Samir",
                "class": "Young Trainer",
                "team": [("Bagon", 16), ("Horsea", 15)],
                "greeting": "Samir: I caught both of these here today. Fresh and fired up!",
                "defeat_text": "Samir: Fresh caught but not trained enough. I see the problem.",
                "reward": 800,
            },
        ],
    },

    "Route 5": {
        "description": "A foggy valley. Cold air drifts south — a sign of what lies further north.",
        "wild_pokemon": [
            {"name": "Bagon",   "min_level": 15, "max_level": 18, "rate": 25},
            {"name": "Horsea",  "min_level": 15, "max_level": 18, "rate": 25},
            {"name": "Zorua",   "min_level": 15, "max_level": 17, "rate": 25},
            {"name": "Sneasel", "min_level": 14, "max_level": 17, "rate": 25},
        ],
        "trainers": [
            {
                "name": "Fuad",
                "class": "Young Trainer",
                "team": [("Zorua", 16), ("Sneasel", 15)],
                "greeting": "Fuad: Dark types never fall for tricks. Which means I never fall for tricks either.",
                "defeat_text": "Fuad: ...Guess you don't fall for tricks either.",
                "reward": 850,
            },
            {
                "name": "Pərvin",
                "class": "Young Trainer",
                "team": [("Horsea", 16), ("Bagon", 17)],
                "greeting": "Pərvin: I've been waiting here for a strong trainer. Finally someone shows up.",
                "defeat_text": "Pərvin: Even stronger than I hoped. Well done.",
                "reward": 900,
            },
            {
                "name": "Camalə",
                "class": "Young Trainer",
                "team": [("Sneasel", 17), ("Zorua", 17), ("Bagon", 16)],
                "greeting": "Camalə: Three Pokémon. You ready for that?",
                "defeat_text": "Camalə: You were ready for that.",
                "reward": 950,
            },
        ],
    },

    "Route 6": {
        "description": "A forested road. Evolved Pokémon are starting to appear — things are getting serious.",
        "wild_pokemon": [
            {"name": "Shelgon",    "min_level": 16, "max_level": 19, "rate": 20},
            {"name": "Seadra",     "min_level": 16, "max_level": 19, "rate": 20},
            {"name": "Zorua",      "min_level": 16, "max_level": 18, "rate": 25},
            {"name": "Sneasel",    "min_level": 16, "max_level": 18, "rate": 20},
            {"name": "Misdreavus", "min_level": 15, "max_level": 18, "rate": 15},
        ],
        "trainers": [
            {
                "name": "Ceyhun",
                "class": "Young Trainer",
                "team": [("Shelgon", 17), ("Zorua", 16)],
                "greeting": "Ceyhun: My Shelgon evolved last week. It's basically unstoppable now.",
                "defeat_text": "Ceyhun: ...Basically unstoppable. Not actually unstoppable. Got it.",
                "reward": 1000,
            },
            {
                "name": "Məlahət",
                "class": "Young Trainer",
                "team": [("Seadra", 18), ("Sneasel", 17)],
                "greeting": "Məlahət: The fog on this route hides a lot. You'd better be ready for anything.",
                "defeat_text": "Məlahət: You were ready for everything. Fair enough.",
                "reward": 1050,
            },
            {
                "name": "Oktay",
                "class": "Young Trainer",
                "team": [("Misdreavus", 18), ("Shelgon", 18)],
                "greeting": "Oktay: Ghost and Dragon. You tell me which one scares you more.",
                "defeat_text": "Oktay: Neither. The answer was neither. Noted.",
                "reward": 1100,
            },
        ],
    },

    "Route 7": {
        "description": "The last stretch before Goldenrod City. Only serious trainers make it this far.",
        "wild_pokemon": [
            {"name": "Shelgon",    "min_level": 17, "max_level": 20, "rate": 20},
            {"name": "Seadra",     "min_level": 17, "max_level": 20, "rate": 20},
            {"name": "Misdreavus", "min_level": 17, "max_level": 19, "rate": 25},
            {"name": "Zorua",      "min_level": 17, "max_level": 19, "rate": 20},
            {"name": "Quadrabirr", "min_level": 16, "max_level": 19, "rate": 15},
        ],
        "trainers": [
            {
                "name": "Zəhra",
                "class": "Young Trainer",
                "team": [("Zorua", 18), ("Misdreavus", 17)],
                "greeting": "Zəhra: Dark and Ghost. Let's see how you handle things you can't easily hit.",
                "defeat_text": "Zəhra: You handled it fine. Ugh.",
                "reward": 1150,
            },
            {
                "name": "Bəhruz",
                "class": "Young Trainer",
                "team": [("Seadra", 19), ("Shelgon", 18)],
                "greeting": "Bəhruz: Goldenrod's just ahead. I'm going to beat you and walk in feeling great.",
                "defeat_text": "Bəhruz: ...I'll still walk in. Just not feeling great.",
                "reward": 1200,
            },
            {
                "name": "Leyla",
                "class": "Ace Trainer",
                "team": [("Misdreavus", 19), ("Seadra", 19), ("Shelgon", 20)],
                "greeting": "Leyla: You've come a long way from Bakil City. Prove you deserve to walk through those gates.",
                "defeat_text": "Leyla: You deserve it. Goldenrod is waiting.",
                "reward": 1300,
            },
        ],
    },
}
