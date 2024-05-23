import random as r
from time import sleep
from Attacks import SwordSlash, QuickStab, SpinningBlade

class Player():

    def __init__(self):
        self.name = "Player"
        self.hitPoints = 100
        self.armor = 15
        self.energy = 15
        self.attacks = (SwordSlash(), QuickStab(), SpinningBlade())

    def attackMonster(self, attack, toHit, monsterArmor, monsterHP):

        attackChoice = self.attacks[attack]
        self.energy = self.energy - attackChoice.cost

        print(f"{self.name} uses {attackChoice.name}")
        sleep(1)
        print(f"{self.name} rolls {toHit}...")
        sleep(1)

        if toHit >= monsterArmor:
            print(f"{self.name} hits!")
            sleep(1)
            print(f"{self.name} deals {attackChoice.damage} damage!\n")
            return monsterHP - attackChoice.damage
        else:
            print(f"{self.name} misses!\n")
            return monsterHP