import random

class Dice:
    def __init__(self, num_dice=5):
        self.num_dice = num_dice
        self.values = []

    def roll(self):
        self.values = [random.randint(1, 6) for _ in range(self.num_dice)]
        return self.values
