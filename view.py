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
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton
from PyQt6 import uic

class View(QMainWindow):
    lValue: QLabel
    lAvg: QLabel
    pBGo: QPushButton
    pBReset: QPushButton

    def __init__(self):
        super().__init__()
        uic.loadUi("design.ui", self)
        # self.pBGo.clicked.connect(c.submit)
        # self.pBReset.clicked.connect(c.reset)
        self.pBReset.clicked.connect(self.reset)  # testhalber
        self.reset()

    def setValues(self, value: int, count: int, avg: float):
        pass

    def setTxtStatusbar(self, s: str) -> None:
        self.statusbar.showMessage(s)

    def reset(self) -> None:
        self.setValues(0, 0, None)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = View()
    view.show()
    sys.exit(app.exec_())