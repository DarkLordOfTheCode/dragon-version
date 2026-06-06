from pokedex import pokedex
from learnsets import learnsets
from evolutions import evolutions


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

    if mon["name"] in evolutions:
        evo_name, evo_level = evolutions[mon["name"]]
        if level >= evo_level:
            old_name = mon["name"]
            new_data = pokedex[evo_name]
            mon["name"] = evo_name
            mon["types"] = new_data["type"]
            mon["base_stats"] = {
                "hp":      new_data["hp"],
                "attack":  new_data["attack"],
                "defence": new_data["defence"],
                "special": new_data["special"],
                "speed":   new_data["speed"],
            }
            b = mon["base_stats"]
            old_max_hp = mon["max_hp"]
            new_max_hp = calc_hp(b["hp"], level)
            mon["max_hp"] = new_max_hp
            mon["hp"] = min(mon["hp"] + (new_max_hp - old_max_hp), new_max_hp)
            mon["attack"]  = calc_stat(b["attack"],  level)
            mon["defence"] = calc_stat(b["defence"], level)
            mon["special"] = calc_stat(b["special"], level)
            mon["speed"]   = calc_stat(b["speed"],   level)
            print(f"\n  Congratulations! Your {old_name} evolved into {evo_name}!")
            for learn_level, move_list in learnsets.get(evo_name, {}).items():
                if learn_level <= level:
                    for move in move_list:
                        if move not in mon["moves"]:
                            if len(mon["moves"]) < 4:
                                mon["moves"].append(move)
                                print(f"  {evo_name} learned {move}!")
