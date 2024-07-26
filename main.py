from dialogue import opening_scene
from monster import *
from hero import *
from menu import menu_selection

def main():
    # name = opening_scene()
    hero = Hero("Zilharr", 50, 50, 50, 50)
    hero.equip_item()
    game_running = True
    time = 0

    while game_running and hero.health > 0:
        menu_selection(hero)
        if hero.exit_game:
            game_running = False

if __name__ == '__main__':
    main()