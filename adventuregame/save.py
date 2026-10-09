import os
import json
import player
from constants import SAVE_PATH

class GameEncoder(json.JSONEncoder):
    # Json dump can turn object into dictnow
    def default(self, obj):
        if isinstance(obj, player.Weapon):
            return obj.__dict__
        return super().default(obj)

def load_all_saves():
    # A missing or corrupted file counts as "no saves yet"
    try:
        with open(SAVE_PATH, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return {}

def save_exist():
    return os.path.exists(SAVE_PATH)

def save_exists_for(username):
    if not save_exist():
        return False
    all_saves = load_all_saves()
    return username in all_saves

def save_game(player):
    all_saves = load_all_saves()

    all_saves[player.username] = {
        "username": player.username,
        "current_scene": player.current_scene,
        "items": player.items,
        "health": player.health,
        "weapon": player.weapon,  # raw object, GameEncoder converts it
        "animals_defeated": player.animals_defeated,
    }

    with open(SAVE_PATH, "w", encoding="utf-8") as f:
        json.dump(all_saves, f, cls=GameEncoder, ensure_ascii=False)

def load_game(username):
    all_saves = load_all_saves()
    data = all_saves[username]

    loaded = player.Player(
        data["username"],
        current_scene=data["current_scene"],
        items=data["items"],
        health=data["health"],
    )
    loaded.animals_defeated = data.get("animals_defeated", 0)

    # json gives the weapon back as a plain dict, so rebuild the object
    weapon_data = data.get("weapon")
    if weapon_data:
        loaded.weapon = player.Weapon(weapon_data["name"], tuple(weapon_data["damage_range"]))

    return loaded