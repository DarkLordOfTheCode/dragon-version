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
                "name": "Mira",
                "class": "Young Trainer",
                "team": [("Dreepy", 5)],
                "greeting": "Mira: My Dreepy is a ghost AND a dragon. Nobody can beat that!",
                "defeat_text": "Mira: Okay... maybe someone can beat that.",
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
                "name": "Leo",
                "class": "Young Trainer",
                "team": [("Trapinch", 6), ("Pikachu", 6)],
                "greeting": "Leo: I caught a Pikachu AND a Trapinch! I'm basically unstoppable!",
                "defeat_text": "Leo: Okay... I might need a few more levels first.",
                "reward": 300,
            },
            {
                "name": "Ivy",
                "class": "Young Trainer",
                "team": [("Gible", 7), ("Dinovinery", 7)],
                "greeting": "Ivy: Gible is going to be a Garchomp one day. And then you'll be sorry.",
                "defeat_text": "Ivy: Just you wait. Garchomp. One day.",
                "reward": 350,
            },
            {
                "name": "Rex",
                "class": "Young Trainer",
                "team": [("Pikachu", 7), ("Trapinch", 8)],
                "greeting": "Rex: Dad says anyone heading to Saffron City must be serious. Are you serious?",
                "defeat_text": "Rex: ...Yeah. You're serious.",
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
                "name": "Nora",
                "class": "Young Trainer",
                "team": [("Trapinch", 9), ("Gible", 9)],
                "greeting": "Nora: Saffron's gym is just ahead! I'm going to win my first badge!",
                "defeat_text": "Nora: Hmm... maybe I should train on this route a bit longer.",
                "reward": 450,
            },
            {
                "name": "Kai",
                "class": "Young Trainer",
                "team": [("Dreepy", 10), ("Pikachu", 9)],
                "greeting": "Kai: Hey, do you know anything about Sabina? The gym leader? Is she scary?",
                "defeat_text": "Kai: Great. I can't beat a random trainer. I'm definitely not ready for the gym.",
                "reward": 500,
            },
            {
                "name": "Dani",
                "class": "Young Trainer",
                "team": [("Gible", 11), ("Dinovinery", 10)],
                "greeting": "Dani: My brother beat Sabina last year. I'm going to beat her this year. Starting with you!",
                "defeat_text": "Dani: You're better than my brother was. That's actually a compliment.",
                "reward": 550,
            },
        ],
    },
}
