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
    location_choice = input(f"Where would you like to go next?\n{loc_frmt}\n").lower()

    if location_choice in locations:
        hero.location = locations[location_choice]
        if location_choice in ["s", "c", "e"]:
            if location_choice == 's':
                open_shop(hero)
        else:
            difficulty = path_difficulty(hero.location)
            monster = monster_selection(difficulty)
            battle(hero, monster)
            if hero.health > 0:
                menu_selection(hero)
            else:
                print("Game Over!")
                hero.exit_game = True
    else:
        print(f"Invalid entry. Please try again.")

def display_stats(hero):
    print(f"\n|--{hero.name}--|")
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
        hero.print_slots_status()
    print("|--Complete--|")

def open_shop(hero):
    shop = Shop()
    shop_options = "|--Buy-(b)| |--Sell-(s)|"
    print("--------------")
    shop_choice = input(f"Would you like to see our offerings or sell your goods?\n{shop_options}\n")
    print("--------------")
    if shop_choice == 'b':
        while True:
            shop_list = []
            for key, item in enumerate(shop.inventory):
                shop_list.append(item)
                print(f"{key + 1}. {item}")
            print(f"\nYour gold: {hero.gold}")
            print("--------------")
            purchase_choice = input("Enter the number next to the item you would like to purchase or 'q' to quit. ")
            print("--------------")
            if purchase_choice.lower() == 'q':
                break
            try:
                purchase_choice = int(purchase_choice)
                if 0 < purchase_choice <= len(shop_list):
                    if shop_list[purchase_choice - 1].value <= hero.gold:
                        hero.gold -= shop_list[purchase_choice - 1].value
                        hero.inventory.append(shop_list[purchase_choice - 1])
                        shop.inventory.remove(shop_list[purchase_choice - 1])
                        shop_list.remove(shop_list[purchase_choice - 1])
                    else:
                        print("--------------")
                        print("You do not have enough gold")
                        print("--------------")
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a valid choice.")
                print("--------------")      

            