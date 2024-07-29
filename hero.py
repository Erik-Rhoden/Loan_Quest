import time
from loot import *
from menu import menu_selection, open_shop

class Hero():
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
        self.backpack = []
        self.location = "Center of Town"
        self.gold = 0.0
        self.inventory = [Weapon("Stick", "Weapon", 0, 2, False)]
        self.equip_list = []
        self.equipped = []
        self.max_inv_size = 8
        self.exit_game = False

    def get_health(self):
        return self.health

    def deal_damage(self, target):
        damage = int(round(self.attack * (1 - target.defense / (target.defense + 50)), 0))
        target.health -= damage
        print(f"{target.name} has taken {damage} damage!")

    def heal_self(self):
        heal_amount = 0
        while True:
            for index, item in enumerate(self.inventory):
                if hasattr(item, 'heal'):
                    print(f"{index + 1}. {item.name} - Heal: {item.heal}")
            print("--------------")
            heal_choice = input("Which potion would you like to use or 'q' to quit? ")
            if heal_choice.lower() == 'q':
                print("\nExiting the remove menu.\n")
                print("--------------")
                break
            if heal_choice.isdigit():
                heal_choice = int(heal_choice)
                heal_amount = item.heal
                if 1 <= heal_choice <= len(self.inventory):
                    if self.health + self.inventory[heal_choice - 1].heal >= self.max_hp:
                        self.health = self.max_hp
                        self.inventory.remove(item)
                        break
                    elif self.health + self.inventory[heal_choice - 1].heal < self.max_hp:
                        self.health += self.inventory[heal_choice - 1].heal
                        self.inventory.remove(item)
                        break
        return heal_amount

    def get_loot(self, monster):
        print("--------------")
        print(f"You defeated {monster.name}!\n")
        if not monster.inventory and monster.gold == 0:
            print(f"Too bad! The {monster.name} had nothing!")
            return
        elif not monster.inventory and monster.gold:
            self.gold += monster.gold
            print(f"The {monster.name} had {monster.gold} gold!")
        elif monster.inventory:
            print("--------------")
            print(f"{monster.name} dropped {monster.gold} gold!")
            print(f"{monster.name} dropped the following items:")
            print("--------------")
            for index, item in enumerate(monster.inventory):
                print(f"{index + 1}. {item}")
            if self.max_inv_size - len(self.inventory) == 0:
                self.inventory_full()
            else:
                print(f"\nYour inventory has {self.max_inv_size - len(self.inventory)}/{self.max_inv_size} slots available.")
            while len(self.inventory) < self.max_inv_size and monster.inventory:
                for index, item in enumerate(monster.inventory):
                    add_to_inv = input(f"Would you like to add {item.name} to your inventory? (y/n): ").lower()
                    if add_to_inv == "y":
                        self.inventory.append(item)
                        monster.inventory.remove(item)
                        break
                    elif add_to_inv == "n":
                        monster.inventory.remove(item)
                    else:
                        print("Invalid response. Please try again!")
                if len(self.inventory) == self.max_inv_size:
                    if monster.inventory:
                        self.inventory_full()
                        choice = input("Would you like to remove an item? (y/n): ")
                        if choice == "y":
                            self.remove_items()
                        if choice == "n":
                            break
                    else:
                        self.inventory_full()

    def inventory_full(self):
        print("--------------\n")
        print("\nYour inventory is full!")
        print("Remove items or sell them at the Shop!")
        print("--------------\n")

    def inventory_options(self):
        while True:
            if self.equipped:
                print("|--Equipped Items--|")
                self.get_equipped_list()
                print("--------------\n")
            print("|--Inventory--|")
            if not self.inventory:
                print("(Empty)")
            else:
                self.get_inventory_list()
            print("--------------")
            choice = input("\nWould you like to equip 'e' an item, unequip 'u' equipment, heal 'h' yourself, drop 'd' an item or quit 'q' selection? ").lower()
            if choice == 'q':
                print("--------------")
                print("Returning to the main menu.")
                break
            elif choice == "e":
                self.equip_item()
            elif choice == 'u':
                self.unequip_items()
            elif choice == 'h':
                heal_amount = self.heal_self()
                print(f"{self.name} healed themselves for {heal_amount} HP")
            elif choice == 'd':
                self.remove_items()

    def remove_items(self):
        while True:
            print("\nThe following items are available to be removed...")
            print("--------------")
            if not self.inventory:
                print("Nothing to remove.")
                print("--------------\n")
                break
            self.get_inventory_list()
            print("--------------")
            choice = input("\nEnter the number of the item you want to remove (or 'q' to quit): ")
            if choice.lower() == 'q':
                print("\nExiting the remove menu.\n")
                print("--------------")
                break
            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= len(self.inventory):
                    item_to_remove = self.inventory[choice - 1]
                    self.inventory.remove(item_to_remove)
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

    def get_equip_list(self):
        self.equip_list = []
        for index, item in enumerate(self.inventory):
            if isinstance(item, Weapon) or isinstance(item, Armor):
                self.equip_list.append((index, item))
                print(f"{len(self.equip_list)}. {item.name} ({item.type}) - {'Damage: ' + str(item.damage) if isinstance(item, Weapon) else 'Defense: ' + str(item.defense)}, Value: {item.value} gold")
            if isinstance(item, Item) and item.type == 'Backpack':
                self.equip_list.append((index, item))
                print(f"{len(self.equip_list)}. {item.name} ({item.type}) - {'Capacity: ' + str(item.capacity)}, Value: {item.value} gold")
        return self.equip_list
            
    def equip_item(self):
        while True:
            print("\nThe following items are available...")
            print("--------------")
            self.equip_list = self.get_equip_list()
            if self.equip_list:
                print("--------------")
            if not self.equip_list:
                print("Nothing to equip.")
                print("--------------")
                break
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
                        print("--------------")
                        self.print_slots_status()
                        print("--------------")
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
            if len(self.inventory) < self.max_inv_size:
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
            else:
                print("--------------")
                print("Inventory is full! You must drop an item first!")
                print("--------------")     
                break

    def slot_status(self, slot):
        return 'Open' if not slot else 'X'

    def print_slots_status(self):
        print("|-Weapon slots-|")
        print(f"Main hand: {self.slot_status(self.main_hand)}, Off hand: {self.slot_status(self.off_hand)}")
        print("|-Armor slots-|")
        slots = ['chest', 'feet', 'legs', 'head', 'backpack']
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
        if item_to_equip.type == "Weapon":
            if (len(self.main_hand) == 0 or len(self.off_hand) == 0):
                if item_to_equip.two_hand:
                    if len(self.main_hand) == 0 and len(self.off_hand) == 0:
                        self.main_hand.append(item_to_equip)
                        self.off_hand.append(item_to_equip)
                        self.add_attack(item_to_equip)
                        self.update_speed(item_to_equip)
                        print(f"{item_to_equip} equipped")
                        return True
                    else:
                        print("Cannot equip a two-handed weapon unless both hands are free.")
                        return False
                else:
                    if len(self.main_hand) == 0:
                        self.main_hand.append(item_to_equip)
                        self.add_attack(item_to_equip)
                        self.update_speed(item_to_equip)
                        print(f"{item_to_equip} equipped")
                        return True
                    elif len(self.off_hand) == 0:
                        self.off_hand.append(item_to_equip)
                        self.add_attack(item_to_equip)
                        self.update_speed(item_to_equip)
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
                    self.update_speed(item_to_equip)
                    print(f"{item_to_equip} equipped")
                    return True
                else:
                    print("Legs slot is already occupied.")
                    return False
            elif item_to_equip.body_type == "Head":
                if len(self.head) == 0:
                    self.head.append(item_to_equip)
                    self.add_defense(item_to_equip)
                    self.update_speed(item_to_equip)
                    print(f"{item_to_equip} equipped")
                    return True
                else:
                    print("Head slot is already occupied.")
                    return False
            elif item_to_equip.body_type == "Feet":
                if len(self.feet) == 0:
                    self.feet.append(item_to_equip)
                    self.add_defense(item_to_equip)
                    self.update_speed(item_to_equip)
                    print(f"{item_to_equip} equipped")
                    return True
                else:
                    print("Feet slot is already occupied.")
                    return False
            elif item_to_equip.body_type == "Chest":
                if len(self.chest) == 0:
                    self.chest.append(item_to_equip)
                    self.add_defense(item_to_equip)
                    self.update_speed(item_to_equip)
                    print(f"{item_to_equip} equipped")
                    return True
                else:
                    print("Chest slot is already occupied.")
                    return False
            elif item_to_equip.body_type == "Off-Hand":
                if len(self.off_hand) == 0:
                    self.off_hand.append(item_to_equip)
                    self.add_defense(item_to_equip)
                    self.update_speed(item_to_equip)
                    print(f"{item_to_equip} equipped")
                    return True
                else:
                    print("Off-Hand slot is already occupied.")
                    return False
                
        elif item_to_equip.type == "Backpack":
            if len(self.backpack) == 0:
                self.backpack.append(item_to_equip)
                self.max_inv_size += item_to_equip.capacity
                print(f"{item_to_equip} equipped")
                return True

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

    def update_speed(self, item):
        self.speed += item.speed
    
    def __repr__(self):
        return f"Health: {self.health}/{self.max_hp}\nAttack: {self.attack}\nDefense: {self.defense}\nSpeed: {self.speed}\nMax Inventory Size: {self.max_inv_size}\nGold: {round(self.gold, 1):.1f}"