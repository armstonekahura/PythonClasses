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

        self.setWindowTitle("ArMarX Event Handling")
        self.setGeometry(0,0,400,400)
        self.initUi()


    def initUi(self):
        self.count = 0

        nameLabel = QLabel(self)
        nameLabel.setText("Number Increment")
        nameLabel.setFont(QFont("Arial", 14))
        nameLabel.move(20, 20)

        self.countLabel = QLabel(self)
        self.countLabel.setText("0")
        self.countLabel.move(20, 60)

        button = QPushButton(self)
        button.setText("Click Me")
        button.move(20, 100)
        button.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        print("Button is Clicked")
        self.count += 1
        self.countLabel.setText(str(self.count))
        self.countLabel.adjustSize()




app = QApplication(sys.argv)


window = Window()
window.show()
sys.exit(app.exec())