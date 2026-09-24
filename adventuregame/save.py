import os
import json
import player
#todo
def save_exist():
    return os.path.exists("tallennus.json")

def save_exists_for(username):
    if not save_exist():
        return False
    with open("tallennus.json", "r") as f:
        all_saves = json.load(f)
    return username in all_saves

def save_game(player):
    if save_exist():
        with open("tallennus.json", "r") as f:
            all_saves = json.load(f)
    else:
        all_saves = {}

    all_saves[player.username] = {
        "username": player.username,
        "current_scene": player.current_scene,
        "items": player.items,
        "health": player.health,
        "weapon": player.weapon
    }

    with open("tallennus.json", "w") as f:
        json.dump(all_saves, f)

def load_game(username):
    with open("tallennus.json", "r") as f:
        all_saves = json.load(f)
    data = all_saves[username]
    return player.Player(
        data["username"],
        current_scene=data["current_scene"],
        items=data["items"],
        health=data["health"],
    )