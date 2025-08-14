from PyQt6.QtWidgets import QApplication, QWidget

import sys


class SimpleCalc(QWidget):
    def __init__(self):
        super().__init__()

    def initUI(self):
        self.setWindowTitle("ArMarX simpleCalc")
        self.setGeometry(0, 0, 350, 300)

app = QApplication(sys.argv)

simpleCalc = SimpleCalc()
simpleCalc.show()
sys.exit(app.exec())