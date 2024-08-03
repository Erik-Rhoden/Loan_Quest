from battle import path_difficulty, battle
from monster import monster_selection
from shop import *

def menu_selection(hero):
    while True:
        if hero.exit_game:
            break

        print("\n--------------")
        print(f"Current location: {hero.location}\n")
        opt_frmt = "|--Travel-(t)| |--Inventory-(i)| |--Stats-(st)| |--Exit-(x)|"
        choice = input(f"What would you like to do next?\n{opt_frmt}\n")
        print("--------------")
        
        if choice == 'x':
            print("Exiting the game. Farewell, hero!")
            print("--------------")
            hero.exit_game = True
            break
        elif choice == "i":
            print("--------------")
            hero.inventory_options()
            print("--------------")
        elif choice == 't':
            travel(hero)
        elif choice == 'st':
            display_stats(hero)
        else:
            print(f"Invalid entry. Please try again.")

def travel(hero):
    locations = {
        "s": "Shop",
        "c": "Center of Town",
        "e": "Edge of Town",
        "p": "Slime Plains",
        "g": "Goblin Forest",
        "o": "Orc Valley"
    }
    loc_frmt = "|--Shop-(s)| |--Center of Town-(c)| |--Edge of Town-(e)| |--Slime Plains-(p)| |--Goblin Forest-(g)| |--Orc Valley-(o)|"
    exit = "|--Exit-(x)|"
    while True:
        location_choice = input(f"Where would you like to go next or 'x' to exit to main menu?\n{loc_frmt}\n{exit}\n").lower()
        if location_choice == 'x':
            break

        if location_choice in locations:
            hero.location = locations[location_choice]
            if location_choice in ["s", "c", "e"]:
                if location_choice == 's':
                    open_shop(hero)
            else:
                difficulty = path_difficulty(hero.location)
                monster = monster_selection(difficulty)
                if hero.health > 0:
                    battle(hero, monster)
                    if hero.exit_game:
                        break
                    print("--------------\n")
                else:
                    print("Game Over!")
                    hero.exit_game = True
        else:
            print(f"Invalid entry. Please try again.")

def display_stats(hero):
    print(f"\n|--{hero.name} - Level: {hero.level}--|")
    print(hero.__repr__())
    print("--------------")
    if not hero.equipped:
        print("No items equipped!")
        print("--------------")
    else:
        print("|-Equipped Items-|")
        for index, item in enumerate(hero.equipped):
            print(f"{index + 1}. {item}")
        print("--------------")
        if hero.inventory:
            print("|-Inventory-|")
            hero.inventory_list()
            print("--------------")
        hero.print_slots_status()
    print("|--Complete--|")

def open_shop(hero):
    shop = Shop()
    while True:
        shop_options = "|--Buy-(b)| |--Sell-(s)| |--Exit-(x)|"
        print("--------------")
        shop_choice = input(f"Would you like to see our offerings or sell your goods?\n{shop_options}\n")
        print("--------------")
        if shop_choice == 'x': #return to main window
            break
        if shop_choice == 'b':
            while True:
                shop_list = []
                for key, item in enumerate(shop.inventory):
                    shop_list.append(item)
                    print(f"{key + 1}. {item}")
                print(f"\nYour gold: {round(hero.gold, 1):.1f}")
                print("--------------")
                purchase_choice = input("Enter the number next to the item you would like to purchase or 'q' to quit. ")
                print("--------------")
                if purchase_choice.lower() == 'q': #return to main shop window
                    break
                try:
                    purchase_choice = int(purchase_choice)
                    if 0 < purchase_choice <= len(shop_list):
                        item = shop_list[purchase_choice - 1]
                        if item.value <= hero.gold:
                            hero.gold -= item.value
                            item.value = int(item.value / 4)
                            hero.inventory.append(item)
                            shop.inventory.remove(item)
                            shop_list.remove(item)
                        else:
                            print("--------------")
                            print("You do not have enough gold")
                            print("--------------")
                    else:
                        print("Invalid choice. Please try again.")
                except ValueError:
                    print("Please enter a valid choice.")
                    print("--------------")
        if shop_choice == 's':
            while True:
                for key, item in enumerate(hero.inventory):
                    print(f"{key + 1}. {item}")
                if not hero.inventory:
                    print("Your inventory is empty.")
                    print("--------------")
                print(f"\nYour gold: {round(hero.gold, 1):.1f}")
                print("--------------")
                sell_choice = input("Enter the number next to the item you would like to sell or 'q' to quit. ")
                print("--------------")
                if sell_choice.lower() == 'q': #return to main shop window
                    break
                try:
                    sell_choice = int(sell_choice)
                    if 0 < sell_choice <= len(hero.inventory):
                        item = hero.inventory[sell_choice - 1]
                        hero.gold += item.value
                        hero.inventory.remove(item)
                    else:
                        print("Invalid choise. Please try again.")
                except ValueError:
                    print("Please enter a valid choice.")
                    print("--------------")