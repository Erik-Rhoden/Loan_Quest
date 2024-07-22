from dialogue import *
from monster import *
from hero import *

def main():
    # name = opening_scene()
    hero = Hero("Zilharr", 50, 50, 50, 50)
    hero.equip_item()
    time = 0
    #give option to equip if item is equipable or go into inventory
    def menu_selection(hero):
        options = {
            "t": "Travel",
            "i": "Inventory",
            "st": "Stats"
        }

        locations = {
            "s": "Shop",
            "c": "Center of Town",
            "e": "Edge of Town",
            "p": "Slime Plains",
            "g": "Goblin Forest",
            "o": "Orc Valley"
        }
        
        print(f"\nCurrent location: {hero.location}\n")
        opt_frmt = "|--Travel-(t)| |--Inventory-(i)| |--Stats-(st)|"
        loc_frmt = "|--Shop-(s)| |--Center of Town-(c)| |--Edge of Town-(e)| |--Slime Plains-(p)| |--Goblin Forest-(g)| |--Orc Valley-(o)|"

        choice = input(f"What would you like to do next?\n{opt_frmt}\n")

        if choice in options:
            if choice == "t":
                location_choice = input(f"Where would you like to go next?\n{loc_frmt}\n")
                if location_choice in locations:
                    hero.location = locations[location_choice]
                    if location_choice in ["s", "c", "e"]:
                        menu_selection(hero)
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
            elif choice == "i":
                print("--------------")
                hero.search_inventory()
                print("--------------")
            elif choice == "st":
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
        else:
            print(f"Invalid entry. Please try again.")

    while hero.health > 0:
        menu_selection(hero)

if __name__ == '__main__':
    main()