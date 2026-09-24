import random

class Weapon:
    def __init__(self, name, damage_range):
        self.name = name
        self.damage_range = damage_range
    def attack(self):
        return random.randint(*self.damage_range)


class Player:
    def __init__(self, username, current_scene="start", items = None, health = 10):
        self.username = username
        self.items = items if items is not None else []
        self.current_scene = current_scene
        self.health = health
        self.weapon = Weapon("Nyrkit", (1, 3))
