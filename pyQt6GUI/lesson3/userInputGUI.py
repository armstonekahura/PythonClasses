from PyQt6.QtWidgets import (QApplication,
                             QWidget,
                             QLabel,
                             QLineEdit,
                             QPushButton
)
from PyQt6.QtGui import QFont
import sys


class Window(QWidget):


    def __init__(self):
        super().__init__()

        self.setWindowTitle("ArMarX Accept User Input")
        self.setGeometry(0,0,400,400)
        self.initUI()


    def initUI(self):

        nameLabel = QLabel(self)
        nameLabel.setText("Enter your Name")
        nameLabel.move(30, 60)

        self.inputName = QLineEdit(self)
        self.inputName.resize(200, 25)
        self.inputName.move(180, 58)

        button = QPushButton(self)
        button.setText("Add")
        button.move(300, 350)
        button.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        print("Your name is "+self.inputName.text())
        



app = QApplication(sys.argv)


window = Window()
window.show()
sys.exit(app.exec())