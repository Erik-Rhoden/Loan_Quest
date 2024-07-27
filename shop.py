import random
from loot import Item, Weapon, Armor, Potion

shop_map = {
        "potion": {
                "Half-Full Minor Health Potion": {
                    "Heal": 3,
                    "Value": 20
            },  "Minor Health Potion": {
                    "Heal": 5,
                    "Value": 40,
            },  "Half-Full Medium Health Potion": {
                    "Heal": 10,
                    "Value": 80,
            }
    },  "weapon": { 
                "Club": {
                    "Damage": 3,
                    "Speed": 0,
                    "Two-Hand": False,
                    "Value": 12
            },  "Dagger": {
                    "Damage": 5,
                    "Speed": 4,
                    "Two-Hand": False,
                    "Value": 20
            },  "Shortsword": {
                    "Damage": 10,
                    "Speed": 2,
                    "Two-Hand": False,
                    "Value": 32
            }
    },  "armor": {
                "Wool Shirt": {
                    "Defense": 1,
                    "Speed": 4,
                    "Body": "Chest",
                    "Value": 8
            },  "Wool Leggings": {
                    "Defense": 1,
                    "Speed": 4,
                    "Body": "Legs",
                    "Value": 8
            },  "Wool Cap": {
                    "Defense": 1,
                    "Speed": 4,
                    "Body": "Head",
                    "Value": 8
            },  "Leather Shoes": {
                    "Defense": 1,
                    "Speed": 2,
                    "Body": "Feet",
                    "Value": 12
            },  "Wooden Shield": {
                    "Defense": 8,
                    "Speed": 2,
                    "Body": "Off-Hand",
                    "Value": 20
            }  
    },  "misc": {
                "Backpack": {
                    "Capacity": 12,
                    "Value": 200
                }
    }
}

class Shop():
    def __init__(self):
        self.inventory = []
        self.get_inventory()

    def get_inventory(self):
        categories = ["weapon", "armor", "potion", "misc"]
        available_items = [random.choice(list(shop_map[category].items())) for category in categories]
        for item in available_items:
            item_name, item_properties = item
            if "Capacity" in item_properties:
                backpack = Item(item_name, "Backpack", item_properties['Value'], item_properties['Capacity'])
                self.inventory.append(backpack)
            if "Damage" in item_properties:
                weapon = Weapon(item_name, "Weapon", item_properties["Value"], item_properties["Damage"], item_properties["Speed"], item_properties["Two-Hand"])
                self.inventory.append(weapon)
            if "Defense" in item_properties:
                armor = Armor(item_name, "Armor", item_properties["Value"], item_properties["Defense"], item_properties["Speed"], item_properties["Body"])
                self.inventory.append(armor)
            if "Heal" in item_properties:
                potion = Potion(item_name, "Potion", item_properties["Value"], item_properties["Heal"])
                self.inventory.append(potion)