import sys
from PyQt6.QtWidgets import QApplication

from model import Model
from view import View

class MyController:
    def __init__(self):
        self.model = Model()
        self.view = View()

        # Connect signals
        self.view.start.clicked.connect(self.play_round)
        self.view.reset_button.clicked.connect(self.reset_game)
        self.view.pushButton_3.clicked.connect(self.exit_game)

        self.view.update_view(self.model)
        self.view.show()

    def play_round(self):
        """Get player move from spinbox and play a round."""
        move_index = self.view.play_spin.value()
        player_move = self.model.moves[move_index]

        self.model.play_round(player_move)
        self.view.update_view(self.model)

    def reset_game(self):
        self.model.reset()
        self.view.reset()
        self.view.update_view(self.model)

    def exit_game(self):
        self.view.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = MyController()
    sys.exit(app.exec())