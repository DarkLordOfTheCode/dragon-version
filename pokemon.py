from pokedex import pokedex
from learnsets import learnsets


def calc_hp(base, level):
    return (base * 2 * level) // 100 + level + 10


def calc_stat(base, level):
    return (base * 2 * level) // 100 + 5


def exp_to_next_level(level):
    return level * 10


def get_moves(name, level):
    moves = []
    for learn_level, move_list in learnsets[name].items():
        if learn_level <= level:
            moves.extend(move_list)
    return moves[-4:]


def create_pokemon(name, level):
    data = pokedex[name]
    return {
        "name": name,
        "level": level,
        "hp": calc_hp(data["hp"], level),
        "max_hp": calc_hp(data["hp"], level),
        "attack": calc_stat(data["attack"], level),
        "defence": calc_stat(data["defence"], level),
        "special": calc_stat(data["special"], level),
        "speed": calc_stat(data["speed"], level),
        "types": data["type"],
        "moves": get_moves(name, level),
        "exp": 0,
        "exp_to_next": exp_to_next_level(level),
        "base_stats": {
            "hp":      data["hp"],
            "attack":  data["attack"],
            "defence": data["defence"],
            "special": data["special"],
            "speed":   data["speed"],
        },
    }


def level_up(mon):
    old_max_hp = mon["max_hp"]
    mon["level"] += 1
    level = mon["level"]
    b = mon["base_stats"]

    new_max_hp = calc_hp(b["hp"], level)
    mon["max_hp"] = new_max_hp
    mon["hp"] = min(mon["hp"] + (new_max_hp - old_max_hp), new_max_hp)
    mon["attack"]  = calc_stat(b["attack"],  level)
    mon["defence"] = calc_stat(b["defence"], level)
    mon["special"] = calc_stat(b["special"], level)
    mon["speed"]   = calc_stat(b["speed"],   level)
    mon["exp"] = 0
    mon["exp_to_next"] = exp_to_next_level(level)

    new_moves = learnsets.get(mon["name"], {}).get(level, [])
    for move in new_moves:
        if len(mon["moves"]) < 4:
            mon["moves"].append(move)
            print(f"  {mon['name']} learned {move}!")
        else:
            print(f"  {mon['name']} wants to learn {move} but already knows 4 moves.")
