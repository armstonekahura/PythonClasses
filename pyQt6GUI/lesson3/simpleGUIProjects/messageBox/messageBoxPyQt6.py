from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QMessageBox, QPushButton
from PyQt6.QtGui import QFont

import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ArmarX messagebox")
        self.setGeometry(0, 0, 300, 200)

        self.initUI()


    def initUI(self):
        exitButton = QPushButton("Exit", self)
        exitButton.move(100, 150)
        exitButton.clicked.connect(self.exitMessageBox)


    def exitMessageBox(self):
        msg = QMessageBox(self)
        msg.setWindowTitle("ArmarX Message")
        msg.setText("Are you sure you want to exit?")
        msg.setIcon(QMessageBox.Icon.Question)
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msg.setDefaultButton(QMessageBox.StandardButton.Cancel)
        result = msg.exec()

        if result == QMessageBox.StandardButton.Yes:
            print("Yes button is clicked")
            sys.exit(app.exec())
        else:
            print("No button is clicked")


app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())
