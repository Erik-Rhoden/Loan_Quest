import time

class Hero():
    def __init__(self, name, health, attack, defense, speed):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.gold = 0.0

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
    
    def __repr__(self):
        return f"{self.name} has {self.health} health, {self.attack} attack, {self.defense} defense, and {self.speed} speed."
    
def path_difficulty():
    difficulty_map = [
        {'DIFFICULTY': "EASY", 'LEVEL': 1, 'AREA': "Slime Plains"},
        {'DIFFICULTY': "MEDIUM", 'LEVEL': 2, 'AREA': "Goblin Forest"},
        {'DIFFICULTY': "HARD", 'LEVEL': 3, 'AREA': "Orc Valley"}
    ]
        
    while True:
        print("Choose a path...")
        time.sleep(2)
        difficulty_input = input("Easy - Slime Plains, Medium - Goblin Forest, Hard - Orc Valley\n").upper()
        for entry in difficulty_map:
            if difficulty_input == entry['DIFFICULTY']:
                chosen_difficulty = entry['LEVEL']
                area = entry['AREA']
                print(f"You've chosen {area}\n")
                return chosen_difficulty
        print("Invalid input. Please choose again.")