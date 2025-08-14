from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt6.QtGui import QFont

import sys


class SimpleCalc(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("ArMarX simpleCalc")
        self.setGeometry(0, 0, 400, 300)

        num1Label = QLabel("Insert a number", self)
        num1Label.move(30, 30)

        self.num1LineEdit = QLineEdit(self)
        self.num1LineEdit.move(200, 28)

        num2Label = QLabel("Insert another number", self)
        num2Label.move(30, 80)

        self.num2LineEdit = QLineEdit(self)
        self.num2LineEdit.move(200, 78)

        answerLabel = QLabel("Answer", self)
        answerLabel.move(70, 145)

        self.answerLabel = QLabel("0.0", self)
        self.answerLabel.setFont(QFont("Ubuntu Sans Mono", 20))
        self.answerLabel.move(180, 130)

        addBtn = QPushButton("Add", self)
        addBtn.clicked.connect(self.sumCalculation)
        addBtn.move(200, 260)

    def sumCalculation(self):
        try:
            num1 = float(self.num1LineEdit.text())
            num2 = float(self.num2LineEdit.text())
            sum = num1 + num2

            self.answerLabel.setText(f"{sum:.2f}")
            self.answerLabel.adjustSize()
        except ValueError:
            self.answerLabel.setFont(QFont("Ubuntu Sans Mono", 20))
            self.answerLabel.setFixedSize(300, 50)
            self.answerLabel.setText("Invalid Input!")



app = QApplication(sys.argv)

simpleCalc = SimpleCalc()
simpleCalc.show()
sys.exit(app.exec())