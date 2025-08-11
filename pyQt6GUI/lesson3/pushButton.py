from PyQt6.QtWidgets import (QApplication,
                             QWidget,
                             QLabel,
                             QPushButton
)
from PyQt6.QtGui import QFont
import sys


class Window(QWidget):


    def __init__(self):
        super().__init__()

        self.setWindowTitle("ArMarX Test")
        self.setGeometry(0,0,400,400)
        self.initUi()


    def initUi(self):
        nameLabel = QLabel(self)
        nameLabel.setText("ArMarX Test")
        nameLabel.setFont(QFont("Arial", 14))
        nameLabel.move(20, 20)

        button = QPushButton(self)
        button.setText("Click Me")
        button.move(20, 60)
        button.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        print("Button is Clicked")




app = QApplication(sys.argv)


window = Window()
window.show()
sys.exit(app.exec())