from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox, QLabel
from PyQt6.QtGui import QFont
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ArMarX Coffee Calculator")
        self.setGeometry(0, 0, 400, 300)

        self.initUI()

    
    def initUI(self):

        self.totalCost = 0
        
        titleLabel = QLabel(self)
        titleLabel.setText("Select your options")
        titleLabel.setFont(QFont("Ubuntu", 16))
        titleLabel.move(80, 30)

        sugarCheckbox = QCheckBox(self)
        sugarCheckbox.setText("Sugar    (Ksh. 40)")
        sugarCheckbox.setFont(QFont("Arial", 13))
        sugarCheckbox.move(30, 70)
        sugarCheckbox.toggled.connect(self.sugarChecked)

        milkCheckbox = QCheckBox(self)
        milkCheckbox.setText("Milk      (Ksh. 60)")
        milkCheckbox.setFont(QFont("Arial", 13))
        milkCheckbox.move(30, 110)
        milkCheckbox.toggled.connect(self.milkChecked)

        totalLabel = QLabel("Total", self)
        totalLabel.setFont(QFont("Arial", 13))
        totalLabel.move(60, 190)

        self.resultLabel = QLabel("", self)
        self.resultLabel.setFont(QFont("Arial", 30))
        self.resultLabel.resize(200, 40)
        self.resultLabel.move(160, 180)

    def sugarChecked(self, checked):
        if checked:
            self.totalCost += 40
            
        else:
            self.totalCost -= 40
            
        self.resultLabel.setText(str(self.totalCost))

    
    def milkChecked(self, checked):
        if checked:
            self.totalCost += 60
        else:
            self.totalCost -= 60

        self.resultLabel.setText(str(self.totalCost))


app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())