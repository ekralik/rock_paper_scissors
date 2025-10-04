import sys
from PyQt6.QtWidgets import QApplication

import Model
import View


class MyController:
    def __init__(self):
        self.model = Model.Wuerfel()
        self.view = View.MyView(self) # View/Controller
        self.reset()
        self.view.show()
    def submit(self) -> None:
        value = self.model.go()
        count = self.model.count
        avg = self.model.avg()
        self.view.setValues(value, count, avg)
    def reset(self) -> None:
        self.view.reset()
        self.model.reset()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    c = MyController()
    sys.exit(app.exec())