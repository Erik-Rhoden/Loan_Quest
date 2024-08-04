import time
import random

def opening_scene():
    while True:
        name = input("Care to try again...ugh...what was your name again, friend? ").capitalize()
        if name.isalpha():    
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
            print("*You bring yourself to the Slime Plains where adventurers begin their journey. You appear hesitant but at your feet lies a stick...*")
            time.sleep(2)
            print("*You pick up the stick*")
            time.sleep(2)
            return name
        else:
            print("Hmm, maybe we need to cutback on the complimentary drinks...")

def encounter_text(hero, monster):
    if hero.defense * 3 < monster.defense and hero.attack < monster.attack * 3:
        outclassed_text = [f"Your path is blocked by a towering {monster.name}. The time for combat has come!",
                        f"A {monster.name} looms ahead, its eyes glinting with malevolence. Prepare for battle!",
                        f"An eerie silence falls as a menacing {monster.name} steps into view. Engage in battle!",
                        f"A guttural roar pierces the night. A {monster.name} has arrived. Defend yourself!"]
        return random.choice(outclassed_text)
    elif hero.defense > monster.defense * 3 and hero.attack > monster.attack * 3:
        knight_text = [f"A puny {monster.name} stumbles into your path, its eyes widening at the sight of your visage. Prepare for an easy victory!",
                       f"The {monster.name} hesitates, clearly intimidated by your presence. Show it the might of a true hero!",
                       f"The feeble {monster.name} before you can barely muster the courage to attack.",
                       f"As your armor clatters with each movement, the {monster.name} seems to shrink in fear. This will be a quick battle."]
        return random.choice(knight_text)
    elif hero.attack * 2 < monster.attack:
        powerful_text = [f"The air crackles with the force of the {monster.name}'s might, its power far surpassing your own. Prepare for a fierce battle!",
                         f"The {monster.name}'s raw strength is daunting, its blows twice as powerful as yours. This will be a true test of your resilience.",
                         f"A formidable {monster.name} stands before you, its strength easily double that of your own. Brace yourself for a grueling fight.",
                         f"The {monster.name}'s attacks are devastating, each strike capable of overwhelming your defenses. Strategy and precision will be key."]
        return random.choice(powerful_text)
    elif hero.defense * 3 < monster.defense:
        juggernaut_text = [f"The {monster.name} armor gleams menacingly, each plate thicker than your own. Steady your resolve for a tough battle.",
                           f"A heavily armored {monster.name} stands before you, its defenses daunting. This battle will not be easy.",
                           f"The {monster.name}'s armor is a fortress, dwarfing your own defenses. You'll need to be cunning to prevail.",
                           f"Every inch of the {monster.name} is covered in impenetrable armor, making your own seem like mere cloth. This will be a hard-fought battle."]
        return random.choice(juggernaut_text)
    elif monster.speed > hero.speed * 3:
        slower_text = [f"You are distracted by the latest Backend Banter podcast episode and are ambushed by a {monster.name}!",
                       f"The sound of your armor is so loud. You hope that a monster does not catch...a {monster.name} leaps out and attacks you!",
                       f"A chilling wind whispers of danger. A {monster.name} has found you. Brace yourself!",
                       f"A sudden darkness envelops you, and a {monster.name} emerges from the shadows. Prepare for battle!"]
        return random.choice(slower_text)
    elif hero.speed > monster.speed * 3:
        critical_text = [f"The {monster.name} moves sluggishly as you dart around it with unparalleled speed. Prepare for a swift victory!",
                         f"Like a bolt of lightning, you strike with speed that the {monster.name} cannot hope to match. Engage in combat!",
                         f"The {monster.name}'s attacks are a slow-motion blur as you dance around it effortlessly. Prepare to end this quickly.",
                         f"The gap in speed between you and the {monster.name} is vast. This battle will be won with agility and precision."]
        return random.choice(critical_text)
    else:
        normal_text = [f"A wild {monster.name} has appeared!",
                f"A {monster.name} has wandered onto your path!",
                f"You hear rustling in the nearby bush. You investigate and find a {monster.name}!",
                f"The underbrush rustles, revealing a hidden {monster.name}. Ready for combat!"]
        return random.choice(normal_text)