import random
from cgitb import reset


class Model:
    moves = ["rock", "paper", "scissors"]

    def __init__(self):
        self.reset()

    def reset(self):
        """Reset all scores and rounds."""
        self.round = 0
        self.player_score = 0
        self.computer_score = 0
        self.last_player_move = None
        self.last_computer_move = None
        self.last_result = None

    def get_random_move(self):
        """Computer chooses randomly."""
        return random.choice(self.moves)

    def play_round(self, player_move: str):
        """Play one round and determine winner."""
        self.round += 1
        self.last_player_move = player_move
        self.last_computer_move = self.get_random_move()

        result = self.decide_winner(player_move, self.last_computer_move)
        self.last_result = result

        if result == "player":
            self.player_score += 1
        elif result == "computer":
            self.computer_score += 1

        return result

    def decide_winner(self, player: str, computer: str) -> str:
        """Decide who wins a round."""
        if player == computer:
            return "tie"
        wins = {
            "scissors": "paper",
            "rock": "scissors",
            "paper": "rock"
        }
        return "player" if wins[player] == computer else "computer"