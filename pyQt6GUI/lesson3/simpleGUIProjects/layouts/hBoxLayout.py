from PyQt6.QtWidgets import (QWidget,
                             QApplication,
                             QHBoxLayout,
                             QLabel,
                             QLineEdit,
                             QPushButton
)

import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ArmarX QHBoxLayout")
        self.setGeometry(0, 0, 400, 150)

        self.initUI()


    def initUI(self):
        nameLabel = QLabel("Name")
        inputName = QLineEdit()
        nextBtn = QPushButton("Next")

        hBoxLayout = QHBoxLayout()
        hBoxLayout.addWidget(nameLabel)
        hBoxLayout.addWidget(inputName)
        hBoxLayout.addWidget(nextBtn)

        self.setLayout(hBoxLayout)




app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())