import time
import random
from dialogue import *
from monster import *
from hero import *

def main():
    name = opening_scene()
    difficulty, = path_difficulty()
    monster, monster_name = monster_selection(difficulty)
    hero = Hero(name, 5, 5, 5, 5)
    print(battle(hero, monster))
    
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
        return f"{monster.name} defeated {hero.name}!"
    return f"{hero.name} defeated {monster.name}!\nLet's see what they dropped!"

def loot_roll():
    pass
    
if __name__ == '__main__':
    main()