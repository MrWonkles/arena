import random as r

class Attack:

    def __init__(self):
        self.name = ''
        self.damage = 1

## <-- Monster Attacks -->

class Fireball(Attack):

    def __init__(self):
        self.name = 'Fireball'
        self.damage = r.randint(1,6) + 2

class Singe(Attack):

    def __init__(self):
        self.name = 'Singe'
        self.damage = r.randint(1,4) + 1

class Inferno(Attack):

    def __init__(self):
        self.name = 'Inferno'
        self.damage = r.randint(1,10)

class Bash(Attack):

    def __init__(self):
        self.name = 'Bash'
        self.damage = r.randint(1,6) + 1

class ClubSmash(Attack):

    def __init__(self):
        self.name = 'Club Smash'
        self.damage = r.randint(1,8) + 1

class Stomp(Attack):

    def __init__(self):
        self.name = 'Stomp'
        self.damage = r.randint(1,6)

class Claw(Attack):

    def __init__(self):
        self.name = 'Claw'
        self.damage = r.randint(1,4)

class Bite(Attack):

    def __init__(self):
        self.name = 'Bite'
        self.damage = r.randint(1,6)

class LeapAttack(Attack):

    def __init__(self):
        self.name = 'Leap Attack'
        self.damage = r.randint(1,6) + 2

## <-- Player Attacks -->

class SwordSlash(Attack):

    def __init__(self):
        self.name = "Sword Slash"
        self.damageDice = "d6 + 1"
        self.damage = r.randint(1, 6) + 1

class QuickStab(Attack):

    def __init__(self):
        self.name = "Quick Stab"
        self.damageDice = "d4"
        self.damage = r.randint(1,4)

class SpinningBlade(Attack):

    def __init__(self):
        self.name = "Spinning Blade"
        self.damageDice = "d8 + 2"
        self.damage = r.randint(1,8) + 2

