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
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QWidget, QSpinBox
from PyQt6 import uic

class View(QMainWindow):
    label_7: QLabel #aktuelle Runde
    spinBox: QSpinBox #runde spielen
    start: QPushButton
    resetB: QPushButton
    pushButton_3: QPushButton #schließen

    def __init__(self):
        super().__init__()
        uic.loadUi("design.ui", self)
        self.setWindowTitle("Schere, Stein, Papier")
        self.setFixedSize(625, 500)
        self.reset()

    def setValues(self, value: int, count: int, avg: float):
        pass

    def setTxtStatusbar(self, s: str) -> None:
        self.statusBar().showMessage(s)

    def reset(self) -> None:
        self.setValues(0, 0, None)
        self.setTxtStatusbar("Ready to Play")
        self.spinBox.setValue(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = View()
    view.show()
    sys.exit(app.exec())
