import time

class Hero():
    def __init__(self, name, health, attack, defense, speed):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.location = "Center of Town"
        self.gold = 0.0
        self.inventory = []
        self.max_inv_size = 8

    def get_health(self):
        return self.health

    def deal_damage(self, target):
        net_damage = self.attack - target.defense
        if target.defense > self.attack:
            target.health
        elif net_damage > target.health:
            target.health = 0
        else:
            target.health -= net_damage

    def get_loot(self, hero, monster):
        print(f"{hero.name} defeated {monster.name}!\nLet's see what they dropped!\n")
        if not monster.inventory:
                print(f"Too bad! The {monster.name} had nothing!")
                return
        for item_key, item_value in monster.inventory.items():
            if len(self.inventory) < self.max_inv_size:
                self.inventory.append({item_key: item_value})
                print(f"{item_key} dropped!")
            else:
                print(f"Your inventory is full!\n")
                return
    
    def __repr__(self):
        return f"{self.name} has {self.health} health, {self.attack} attack, {self.defense} defense, and {self.speed} speed."
    
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
        else:
            monster.deal_damage(hero)
            if hero.health > 0:
                hero.deal_damage(monster)
    if hero.health == 0:
        print(f"{monster.name} defeated {hero.name}!")
        return
    else:
        hero.get_loot(hero, monster)