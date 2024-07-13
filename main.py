import time
from enum import Enum

def main():
    # name = opening_scene()
    difficulty, area = path_difficulty()

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
    
if __name__ == '__main__':
    main()