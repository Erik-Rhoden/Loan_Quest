# from main import path_difficulty
import random

def monster_selection(difficulty):
    enemy_map = {1: {
                    "green slime": {
                            "health": 2, 
                            "attack": 1, 
                            "defense": 0
                        }, 
                    "red slime": {
                            "health": 3, 
                            "attack": 1, 
                            "defense": 1
                        },
                    "silver slime": {
                            "health": 5, 
                            "attack": 2, 
                            "defense": 2
                        },
                    "golden slime": {
                            "health": 10, 
                            "attack": 3, 
                            "defense": 3
                        }},
                2: {
                    "green goblin": {
                            "health": 7,
                            "attack": 3,
                            "defense": 2
                        },
                    "red goblin": {
                            "health": 9,
                            "attack": 3,
                            "defense": 2
                        },
                    "silver goblin": {
                            "health": 11,
                            "attack": 4,
                            "defense": 3
                        },
                    "golden goblin": {
                            "health": 13,
                            "attack": 5,
                            "defense": 4
                    }},
                3: {
                    "green orc": {
                            "health": 15,
                            "attack": 7,
                            "defense": 5
                        },
                    "red orc": {
                            "health": 18,
                            "attack": 8,
                            "defense": 7
                        },
                    "silver orc": {
                            "health": 21,
                            "attack": 10,
                            "defense": 8
                        },
                    "golden orc": {
                            "health": 30,
                            "attack": 15,
                            "defense": 12
                        },
                    }
                }
    monster, val = random.choice(list(enemy_map[difficulty].items()))
    name, health, attack, defense = monster, val["health"], val["attack"], val["defense"]
    return Monster(name, health, attack, defense)

class Monster():
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def get_health(self):
        return self.health

    def deal_damage(self, target):
        net_damage = self.attack - target.defense
        if target.defense > self.attack:
            return target.health
        if net_damage > target.health:
            target.health = 0
            return target.health
        target.health -= net_damage
    
    def __repr__(self):
        return f"The {self.name} has {self.health} health, {self.attack} attack, and {self.defense} defense."