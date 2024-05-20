import random as r
from time import sleep
from Attacks import *

class Monster:

    def __init__(self):
        self.type = ''
        self.hitPoints = 1
        self.armor = 1
        self.attacks = []

    def attackPlayer(self, toHit, playerArmor, playerHP):

        attackChoice = r.choice(self.attacks)

        print(f"{self.type} uses {attackChoice.name}")
        sleep(1)
        print(f"{self.type} rolls {toHit}...")
        sleep(1)

        if toHit >= playerArmor:
            print(f"{self.type} hits!")
            sleep(1)
            print(f"{self.type} deals {attackChoice.damage} damage!\n")
            return playerHP - attackChoice.damage
        else:
            print(f"{self.type} misses!\n")
            return playerHP


class Goblin(Monster):

    def __init__(self):
        self.type = 'Goblin'
        self.hitPoints = 35
        self.armor = 10
        self.attacks = (Claw(), Bite(), LeapAttack())

class CaveTroll(Monster):

    def __init__(self):
        self.type = 'Cave Troll'
        self.hitPoints = 75
        self.armor = 15
        self.attacks = (Bash(), ClubSmash(), Stomp())

class FlameImp(Monster):

    def __init__(self):
        self.type = 'Flame Imp'
        self.hitPoints = 25
        self.armor = 5
        self.attacks = (Fireball(), Inferno(), Singe())