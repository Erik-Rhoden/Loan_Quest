def path_difficulty(choice):
    difficulty_map = [
        {'LEVEL': 1, 'AREA': "Slime Plains"},
        {'LEVEL': 2, 'AREA': "Goblin Forest"},
        {'LEVEL': 3, 'AREA': "Orc Valley"}
    ]
        
    while True:
        for entry in difficulty_map:
            if choice == entry['AREA']:
                chosen_difficulty = entry['LEVEL']
                area = entry['AREA']
                print("--------------")
                print(f"You've chosen {area}\n")
                return chosen_difficulty
        print("Invalid input. Please choose again.")

def battle(hero, monster):
    print("--------------")
    print(f"A {monster.name} has appeared!")
    while hero.health > 0 and monster.health > 0:
        print(f"{hero.name}: {hero.health} HP\n{monster.name}: {monster.health} HP")
        print("--------------")
        if hero.speed >= monster.speed:
            battle_result = hero_battle_options(hero, monster)
            if battle_result == 'run':
                print("You successfully fled from battle!")
                print("--------------")
                return
        if monster.speed > hero.speed:
            monster.deal_damage(hero)
            if hero.health > 0:
                battle_result = hero_battle_options(hero, monster)
                if battle_result == 'run':
                    print("You successfully fled from battle!")
                    print("--------------")
                    return
    if hero.health <= 0:
        print(f"{monster.name} defeated {hero.name}!")
        hero.exit_game = True
    else:
        hero.get_loot(monster)

def hero_battle_options(hero, monster):
    battle_menu = "|--Attack-(a)| |--Heal-(h)| |--Run-(r)|\n"
    battle_choice = input(f"What would you like to do?\n{battle_menu}").lower()
    if battle_choice == 'a':
        hero.deal_damage(monster)
        if 0 < monster.health < (monster.max_hp * 0.5) and potion_check(monster):
            heal_amount = monster.heal_self()
            print(f"{monster.name} has healed itself for {heal_amount} HP")
        elif 0 < monster.health:
            monster.deal_damage(hero)
    if battle_choice == 'h':
        heal_amount = hero.heal_self()
        print(f"{hero.name} has healed themselves for {heal_amount} HP")
        print("--------------")
    if battle_choice == 'r':
        return 'run'
    return None
    
def potion_check(monster):
    for item in monster.inventory:
        if hasattr(item, 'heal'):
            return True
    return False