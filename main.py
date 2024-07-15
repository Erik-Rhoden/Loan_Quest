import time
import random
from dialogue import *
from monster import *
from hero import *

def main():
    name = opening_scene()
    difficulty, area = path_difficulty()
    monster = monster_selection(difficulty)
    hero = Hero(name, 5, 5, 5)
    hero.deal_damage(monster)
    monster.deal_damage(hero)
    print(monster, hero)
    
if __name__ == '__main__':
    main()