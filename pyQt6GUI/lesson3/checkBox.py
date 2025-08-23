from PyQt6.QtWidgets import QWidget, QApplication, QCheckBox, QLabel
from PyQt6.QtGui import QFont

import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ArMarX Lessons")
        self.setGeometry(0, 0, 400, 300)

        self.initUI()

    def initUI(self):
        sugarCheckbox = QCheckBox(self)
        sugarCheckbox.setText("Sugar")
        sugarCheckbox.move(30, 40)
        sugarCheckbox.toggled.connect(self.sugarChecked)

        self.outputLabel = QLabel("Waiting...",self)
        self.outputLabel.setFont(QFont("Ubuntu", 15))
        self.outputLabel.resize(200, 30)
        self.outputLabel.setStyleSheet("""
            color: white;
        """)
        self.outputLabel.move(30, 90)

    def sugarChecked(self, checked):
        if checked:
            self.outputLabel.setText("Sugar added")
            self.outputLabel.setStyleSheet("""
                color: green;
            """)
        else:
            self.outputLabel.setText("Sugar not added")
            self.outputLabel.setStyleSheet("""
                color: red;
            """)

app = QApplication(sys.argv)

window = Window()
window.show()
sys.exit(app.exec())