import time
from loot import *

class Hero():
    def __init__(self, name, health, attack, defense, speed):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.main_hand = []
        self.off_hand = []
        self.head = []
        self.legs = []
        self.feet = []
        self.chest = []
        self.location = "Center of Town"
        self.gold = 0
        self.inventory = []
        self.equip_list = []
        self.equipped = []
        self.max_inv_size = 8

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

    def get_loot(self, monster):
        print(f"You defeated {monster.name}!\n")
        if not monster.inventory:
            print(f"Too bad! The {monster.name} had nothing!")
            return
        if monster.gold:
            self.gold += monster.gold
        print(f"{monster.name} dropped the following items:")
        for index, item in enumerate(monster.inventory):
            print(f"{index + 1}. {item}")
        print(f"\nYour inventory has {self.max_inv_size - len(self.inventory)}/{self.max_inv_size} slots available.")
        while len(self.inventory) <= self.max_inv_size and monster.inventory:
            for index, item in enumerate(monster.inventory):
                add_to_inv = input(f"Would you like to add {item} to your inventory? (y/n): ")
                if add_to_inv.lower() == "y":
                    self.inventory.append(item)
                    monster.inventory.remove(item)
                    break
                elif add_to_inv.lower() == "n":
                    monster.inventory.remove(item)
                else:
                    print("Invalid response. Please try again!")
            if len(self.inventory) == self.max_inv_size:
                print("\nYour inventory is full!")
                print("Remove items or sell them at the Shop!")
                break
            
    def search_inventory(self):
        if len(self.inventory) == 0:
            print("Inventory is Empty")
            print("--------------")
            return
        for item in self.inventory:
            if isinstance(item, Weapon):
                print(f"{item.name}({item.type}) - Damage: {item.damage}, Value: {item.value}")
            elif isinstance(item, Armor):
                print(f"{item.name}({item.type}) - Defense: {item.defense}, Value: {item.value}")
            elif isinstance(item, Potion):
                print(f"{item.name}({item.type}) - Healing: {item.heal}, Value: {item.value}")
            else:
                print(f"{item.name}({item.type}) - Value: {item.value}")
        print("--------------")
        choice = input("\nWould you like to equip 'e' an item, drop 'd' an item or quit 'q' selection? ")
        if choice.lower() == 'q':
            print("Exiting the inventory menu.")
            return
        if choice is "e":
            self.equip_item()
        #add choice "d" logic here

    def get_equip_list(self):
        self.equip_list = []
        for index, item in enumerate(self.inventory):
            if isinstance(item, Weapon) or isinstance(item, Armor):
                self.equip_list.append((index, item))
                print(f"{len(self.equip_list)}. {item.name} ({item.type}) - {'Damage: ' + str(item.damage) if isinstance(item, Weapon) else 'Defense: ' + str(item.defense)}, Value: {item.value} gold")
            
    def equip_item(self):
        while True:
            print("\nThe following items are available...")
            print("--------------")
            if not self.get_equip_list():
                print("Nothing to equip.")
                break
            else:
                self.get_equip_list()
            print("--------------")
            choice = input("\nEnter the number of the item you want to equip (or 'q' to quit): ")
            if choice.lower() == 'q':
                print("Exiting the equip menu.")
                break
            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= len(self.equip_list):
                    index, item_to_equip = self.equip_list[choice - 1]
                    if self.slot_availability(item_to_equip):
                        self.equipped.append(item_to_equip)
                        self.inventory.pop(index)
                        self.equip_list.pop(choice - 1)
                        print(f"Equipped {item_to_equip.name}.")
                        self.print_slots_status()
                    else:
                        print(f"{item_to_equip.name} failed to equip! Equipment slot is full!")
                        while True:
                            unequip_choice = input("Would you like to un-equip an item? (y/n): ")
                            if unequip_choice == "y":
                                self.unequip_items()
                                break
                            elif unequip_choice == "n":
                                break
                            else:
                                print("Invalid entry. Please try again.")
            
                else:
                    print("Invalid choice. Please select a number from the list.")
            else:
                print("Invalid input. Please enter a number or 'q' to quit.")

    def unequip_items(self):
        while True:
            print("\nThe following items are available...")
            print("--------------")
            for index, item in enumerate(self.equipped):
                print(f"{index + 1}. {item}")
            print("--------------")
            choice = input("\nEnter the number of the item you want to remove (or 'q' to quit): ")
            if choice.lower() == 'q':
                print("Exiting the equip menu.")
                break
            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= len(self.equipped):
                    equipped_item = self.equipped[choice - 1]
                    self.free_slot(equipped_item)
                    self.equipped.remove(equipped_item)
                    self.inventory.append(equipped_item)
                    print(f"Removed {equipped_item.name}.")
                    self.print_slots_status()
                else:
                    print("Failed to remove! Enter a valid number!")            

    def print_slots_status(self):
        print("Weapon slots")
        print(f"Main hand: {len(self.main_hand)}, Off hand: {len(self.off_hand)}")
        print("Armor slots")
        print(f"Chest: {len(self.chest)}, Feet: {len(self.feet)}, Legs: {len(self.legs)}, Head: {len(self.head)}, Off hand: {len(self.off_hand)}")

    def free_slot(self, equipped_item):
        if equipped_item.type == "Weapon":
            if equipped_item.two_hand:
                if equipped_item in self.main_hand and equipped_item in self.off_hand:
                    self.main_hand = []
                    self.off_hand = []
                    self.decrease_attack(equipped_item)
                    print("TWO HAND WEAPON UNEQUIPPED")
                    return True
                else:
                    print("Two-handed weapon is not equipped.")
                    return False
            else:
                if equipped_item in self.main_hand:
                    self.main_hand = []
                    self.decrease_attack(equipped_item)
                    print("One-handed weapon in main hand unequipped")
                    return True
                elif equipped_item in self.off_hand:
                    self.off_hand = []
                    self.decrease_attack(equipped_item)
                    print("One-handed weapon in off hand unequipped")
                    return True
                else:
                    print("One-handed weapon is not equipped.")
                    return False
                
        elif equipped_item.type == "Armor":
            if equipped_item.body_type == "Legs":
                if equipped_item in self.legs:
                    self.legs = []
                    self.decrease_defense(equipped_item)
                    print("Legs armor unequipped")
                    return True
                else:
                    print("Legs armor is not equipped.")
                    return False
            elif equipped_item.body_type == "Head":
                if equipped_item in self.head:
                    self.head = []
                    self.decrease_defense(equipped_item)
                    print("Head armor unequipped")
                    return True
                else:
                    print("Head armor is not equipped.")
                    return False
            elif equipped_item.body_type == "Feet":
                if equipped_item in self.feet:
                    self.feet = []
                    self.decrease_defense(equipped_item)
                    print("Feet armor unequipped")
                    return True
                else:
                    print("Feet armor is not equipped.")
                    return False
            elif equipped_item.body_type == "Chest":
                if equipped_item in self.chest:
                    self.chest = []
                    self.decrease_defense(equipped_item)
                    print("Chest armor unequipped")
                    return True
                else:
                    print("Chest armor is not equipped.")
                    return False
            elif equipped_item.body_type == "Off-Hand":
                if equipped_item in self.off_hand:
                    self.off_hand = []
                    self.decrease_defense(equipped_item)
                    print("Off-Hand armor unequipped")
                    return True
                else:
                    print("Off-Hand armor is not equipped.")
                    return False
            else:
                print(f"{equipped_item.body_type} slot is not recognized.")
                return False

        print("Item type not recognized.")
        return False

        
    def slot_availability(self, item_to_equip):
        if item_to_equip.type == "Weapon" and (len(self.main_hand) == 0 or len(self.off_hand) == 0):
            if item_to_equip.two_hand:
                if len(self.main_hand) == 0 and len(self.off_hand) == 0:
                    self.main_hand.append(item_to_equip)
                    self.off_hand.append(item_to_equip)
                    self.add_attack(item_to_equip)
                    print("TWO HAND EQUIPPED")
                    return True
                else:
                    print("Cannot equip a two-handed weapon unless both hands are free.")
                    return False
            else:
                if len(self.main_hand) == 0:
                    self.main_hand.append(item_to_equip)
                    self.add_attack(item_to_equip)
                    print("ONE HAND EQUIPPED")
                    return True
                elif len(self.off_hand) == 0:
                    self.off_hand.append(item_to_equip)
                    self.add_attack(item_to_equip)
                    print("ONE HAND EQUIPPED")
                    return True
                else:
                    print("Both hands have weapons.")
                    return False
        
                
        elif item_to_equip.type == "Armor":
            if item_to_equip.body_type == "Legs":
                if len(self.legs) == 0:
                    self.legs.append(item_to_equip)
                    self.add_defense(item_to_equip)
                    return True
                else:
                    print("Legs slot is already occupied.")
                    return False
            elif item_to_equip.body_type == "Head":
                if len(self.head) == 0:
                    self.head.append(item_to_equip)
                    self.add_defense(item_to_equip)
                    return True
                else:
                    print("Head slot is already occupied.")
                    return False
            elif item_to_equip.body_type == "Feet":
                if len(self.feet) == 0:
                    self.feet.append(item_to_equip)
                    self.add_defense(item_to_equip)
                    return True
                else:
                    print("Feet slot is already occupied.")
                    return False
            elif item_to_equip.body_type == "Chest":
                if len(self.chest) == 0:
                    self.chest.append(item_to_equip)
                    self.add_defense(item_to_equip)
                    return True
                else:
                    print("Chest slot is already occupied.")
                    return False
            elif item_to_equip.body_type == "Off-Hand":
                if len(self.off_hand) == 0:
                    self.off_hand.append(item_to_equip)
                    self.add_defense(item_to_equip)
                    return True
                else:
                    print("Off-Hand slot is already occupied.")
                    return False
            else:
                print(f"{item_to_equip.body_type} slot is not recognized.")
                return False

        print("Both hands are occupied.")
        return False
        
    def add_attack(self, item):
        self.attack += item.damage

    def decrease_attack(self, item):
        self.attack -= item.damage

    def add_defense(self, item):
        self.defense += item.defense

    def decrease_defense(self, item):
        self.attack -= item.defense
    
    def __repr__(self):
        return f"{self.name} has {self.health} health, {self.attack} attack, {self.defense} defense, {self.speed} speed, and {self.gold} gold."
    
def path_difficulty(choice):
    difficulty_map = [
        {'LEVEL': 1, 'AREA': "Slime Plains"},
        {'LEVEL': 2, 'AREA': "Goblin Forest"},
        {'LEVEL': 3, 'AREA': "Orc Valley"}
    ]
        
    while True:
        for entry in difficulty_map:
            if choice == entry['AREA']:
                chosen_difficulty = entry['LEVEL']
                area = entry['AREA']
                print(f"You've chosen {area}\n")
                return chosen_difficulty
        print("Invalid input. Please choose again.")

def battle(hero, monster):
    while hero.health > 0 and monster.health > 0:
        if hero.speed > monster.speed:
            hero.deal_damage(monster)
            if monster.health > 0:
                monster.deal_damage(hero)
        else:
            monster.deal_damage(hero)
            if hero.health > 0:
                hero.deal_damage(monster)
    if hero.health == 0:
        print(f"{monster.name} defeated {hero.name}!")
        return
    else:
        hero.get_loot(monster)