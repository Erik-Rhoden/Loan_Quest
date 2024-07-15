import time
import random

def main():
    4
    difficulty, area = path_difficulty()
    monster = monster_selection(difficulty)
    print(monster)

def opening_scene():
    name = input("Care to try again...ugh...what was your name again, friend? ")
    time.sleep(3)
    print(f"That's right, {name}. Double or nothing. If you win this then you'll be rich!")
    time.sleep(3)
    print("*You look up at the shady fellow and nod in agreement*\n...*The die are cast!*")
    time.sleep(2)
    print("'YOU LOSE!' shouts the shady fellow.")
    time.sleep(2)
    print(f"It's time you pay what you owe, {name}. That'll be 1,000 gold.")
    time.sleep(2)
    answer = input("Are you ready to pay up? (y/n)\n")
    if answer == 'n':
        print(f"You have one week to get me my money, {name}!")
    elif answer == 'y':
        print("Don't lie to me! I want my money in one week or else!")
    else:
        print("I don't have time for your games! It's obvious you are dead broke and if you don't have my money in one week you'll be dead as well!")
    time.sleep(3)
    print("*You are cast out into the street...*")
    time.sleep(2)
    print("The only way to make that kind of money in a week is by adventuring!")
    time.sleep(3)
    print("*You bring yourself to the edge of town and decide where you will go...*")
    return name

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
                return chosen_difficulty, area
        print("Invalid input. Please choose again.")


def monster_selection(difficulty):
    enemy_map = {1: {
                    "green slime": {
                            "health": 2, 
                            "attack": 1, 
                            "defense": 0
                        }, 
                    "red slime": {
                            "health": 3, 
                            "attack": 1, 
                            "defense": 1
                        },
                    "silver slime": {
                            "health": 5, 
                            "attack": 2, 
                            "defense": 2
                        },
                    "golden slime": {
                            "health": 10, 
                            "attack": 3, 
                            "defense": 3
                        }},
                2: {
                    "green goblin": {
                            "health": 7,
                            "attack": 3,
                            "defense": 2
                        },
                    "red goblin": {
                            "health": 9,
                            "attack": 3,
                            "defense": 2
                        },
                    "silver goblin": {
                            "health": 11,
                            "attack": 4,
                            "defense": 3
                        },
                    "golden goblin": {
                            "health": 13,
                            "attack": 5,
                            "defense": 4
                    }},
                3: {
                    "green orc": {
                            "health": 15,
                            "attack": 7,
                            "defense": 5
                        },
                    "red orc": {
                            "health": 18,
                            "attack": 8,
                            "defense": 7
                        },
                    "silver orc": {
                            "health": 21,
                            "attack": 10,
                            "defense": 8
                        },
                    "golden orc": {
                            "health": 30,
                            "attack": 15,
                            "defense": 12
                        },
                    }
                }
    monster, val = random.choice(list(enemy_map[difficulty].items()))
    name, health, attack, defense = monster, val["health"], val["attack"], val["defense"]
    return Monster(name, health, attack, defense)

class Monster():
    def __init__(self, name, health, attack, defense):
        self.__name = name
        self.__health = health
        self.__attack = attack
        self.__defense = defense

    def get_health(self):
        return self.__health
    
    def take_damage(self):
        self.__health -= 1
    
    def __repr__(self):
        return f"The {self.__name} has {self.__health} health, {self.__attack} attack, and {self.__defense} defense."
    
if __name__ == '__main__':
    main()