from Monsters import *
import random as r
from Player import *
from time import sleep

def D20():
    return r.randint(1,20)

def EndCheck():

    if player.hitPoints < 1:
        sleep(1)
        print(f"{currentMonster.type} has defeated you...")
        exit()
    elif currentMonster.hitPoints < 1:
        sleep(1)
        print(f"The {currentMonster.type} has been defeated. You win!")
        exit()

def ChoiceCheck():

    userChoice = input("Enter your choice: ")
    validChoices = ['1','2','3','4']

    while userChoice not in validChoices:
        print("Please choose again...")
        userChoice = input("Enter your choice: ")
    else:
        return userChoice

def PlayerAction():

    EndCheck()

    print("---------------------")
    print(f"Player HP:\t{player.hitPoints}\n")
    sleep(0.5)
    print("Actions:")
    print("---------------------")
    sleep(0.5)
    print(f"1) {player.attacks[0].name} ({player.attacks[0].damageDice})")
    sleep(0.5)
    print(f"2) {player.attacks[1].name} ({player.attacks[1].damageDice})")
    sleep(0.5)
    print(f"3) {player.attacks[2].name} ({player.attacks[2].damageDice})")
    sleep(0.5)
    print("4) Exit Game")

    userChoice = ChoiceCheck()

    if userChoice == '1': userChoice = 0
    elif userChoice == '2': userChoice = 1
    elif userChoice == '3': userChoice = 2
    else:
        print("Goodbye...")
        sleep(1)
        exit()

    currentMonster.hitPoints = player.attackMonster(userChoice, D20(), currentMonster.armor, currentMonster.hitPoints)
    sleep(1)
    MonsterAction()

def MonsterAction():

    EndCheck()

    player.hitPoints = currentMonster.attackPlayer(D20(), player.armor, player.hitPoints)

    PlayerAction()

monsterList = (Goblin(), CaveTroll(), FlameImp())

player = Player()

print("ENTER THE ARENA!\n")
sleep(1)
print("Who will you fight?\n")
sleep(1)
print("1) Goblin")
sleep(0.5)
print("2) Cave Troll")
sleep(0.5)
print("3) Flame Imp")
sleep(0.5)
print("4) Random Choice\n")
sleep(0.5)
print("Choose wisely...\n")

currentMonster = ChoiceCheck()

if currentMonster == '1': currentMonster = monsterList[0]
if currentMonster == '2': currentMonster = monsterList[1]
if currentMonster == '3': currentMonster = monsterList[2]
if currentMonster == '4': currentMonster = r.choice(monsterList)

print(f"\nYou will fight the {currentMonster.type}!\n")
sleep(1)
PlayerAction()
