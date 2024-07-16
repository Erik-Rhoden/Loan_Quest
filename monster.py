import random
from loot import *

def monster_selection(difficulty):
    enemy_map = {1: {
                    "green slime": {
                            "health": 2, 
                            "attack": 1, 
                            "defense": 0,
                            "speed": 0
                        }, 
                    "red slime": {
                            "health": 3, 
                            "attack": 1, 
                            "defense": 1,
                            "speed": 0
                        },
                    "silver slime": {
                            "health": 5, 
                            "attack": 2, 
                            "defense": 2,
                            "speed": 0
                        },
                    "golden slime": {
                            "health": 10, 
                            "attack": 3, 
                            "defense": 3,
                            "speed": 1
                        }},
                2: {
                    "green goblin": {
                            "health": 7,
                            "attack": 3,
                            "defense": 2,
                            "speed": 2
                        },
                    "red goblin": {
                            "health": 9,
                            "attack": 3,
                            "defense": 2,
                            "speed": 3
                        },
                    "silver goblin": {
                            "health": 11,
                            "attack": 4,
                            "defense": 3,
                            "speed": 3
                        },
                    "golden goblin": {
                            "health": 13,
                            "attack": 5,
                            "defense": 4,
                            "speed": 5
                    }},
                3: {
                    "green orc": {
                            "health": 15,
                            "attack": 7,
                            "defense": 5,
                            "speed": 5
                        },
                    "red orc": {
                            "health": 18,
                            "attack": 8,
                            "defense": 7,
                            "speed": 6
                        },
                    "silver orc": {
                            "health": 21,
                            "attack": 10,
                            "defense": 8,
                            "speed": 8
                        },
                    "golden orc": {
                            "health": 30,
                            "attack": 15,
                            "defense": 12,
                            "speed": 10
                        },
                    }
                }
    name, val = random.choice(list(enemy_map[difficulty].items()))
    health, attack, defense, speed = val["health"], val["attack"], val["defense"], val["speed"]
    return Monster(name, health, attack, defense, speed), name

class Monster():
    def __init__(self, name, health, attack, defense, speed):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed

    def get_health(self):
        return self.health

    def deal_damage(self, target):
        net_damage = self.attack - target.defense
        if target.defense > self.attack:
            target.health
        elif net_damage > target.health:
            target.health = 0
        else:
            target.health -= net_damage
    
    def __repr__(self):
        return f"The {self.name} has {self.health} health, {self.attack} attack, {self.defense} defense, and {self.speed} speed."