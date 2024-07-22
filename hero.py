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
        self.inventory = [Weapon("Stick", "Weapon", 0, 2, False)]
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
        while True:
            if not self.inventory:
                if self.equipped:
                    print("|--Equipped Items--|")
                    self.get_equipped_list()
                    self.inventory_options()
                elif not self.equipped:
                    print("Inventory is empty and nothing equipped")
                    break
            else:
                self.inventory_options()
                break

    def inventory_options(self):
        print("|--Inventory--|")
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
        choice = input("\nWould you like to equip 'e' an item, unequip 'u' equipment, drop 'd' an item or quit 'q' selection? ")
        if choice.lower() == 'q':
            print("Exiting the inventory menu.\n")
            return
        elif choice == "e":
            self.equip_item()
        elif choice == 'u':
            self.unequip_items()
        elif choice == 'd':
            self.remove_items()

    def remove_items(self):
        while True:
            print("\nThe following items are available to be removed...")
            print("--------------")
            self.inventory_list = self.get_inventory_list()
            if not self.inventory_list:
                print("Nothing to remove.")
                break
            print("--------------")
            choice = input("\nEnter the number of the item you want to remove (or 'q' to quit): ")
            if choice.lower() == 'q':
                print("\nExiting the remove menu.\n")
                break
            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= len(self.inventory_list):
                    index, item_to_remove = self.inventory_list[choice - 1]
                    self.inventory.pop(index)
                    print(f"Removed {item_to_remove.name}.")
                else:
                    print("--------------")
                    print(f"Invalid entry. Please try again.")
                    print("--------------")

    def get_inventory_list(self):
        self.inventory_list = []
        for index, item in enumerate(self.inventory):
            self.inventory_list.append((index, item))
            if isinstance(item, Potion):
                print(f"{len(self.inventory_list)}. {item.name} ({item.type}) - {'Healing: ' + str(item.heal)}, 'Value': {item.value} gold")
            elif isinstance(item, Weapon) or isinstance(item, Armor):
                print(f"{len(self.inventory_list)}. {item.name} ({item.type}) - {'Damage: ' + str(item.damage) if isinstance(item, Weapon) else 'Defense: ' + str(item.defense)}, Value: {item.value} gold")
            elif isinstance(item, Item):
                print(f"{len(self.inventory_list)}. {item.name} ({item.type}) - 'Value': {item.value} gold")
        return self.inventory_list

    def get_equip_list(self):
        self.equip_list = []
        for index, item in enumerate(self.inventory):
            if isinstance(item, Weapon) or isinstance(item, Armor):
                self.equip_list.append((index, item))
                print(f"{len(self.equip_list)}. {item.name} ({item.type}) - {'Damage: ' + str(item.damage) if isinstance(item, Weapon) else 'Defense: ' + str(item.defense)}, Value: {item.value} gold")
        return self.equip_list
            
    def equip_item(self):
        while True:
            print("\nThe following items are available...")
            print("--------------")
            self.equip_list = self.get_equip_list()
            if not self.equip_list:
                print("Nothing to equip.")
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
                        self.print_slots_status()
                    else:
                        print(f"{item_to_equip.name} failed to equip! Equipment slot is full!")
                        while True:
                            unequip_choice = input("Would you like to un-equip an item? (y/n): ")
                            if unequip_choice == "y":
                                self.unequip_items()
                            elif unequip_choice == "n":
                                break
                            else:
                                print("Invalid entry. Please try again.")
            
                else:
                    print("Invalid choice. Please select a number from the list.")
            else:
                print("Invalid input. Please enter a number or 'q' to quit.")

    def get_equipped_list(self):
        for index, item in enumerate(self.equipped):
            print(f"{index + 1}. {item}")

    def unequip_items(self):
        while True:
            print("\nThe following items are available to remove...")
            print("--------------")
            self.get_equipped_list()
            if not self.equipped:
                print("Nothing to remove.")
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
                    self.print_slots_status()
                else:
                    print("Failed to remove! Enter a valid number!")            

    def slot_status(self, slot):
        return '0' if not slot else 'X'

    def print_slots_status(self):
        print("|-Weapon slots-|")
        print(f"Main hand: {self.slot_status(self.main_hand)}, Off hand: {self.slot_status(self.off_hand)}")
        print("|-Armor slots-|")
        slots = ['chest', 'feet', 'legs', 'head']
        print(", ".join(f"{slot.capitalize()}: {self.slot_status(getattr(self, slot))}" for slot in slots))

    def free_slot(self, equipped_item):
        if equipped_item.type == "Weapon":
            if equipped_item.two_hand:
                if equipped_item in self.main_hand and equipped_item in self.off_hand:
                    self.main_hand = []
                    self.off_hand = []
                    self.decrease_attack(equipped_item)
                    print(f"{equipped_item.name} unequipped")
            else:
                if equipped_item in self.main_hand:
                    self.main_hand = []
                    print(f"{equipped_item.name} in main-hand unequipped")
                else:
                    self.off_hand = []
                    print(f"{equipped_item.name} in off-hand unequipped")
                self.decrease_attack(equipped_item)
                
        elif equipped_item.type == "Armor":
            if equipped_item.body_type == "Legs":
                self.legs = []
                print("Legs armor unequipped")
            elif equipped_item.body_type == "Head":
                self.head = []
                print("Head armor unequipped")
            elif equipped_item.body_type == "Feet":
                self.feet = []
                print("Feet armor unequipped")
            elif equipped_item.body_type == "Chest":
                self.chest = []
                print("Chest armor unequipped")
            elif equipped_item.body_type == "Off-Hand":
                self.off_hand = []
                print("Off-Hand armor unequipped")
            self.decrease_defense(equipped_item)

    def slot_availability(self, item_to_equip):
        if item_to_equip.type == "Weapon" and (len(self.main_hand) == 0 or len(self.off_hand) == 0):
            if item_to_equip.two_hand:
                if len(self.main_hand) == 0 and len(self.off_hand) == 0:
                    self.main_hand.append(item_to_equip)
                    self.off_hand.append(item_to_equip)
                    self.add_attack(item_to_equip)
                    print(f"{item_to_equip} equipped")
                    return True
                else:
                    print("Cannot equip a two-handed weapon unless both hands are free.")
                    return False
            else:
                if len(self.main_hand) == 0:
                    self.main_hand.append(item_to_equip)
                    self.add_attack(item_to_equip)
                    print(f"{item_to_equip} equipped")
                    return True
                elif len(self.off_hand) == 0:
                    self.off_hand.append(item_to_equip)
                    self.add_attack(item_to_equip)
                    print(f"{item_to_equip} equipped")
                    return True
                else:
                    print("Both hands have weapons.")
                    return False
        
        elif item_to_equip.type == "Armor":
            if item_to_equip.body_type == "Legs":
                if len(self.legs) == 0:
                    self.legs.append(item_to_equip)
                    self.add_defense(item_to_equip)
                    print(f"{item_to_equip} equipped")
                    return True
                else:
                    print("Legs slot is already occupied.")
                    return False
            elif item_to_equip.body_type == "Head":
                if len(self.head) == 0:
                    self.head.append(item_to_equip)
                    self.add_defense(item_to_equip)
                    print(f"{item_to_equip} equipped")
                    return True
                else:
                    print("Head slot is already occupied.")
                    return False
            elif item_to_equip.body_type == "Feet":
                if len(self.feet) == 0:
                    self.feet.append(item_to_equip)
                    self.add_defense(item_to_equip)
                    print(f"{item_to_equip} equipped")
                    return True
                else:
                    print("Feet slot is already occupied.")
                    return False
            elif item_to_equip.body_type == "Chest":
                if len(self.chest) == 0:
                    self.chest.append(item_to_equip)
                    self.add_defense(item_to_equip)
                    print(f"{item_to_equip} equipped")
                    return True
                else:
                    print("Chest slot is already occupied.")
                    return False
            elif item_to_equip.body_type == "Off-Hand":
                if len(self.off_hand) == 0:
                    self.off_hand.append(item_to_equip)
                    self.add_defense(item_to_equip)
                    print(f"{item_to_equip} equipped")
                    return True
                else:
                    print("Off-Hand slot is already occupied.")
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
        self.defense -= item.defense
    
    def __repr__(self):
        return f"Health: {self.health}\nAttack: {self.attack}\nDefense: {self.defense}\nSpeed: {self.speed}\nGold: {self.gold}"
    
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