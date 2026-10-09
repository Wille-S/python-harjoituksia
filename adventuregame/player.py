import random

class Weapon:
    def __init__(self, name, damage_range):
        self.name = name
        self.damage_range = damage_range
    def attack(self):
        return random.randint(*self.damage_range) # random damage between tuple values


class Player:
    def __init__(self, username, current_scene="start", items = None, health = 20):
        self.username = username
        self.items = items if items is not None else []
        self.current_scene = current_scene
        self.health = health
        self.weapon = Weapon("Nyrkit", (1, 3))
        self.animals_defeated = 0 # Counter of wolves defeated that impacts the ending
        self.helped_cub = False # If in forest scene helped cub set this flag to true
