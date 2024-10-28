from yatzy_engine import YatzyEngine
from dice import Dice

class YatzyGame:
    def __init__(self):
        self.current_round = 1
        self.total_score = 0
        self.yatzy_engine = YatzyEngine()
        self.dice = Dice()

    def startNewGame(self):
        self.current_round = 1
        self.total_score = 0
        print("Starting a new Yatzy game!")

    def playRound(self):
        # Roll the dice and get the result
        rolled_values = self.dice.roll()
        print(f"Round {self.current_round}: Rolled values: {rolled_values}")

        # Example: Calculating score for the 'Chance' category
        category = "Chance"
        score = self.yatzy_engine.calculateScore(category, rolled_values)
        print(f"Score for {category}: {score}")

        # Increment the score and move to the next round
        self.total_score += score
        self.current_round += 1

    def endGame(self):
        print("Game Over! Final score:", self.total_score)
