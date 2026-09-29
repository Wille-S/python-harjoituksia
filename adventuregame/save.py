import os
import json
import player
from constants import SAVE_PATH

class GameEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, player.Weapon):
            return obj.__dict__
        return super().default(obj)

def load_all_saves():
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
        "weapon": player.weapon,
    }

    with open(SAVE_PATH, "w") as f:
        json.dump(all_saves, f, cls=GameEncoder)

def load_game(username):
    with open(SAVE_PATH, "r") as f:
        all_saves = json.load(f)
    data = all_saves[username]
    return player.Player(
        data["username"],
        current_scene=data["current_scene"],
        items=data["items"],
        health=data["health"],
    )