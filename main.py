from dialogue import *
from monster import *
from hero import *
from menu import menu_selection
from battle import final_battle

def main():
    name = opening_scene()
    hero = Hero(name, 10, 5, 5, 3)
    hero.equip_item()
    game_running = True

    while game_running and hero.health > 0 and (hero.time < hero.max_time) and hero.gold < 10000:
        menu_selection(hero)
        if hero.exit_game:
            game_running = False

    if hero.time >= hero.max_time:
        out_of_time()
        return

    if hero.gold >= 10000:
        final_choice = ending_scene()
        if final_choice == "pay":
            return
        elif final_choice == "fight":
            loan_shark = Monster(50, 50, 50, 15)
            result = final_battle(hero, loan_shark)
            if result:
                defeated_loan_shark()
                return
            else:
                return

if __name__ == '__main__':
    main()