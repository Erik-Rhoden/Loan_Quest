import random
from loot import *
from menu import menu_selection, open_shop

class Hero():
    def __init__(self, name, health, attack, defense, speed):
        self.name = name
        self.health = health
        self.max_hp = health
        self.xp = 0
        self.level = 1
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
        self.location = "Shop"
        self.gold = 0.0
        self.inventory = [Weapon("Stick", "Weapon", 0, 2, False)]
        self.equip_list = []
        self.equipped = []
        self.max_inv_size = 8
        self.exit_game = False
        self.time = 0
        self.max_time = 168

    def time_logged(current_location, destination):
        destinations = ['Shop', 'Slime Plains', 'Goblin Forest', 'Orc Valley']
        difference = abs(destinations.index(current_location) - destinations.index(destination))
        if current_location != destination:
            time_past = difference * 0.25
            return time_past
        else:
            return 0.1

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

    def check_level(self):
        while True:
            current_level = self.level
            next_level_up = int(round(30 * (1.5 ** (current_level - 1))))
            if self.xp >= next_level_up:
                self.level += 1
                self.xp = 0
                print(f"Congratulations! {self.name} reached level {self.level}!")
                self.update_stats(current_level)
                self.health = self.max_hp
            else:
                break

    def update_stats(self, current_level):
        modifier = 1.2
        base_attack_increase = round((self.attack - self.get_attack_modifiers()) * modifier)
        base_defense_increase = round((self.defense - self.get_defense_modifiers()) * modifier)
        base_speed_increase = round((self.speed - self.get_speed_modifiers()) * modifier)
        self.max_hp = round(self.max_hp * modifier)
        self.attack += base_attack_increase - self.attack
        self.defense += base_defense_increase - self.defense
        self.speed += base_speed_increase - self.speed

    def get_attack_modifiers(self):
        modifier = 0
        for item in self.equipped:
            if hasattr(item, "Weapon"):
                modifier += item.damage
            elif hasattr(item, "Armor"):
                modifier += item.defense
        return modifier
    
    def get_defense_modifiers(self):
        modifier = 0
        for item in self.equipped:
            if hasattr(item, "Armor"):
                modifier += item.defense
        return modifier

    def get_speed_modifiers(self):
        modifier = 0
        for item in self.equipped:
            if hasattr(item, "Weapon") or hasattr(item, "Armor"):
                modifier += item.speed
        return modifier

    def heal_self(self):
        heal_amount = 0
        while True:
            healing_items = [(index, item) for index, item in enumerate(self.inventory) if hasattr(item, 'heal')]
            if not healing_items:
                print("No potions available")
                break
            for index, item in enumerate(self.inventory):
                if hasattr(item, 'heal'):
                    print(f"{index}. {item.name} - Heal: {item.heal}")
            print("--------------")
            heal_choice = input("Which potion would you like to use or 'q' to quit? ")
            if heal_choice.lower() == 'q':
                print("\nExiting the remove menu.\n")
                print("--------------")
                break
            if heal_choice.isdigit():
                heal_choice = int(heal_choice)
                if 1 <= heal_choice <= len(healing_items):
                    index, potion = healing_items[heal_choice -1]
                    heal_amount = potion.heal
                    if self.health + heal_amount >= self.max_hp:
                        self.health = self.max_hp
                    else:
                        self.health += heal_amount
                    self.inventory.pop(index)
                    break
        return heal_amount

    def get_loot(self, monster):
        print("--------------")
        print(f"You defeated {monster.name}!")
        if not monster.inventory and monster.gold == 0:
            print(f"Too bad! The {monster.name} had nothing!")
            return
        elif not monster.inventory and monster.gold:
            self.gold += monster.gold
            print(f"The {monster.name} had {monster.gold} gold!")
            self.get_loot_helper(monster, [])
        elif len(monster.inventory) < 3:
            self.get_loot_helper(monster, monster.inventory)
        elif len(monster.inventory) > 2 and monster.gold:
            available_items = monster.get_inventory_list()
            random.shuffle(available_items)
            limit = round(len(available_items) / 2)
            selected_items = available_items[:limit]
            self.get_loot_helper(monster, selected_items)

    def get_loot_helper(self, monster, inventory):
        print("--------------")
        print(f"{monster.name} dropped {monster.gold} gold!")
        if monster.gold > 0:
            self.gold += monster.gold
        if not inventory:
            print("No items dropped.")
            return

        print(f"{monster.name} dropped the following items:")
        print("--------------")
        for index, item in enumerate(inventory):
            print(f"{index + 1}. {item}")
        print(f"\nYour inventory has {self.max_inv_size - len(self.inventory)}/{self.max_inv_size} slots available.")
        while len(self.inventory) < self.max_inv_size and inventory:
            for index, item in enumerate(inventory):
                add_to_inv = input(f"Would you like to add {item.name} to your inventory? (y/n): ").lower()
                if add_to_inv == "y":
                    self.inventory.append(item)
                    inventory.remove(item)
                    break
                elif add_to_inv == "n":
                    inventory.remove(item)
                else:
                    print("Invalid response. Please try again!")

        if len(self.inventory) == self.max_inv_size and inventory:
            while inventory:
                choice = input("\nYour inventory is full. Would you like to remove an item? (y/n): ")
                
                if choice == "y":
                    self.remove_items()
                elif choice == "n":
                    print("You chose to discard the loot item.")
                    break
                else:
                    print("Invalid choice. Please enter 'y' or 'n'.")
                
                if len(self.inventory) < self.max_inv_size:
                    for index, item in enumerate(inventory):
                        add_to_inv = input(f"Would you like to add {item.name} to your inventory? (y/n): ").lower()
                        if add_to_inv == "y":
                            self.inventory.append(item)
                            inventory.remove(item)
                            break
                        elif add_to_inv == "n":
                            inventory.remove(item)
                        else:
                            print("Invalid response. Please try again!")
        elif not inventory:
            print("No more items to add.")

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
                self.inventory_list()
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
            self.inventory_list()
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

    def inventory_list(self):
        inventory_details = []
        for index, item in enumerate(self.inventory):
            inventory_details.append((index, item))
            if isinstance(item, Potion):
                print(f"{index + 1}. {item.name} ({item.type}) - Healing: {item.heal}, Value: {item.value} gold")
            elif isinstance(item, Weapon):
                print(f"{index + 1}. {item.name} ({item.type}) - Damage: {item.damage}, Value: {item.value} gold")
            elif isinstance(item, Armor):
                print(f"{index + 1}. {item.name} ({item.type}) - Defense: {item.defense}, Value: {item.value} gold")
            elif isinstance(item, Item):
                print(f"{index + 1}. {item.name} ({item.type}) - Value: {item.value} gold")

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
                                break
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
            print("\nThe following items are available to unequip...")
            print("--------------")
            self.get_equipped_list()
            if not self.equipped:
                print("Nothing to remove.")
                print("--------------")
            choice = input("\nEnter the number of the item you want to unequip (or 'q' to quit): ")
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
        if self.speed < 3:
            self.speed = 3
    
    def __repr__(self):
        return f"Health: {round(self.health)}/{self.max_hp}\nAttack: {self.attack}\nDefense: {self.defense}\nSpeed: {self.speed}\nMax Inventory Size: {self.max_inv_size}\nGold: {round(self.gold, 1):.1f}"