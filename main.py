from dialogue import opening_scene
from monster import *
from hero import *
from menu import menu_selection, time_logged

def main():
    # name = opening_scene()
    hero = Hero("Zilharr", 100, 5, 5, 3)
    hero.equip_item()
    game_running = True

    while game_running and hero.health > 0 and hero.time < hero.max_time:
        menu_selection(hero)
        if hero.exit_game:
            game_running = False

    if hero.time >= hero.max_time:
        print("You've ran out of time! Game Over!")

if __name__ == '__main__':
    main()