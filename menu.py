from battle import path_difficulty, battle
from monster import monster_selection

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
    location_choice = location_choice = input(f"Where would you like to go next?\n{loc_frmt}\n").lower()

    if location_choice in locations:
        hero.location = locations[location_choice]
        if location_choice in ["s", "c", "e"]:
            pass
        else:
            difficulty = path_difficulty(hero.location)
            monster = monster_selection(difficulty)
            battle(hero, monster)
            if hero.health > 0:
                menu_selection(hero)
            else:
                print("Game Over!")
                return
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