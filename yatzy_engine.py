class YatzyEngine:
    def __init__(self):
        # Initialize score table with categories and placeholder scores
        self.score_table = {
            "Ones": 0,
            "Twos": 0,
            "Threes": 0,
            "Fours": 0,
            "Fives": 0,
            "Sixes": 0,
            "Three of a Kind": 0,
            "Four of a Kind": 0,
            "Small Straight": 0,
            "Large Straight": 0,
            "Full House": 0,
            "Chance": 0,
            "Yatzy": 0
        }

    def calculateScore(self, category, diceValues):
        # Simplified scoring based on the category chosen
        if category == "Ones":
            return diceValues.count(1) * 1
        elif category == "Twos":
            return diceValues.count(2) * 2
        elif category == "Threes":
            return diceValues.count(3) * 3
        elif category == "Fours":
            return diceValues.count(4) * 4
        elif category == "Fives":
            return diceValues.count(5) * 5
        elif category == "Sixes":
            return diceValues.count(6) * 6
        elif category == "Chance":
            return sum(diceValues)
        elif category == "Yatzy":
            return 50 if len(set(diceValues)) == 1 else 0
        else:
            return 0  # Placeholder for other categories

    def isValidSelection(self, category, diceValues):
        # Placeholder validation logic for the category
        return category in self.score_table
