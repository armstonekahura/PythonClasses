from PyQt6.QtWidgets import (QWidget,
                             QApplication,
                             QVBoxLayout,
                             QLabel,
                             QLineEdit,
                             QPushButton
)

import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ArmarX vbox layout")
        self.setGeometry(0, 0, 300, 200)

        self.initUI()


    def initUI(self):
        nameLabel = QLabel("Name")
        nameLineEdit = QLineEdit()
        nextBtn = QPushButton("Next")

        vBoxLayout = QVBoxLayout()
        vBoxLayout.addWidget(nameLabel)
        vBoxLayout.addWidget(nameLineEdit)
        vBoxLayout.addWidget(nextBtn)

        self.setLayout(vBoxLayout)


app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())