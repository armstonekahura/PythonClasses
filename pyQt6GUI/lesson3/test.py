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

        self.setWindowTitle("ArMarX test")
        self.setGeometry(0, 0, 400, 500)
        self.initUI()


    def initUI(self):
        self.count = 0
        
        titleLabel = QLabel(self)
        titleLabel.setText("ArMarX IT Solutions")
        titleLabel.setFont(QFont("Ubuntu Sans Mono", 20))
        titleLabel.adjustSize()
        titleLabel.move(20, 20)

        self.countLabel = QLabel(self)
        self.countLabel.setText("0")
        self.countLabel.setFont(QFont("Ubuntu Sans Miono", 60))
        self.countLabel.move(148, 70)

        addBtn = QPushButton(self)
        addBtn.setText("Add")
        addBtn.clicked.connect(self.countIncrement)
        addBtn.move(300, 450)

    
    def countIncrement(self):
        self.count += 1
        self.countLabel.setText(str(self.count))
        self.countLabel.adjustSize()

app = QApplication(sys.argv)
        
window = Window()
window.show()

sys.exit(app.exec())