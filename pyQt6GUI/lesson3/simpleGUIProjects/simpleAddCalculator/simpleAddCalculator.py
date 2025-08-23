from PyQt6.QtWidgets import (QApplication,
                             QWidget, 
                             QLabel,
                             QLineEdit,
                             QPushButton,
)
from PyQt6.QtGui import QFont
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ArMarX Recap")
        self.setGeometry(0, 0, 230, 300)
        self.initUI()

    def initUI(self):
        self.num1LineEdit = QLineEdit(self)
        self.num1LineEdit.move(40, 40)
        self.num1LineEdit.setStyleSheet("""
            background-color: white;
            border: 1px solid green;
            border-radius: 10px;
            color: #000;
        """)

        addSign = QLabel("+",self)
        addSign.move(100, 80)

        self.num2LineEdit = QLineEdit(self)
        self.num2LineEdit.move(40, 120)
        self.num2LineEdit.setStyleSheet("""
            background-color: #fff;
            border: 1px solid #fff;
            border-radius: 10px;
            color: #000
        """)

        self.answerLabel = QLabel("?", self)
        self.answerLabel.move(80, 200)

        addBtn = QPushButton("Add",self)
        addBtn.clicked.connect(self.addFn)
        addBtn.setFixedSize(60, 30)
        addBtn.setFont(QFont("Arial", 16))
        addBtn.move(80, 250)
        addBtn.setStyleSheet("""
            background-color: green;
            color: #fff;
            border: 1px solid green;
            border-radius: 11px;
        """)


    def addFn(self):
        try:
            num1 = int(self.num1LineEdit.text())
            num2 = int(self.num2LineEdit.text())

            sum = num1 + num2 
            

            self.answerLabel.setFont(QFont("Ubuntu", 20))
            self.answerLabel.setText(f"{sum}")
            self.answerLabel.move(100, 200)
            self.answerLabel.adjustSize()
            self.answerLabel.setStyleSheet("""
                color: green
            """)
        
        except ValueError:
            self.answerLabel.setFixedSize(200, 30)
            self.answerLabel.setFont(QFont("Ubuntu", 16))
            self.answerLabel.move(30, 200)
            self.answerLabel.setText("⚠️ Invalid Input!")
            self.answerLabel.setStyleSheet("""
                color: red

            """)

app = QApplication(sys.argv)

window = Window()
window.show()
sys.exit(app.exec())