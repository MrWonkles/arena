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

    userChoice = input("\nEnter your choice: ")
    validChoices = ['1','2','3','4']

    while userChoice not in validChoices:
        print("Please choose again...")
        userChoice = input("Enter your choice: ")
    else:
        return userChoice

def PlayerAction():

    EndCheck()

    print("---------------------")
    print(f"Player HP:\t{player.hitPoints}")
    print(f"Player Energy:\t{player.energy}\n")
    sleep(0.5)
    print("Actions:")
    print("---------------------")
    sleep(0.5)
    print(f"1) {player.attacks[0].name} (Damage: {player.attacks[0].damageDice}) (Energy cost: {player.attacks[0].cost})")
    sleep(0.5)
    print(f"2) {player.attacks[1].name} (Damage: {player.attacks[1].damageDice}) (Energy cost: {player.attacks[1].cost})")
    sleep(0.5)
    print(f"3) {player.attacks[2].name} (Damage: {player.attacks[2].damageDice}) (Energy cost: {player.attacks[2].cost})")
    sleep(0.5)
    print("4) Rest (Restore Full Energy)")

    playerChoice = ChoiceCheck()
    playerChoice = int(playerChoice) - 1

    if playerChoice == 3:

        player.energy = player.energy + 15
        print("Player is resting...\n")

    elif player.energy >= player.attacks[playerChoice].cost:

        currentMonster.hitPoints = player.attackMonster(playerChoice, D20(), currentMonster.armor, currentMonster.hitPoints)

    else:
        player.energy = player.energy + 15
        print("Not enough energy!\n")
        sleep(0.5)
        print("Player is resting...\n")

    sleep(1)
    MonsterAction()

def MonsterAction():

    EndCheck()

    player.hitPoints = currentMonster.attackPlayer(D20(), player.armor, player.hitPoints)

    sleep(1)
    PlayerAction()

monsterList = (Goblin(), CaveTroll(), FlameImp())

player = Player()

print("ENTER THE ARENA!\n")
sleep(1)
print("Who will you fight?\n")
sleep(1)
print(f"1) {monsterList[0].type}")
sleep(0.5)
print(f"2) {monsterList[1].type}")
sleep(0.5)
print(f"3) {monsterList[2].type}")
sleep(0.5)
print("4) Random Choice\n")
sleep(1)
print("Choose wisely...")

currentMonster = ChoiceCheck()

if currentMonster == '1': currentMonster = monsterList[0]
if currentMonster == '2': currentMonster = monsterList[1]
if currentMonster == '3': currentMonster = monsterList[2]
if currentMonster == '4': currentMonster = r.choice(monsterList)

print(f"\nYou will fight the {currentMonster.type}!\n")
sleep(1)
PlayerAction()
