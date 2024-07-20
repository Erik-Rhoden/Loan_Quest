import random
from loot import *

def monster_selection(difficulty):
    enemy_map = {1: {
                    "Green Slime": {
                            "health": 2, 
                            "attack": 1, 
                            "defense": 0,
                            "speed": 0
                        }, 
                    "Red Slime": {
                            "health": 3, 
                            "attack": 1, 
                            "defense": 1,
                            "speed": 0
                        },
                    "Silver Slime": {
                            "health": 5, 
                            "attack": 2, 
                            "defense": 2,
                            "speed": 0
                        },
                    "Golden Slime": {
                            "health": 10, 
                            "attack": 3, 
                            "defense": 3,
                            "speed": 1
                        }},
                2: {
                    "Green Goblin": {
                            "health": 7,
                            "attack": 3,
                            "defense": 2,
                            "speed": 2
                        },
                    "Red Goblin": {
                            "health": 9,
                            "attack": 3,
                            "defense": 2,
                            "speed": 3
                        },
                    "Silver Goblin": {
                            "health": 11,
                            "attack": 4,
                            "defense": 3,
                            "speed": 3
                        },
                    "Golden Goblin": {
                            "health": 13,
                            "attack": 5,
                            "defense": 4,
                            "speed": 5
                    }},
                3: {
                    "Green Orc": {
                            "health": 15,
                            "attack": 7,
                            "defense": 5,
                            "speed": 5
                        },
                    "Red Orc": {
                            "health": 18,
                            "attack": 8,
                            "defense": 7,
                            "speed": 6
                        },
                    "Silver Orc": {
                            "health": 21,
                            "attack": 10,
                            "defense": 8,
                            "speed": 8
                        },
                    "Golden Orc": {
                            "health": 30,
                            "attack": 15,
                            "defense": 12,
                            "speed": 10
                        },
                    }
                }
    name, val = random.choice(list(enemy_map[difficulty].items()))
    health, attack, defense, speed = val["health"], val["attack"], val["defense"], val["speed"]
    return Monster(name, health, attack, defense, speed)

class Monster():
    def __init__(self, name, health, attack, defense, speed):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.inventory = {}
        self.populate_inventory()

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

    def populate_inventory(self):
        categories = ["weapon", "armor", "potion", "misc"]
        available_items = [random.choice(list(loot_map[self.name][category].items())) for category in categories]
        random.shuffle(available_items)
        quantity = random.randint(1, 4)
        selected_items = [item for item in available_items[:quantity] if item != ('Empty', 0)]
        for item in selected_items:
            item_key, item_value = item
            if isinstance(item, tuple) and isinstance(item[1], dict):
                if 'Heal' in item_value:
                    self.inventory[item_key] = "potion"
                if 'Damage' in item_value:
                    self.inventory[item_key] = "weapon"
                    self.update_attack()
                if 'Defense' in item_value:
                    self.inventory[item_key] = "armor"
                    self.update_defense()
            else:
                self.inventory[item_key] = "misc"

    def update_attack(self):
        for item, category in self.inventory.items():
            if category == "weapon" and isinstance(item, dict):
                self.attack += item['Damage']

    def update_defense(self):
        for item, category in self.inventory.items():
            if category == "armor" and isinstance(item, dict):
                self.defense += item['Defense']

    def __repr__(self):
        return f"The {self.name} has {self.health} health, {self.attack} attack, {self.defense} defense, and {self.speed} speed. {self.inventory}"