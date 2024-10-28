from yatzy_game import YatzyGame

if __name__ == "__main__":
    game = YatzyGame()
    game.startNewGame()

    # Play a few rounds for demonstration (e.g., 5 rounds)
    for _ in range(5):
        game.playRound()

    game.endGame()
