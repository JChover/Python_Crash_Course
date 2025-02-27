# 9-13 Dice
from random import randint

class Die:
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        """Returns a random value between 1 and Sides"""
        print(randint(1, self.sides))


print("\nLet's roll the 6-sided die 10 times!")
for rolls in range(10):  # Roll the 6-sided die 10 times
    die = Die()
    die.roll_die()

print("\nLet's roll the 10-sided die 10 times!")
for rolls in range(10):  # Roll the 10-sided die 10 times
    die = Die(10)
    die.roll_die()

print("\nLet's roll the 20-sided die 10 times!")
for rolls in range(10):  # Roll the 20-sided die 10 times
    die = Die(20)
    die.roll_die()
