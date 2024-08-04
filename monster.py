import random
from loot import *

class Monster():
    def __init__(self, name, health, attack, defense, speed):
        self.name = name
        self.health = health
        self.max_hp = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.main_hand = []
        self.off_hand = []
        self.head = []
        self.legs = []
        self.feet = []
        self.chest = []
        self.gold = 0
        self.inventory = []
        self.populate_inventory()
        self.equip_items()

    def get_health(self):
        return self.health

    def deal_damage(self, target):
        damage = int(round(self.attack * (1 - target.defense / (target.defense + 50)), 0))
        if self.speed > target.speed * 3:
            modifier = ((self.speed - (target.speed * 3)) / 10) + 1
            if random.randint(1,3) == 1:
                critical_hit = damage * modifier
                target.health -= critical_hit
                print(f"{target.name} has taken {critical_hit} critical damage!")
            else:
                target.health -= damage
                print(f"{target.name} has taken {damage} damage!")
        else:
            target.health -= damage
            print(f"{target.name} has taken {damage} damage!")

    def heal_self(self):
        heal_amount = 0
        for item in self.inventory:
            if hasattr(item, 'heal'):
                heal_amount = item.heal
                if self.health + item.heal >= self.max_hp:
                    self.health = self.max_hp
                    self.inventory.remove(item)
                elif self.health + item.heal < self.max_hp:
                    self.health += item.heal
                    self.inventory.remove(item)
        return heal_amount

    def populate_inventory(self):
        categories = ["potion", "misc"]
        available_items = [random.choice(list(loot_map[self.name][category].items())) for category in categories]
        random.shuffle(available_items)
        quantity = random.randint(1, 3)
        selected_items = [item for item in available_items[:quantity] if item != ('Empty', 0)]
        for item in selected_items:
            item_name, item_properties = item
            if "Useless" in item_properties:
                junk = Item(item_name, "Junk", item_properties["Value"])
                self.inventory.append(junk)
            if "Heal" in item_properties:
                potion = Potion(item_name, "Potion", item_properties["Value"], item_properties["Heal"])
                self.inventory.append(potion)
            if "Gold" in item_properties:
                self.gold += item_properties["Value"]
                selected_items.remove(item)

    def get_inventory_list(self):
        self.inventory_list = []
        for item in self.inventory:
            self.inventory_list.append(item)
        return self.inventory_list

    def equip_items(self):
        available_chest, available_head, available_legs, available_feet, available_weapon, available_off_hand = [], [], [], [], [], []
        for loot_name, loot_properties in loot_map[self.name]["armor"].items():
            if loot_name == "Empty":
                continue
            else:
                armor_piece = Armor(loot_name, "Armor", loot_properties["Value"], loot_properties["Defense"], loot_properties["Speed"], loot_properties["Body"])
                if loot_properties["Body"] == "Chest":
                    available_chest.append(armor_piece)
                if loot_properties["Body"] == "Head":
                    available_head.append(armor_piece)
                if loot_properties["Body"] == "Legs":
                    available_head.append(armor_piece)
                if loot_properties["Body"] == "Feet":
                    available_head.append(armor_piece)
                if loot_properties["Body"] == "Off-Hand":
                    available_off_hand.append(armor_piece)
        for available_armor in [available_chest, available_head, available_legs, available_feet]:
            if available_armor:
                chosen_armor = random.choice(available_armor)
                self.inventory.append(chosen_armor)
                self.update_defense(chosen_armor)
                self.update_speed(chosen_armor)
        for loot_name, loot_properties in loot_map[self.name]["weapon"].items():
            if loot_name == "Empty":
                continue
            else:
                weapon = Weapon(loot_name, "Weapon", loot_properties["Value"], loot_properties["Damage"], loot_properties["Speed"], loot_properties["Two-Hand"])
                available_weapon.append(weapon)

        weapon_one = random.choice(available_weapon) if available_weapon else None
        weapon_two = random.choice(available_weapon) if available_weapon else None
        off_hand = random.choice(available_off_hand) if available_off_hand else None

        random_roll = random.randint(1,3)

        if random_roll == 3 and weapon_one and weapon_two:
            if not weapon_one.two_hand or not weapon_two.two_hand:
                if not weapon_one.two_hand:
                    self.inventory.append(weapon_one)
                    if off_hand:
                        self.inventory.append(off_hand)
                        self.update_defense(off_hand)
                        self.update_speed(off_hand)
                    self.update_attack(weapon_one)
                    self.update_speed(weapon_one)
                else:
                    self.inventory.append(weapon_two)
                    if off_hand:
                        self.inventory.append(off_hand)
                        self.update_defense(off_hand)
                        self.update_speed(off_hand)
                    self.update_attack(weapon_two)
                    self.update_speed(weapon_two)
        elif random_roll in [1, 2]:
            if (weapon_one and weapon_one.two_hand) or (weapon_two and weapon_two.two_hand):
                if weapon_one and weapon_one.two_hand:
                    self.inventory.append(weapon_one)
                    self.update_attack(weapon_one)
                    self.update_speed(weapon_one)
                elif weapon_two and weapon_two.two_hand:
                    self.inventory.append(weapon_two)
                    self.update_attack(weapon_two)
                    self.update_speed(weapon_two)
            elif weapon_one and weapon_two:
                self.inventory.append(weapon_one)
                self.inventory.append(weapon_two)
                self.update_attack(weapon_one)
                self.update_attack(weapon_two)
                self.update_speed(weapon_one)
                self.update_speed(weapon_two)

    def update_attack(self, weapon):
        self.attack += weapon.damage

    def update_speed(self, item):
        self.speed += item.speed
        if self.speed < 3:
            self.speed = 3

    def update_defense(self, armor):
        self.defense += armor.defense

    def __repr__(self):
        return f"The {self.name} has {self.health} health, {self.attack} attack, {self.defense} defense, and {self.speed} speed. {self.inventory}"

def monster_selection(difficulty):
    enemy_map = {1: {
                    "Green Slime": {
                            "health": 3, 
                            "attack": 2, 
                            "defense": 3,
                            "speed": 3
                        }, 
                    "Red Slime": {
                            "health": 4, 
                            "attack": 3, 
                            "defense": 3,
                            "speed": 3
                        },
                    "Silver Slime": {
                            "health": 5, 
                            "attack": 4, 
                            "defense": 3,
                            "speed": 3
                        },
                    "Golden Slime": {
                            "health": 10, 
                            "attack": 5, 
                            "defense": 3,
                            "speed": 3
                        }},
                2: {
                    "Green Goblin": {
                            "health": 7,
                            "attack": 3,
                            "defense": 3,
                            "speed": 3
                        },
                    "Red Goblin": {
                            "health": 9,
                            "attack": 3,
                            "defense": 3,
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