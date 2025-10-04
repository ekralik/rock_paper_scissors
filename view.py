#   Sinnvoller Window-Titel
# • Anzahl der gespielten Runden
# • Aktueller Punktestand: Spieler/Computer
# • Neuer Spielzug via: SpinBox
# • Spiel neustarten (zurücksetzen)
# • Spiel schließen
# • Letzter Spielzug: Spieler/Computer
# • Neuen Spielzug auswählen: (Schere, Stein und Papier)
# • Neuen Spielzug ausführen
import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QSpinBox
from PyQt6 import uic

class View(QMainWindow):
    round: QLabel #aktuelle Runde
    play_spin: QSpinBox #runde spielen
    start: QPushButton
    reset_button: QPushButton
    pushButton_3: QPushButton #schließen

    def __init__(self):
        super().__init__()
        uic.loadUi("design.ui", self)
        #self.setWindowTitle("Rock, Paper, Scissors")
        self.setFixedSize(625, 500)

        self.play_spin.setRange(0, 2)
        #self.play_spin.setToolTip("0 = Schere, 1 = Stein, 2 = Papier")
        #self.play_spin.setSuffix("  (0=Schere, 1=Stein, 2=Papier)")

        self.reset()

    def setTxtStatusbar(self, s: str) -> None:
        self.statusBar().showMessage(s)

    """
    Update the view with the current model state.
    :param model: The current model state.
    """
    def update_view(self, model):
        self.round.setText(str(model.round))
        self.findChild(QLabel, "label_4").setText(f"player: {model.player_score}")
        self.findChild(QLabel, "label_5").setText(f"computer: {model.computer_score}")

        if model.last_result:
            self.setTxtStatusbar(
                f"round {model.round}: {model.last_result} – "
                f"player ({model.last_player_move}) vs computer ({model.last_computer_move})"
            )

    def reset(self) -> None:
        self.setTxtStatusbar("Game is ready to play")
        self.play_spin.setValue(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = View()
    view.show()
    sys.exit(app.exec())
