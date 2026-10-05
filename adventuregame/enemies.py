import random

class Enemy:
    def __init__(self, name, health, damage_range):
        self.name = name
        self.health = health
        self.damage_range = damage_range
        
    def attack(self):
        return random.randint(*self.damage_range)
    
    def is_alive(self):
        return self.health > 0
    
class Boss(Enemy):
    def __init__(self, name, health, damage_range, double_damage_chance):
        super().__init__(name, health, damage_range)
        self.double_damage_chance = double_damage_chance
        
    def special_attack(self):
        if random.random() < self.double_damage_chance:
            return random.randint(*self.damage_range) * 2  # Double damage for special attack
        return 0