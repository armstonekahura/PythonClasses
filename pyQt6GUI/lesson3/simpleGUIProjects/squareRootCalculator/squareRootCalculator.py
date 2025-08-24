from PyQt6.QtWidgets import (QMainWindow,
                             QApplication,
                             QWidget,
                             QLabel,
                             QPushButton,
                             QLineEdit
)
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ArmarX squareroot calculator")
        self.setGeometry(0, 0, 400, 300)

        self.initUI()


    def initUI(self):
        titleLabel = QLabel("Enter a square number", self)
        titleLabel.move(50, 30)

        inputNumber = QLineEdit(self)
        inputNumber.move(50, 60)

        answer = QLabel("Answer:", self)
        answer.move(50, 90)

        answerLabel = QLabel("",self)
        answerLabel.move(50, 120)


app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())