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
                print(f"You've chosen {area}\n")
                return chosen_difficulty
        print("Invalid input. Please choose again.")

def battle(hero, monster):
    while hero.health > 0 and monster.health > 0:
        if hero.speed > monster.speed:
            hero.deal_damage(monster)
            if monster.health > 0:
                monster.deal_damage(hero)
        if monster.speed > hero.speed:
            monster.deal_damage(hero)
            if hero.health > 0:
                hero.deal_damage(monster)
    if hero.health <= 0:
        print(f"{monster.name} defeated {hero.name}!")
        hero.exit_game = True
    else:
        hero.get_loot(monster)