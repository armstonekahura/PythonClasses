from PyQt6.QtWidgets import (QWidget,
                             QApplication,
                             QHBoxLayout,
                             QVBoxLayout,
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
        button1 = QPushButton("Button1")
        button2 = QPushButton("Button2")
        button3 = QPushButton("Button3")
        button4 = QPushButton("Button4")

        # hbox1 = QHBoxLayout()
        # hbox1.addWidget(button1)
        # hbox1.addWidget(button2)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(button3)
        hbox2.addWidget(button4)

        mainVBoxLayout =  QVBoxLayout()
        # mainVBoxLayout.addWidget(hbox1)
        mainVBoxLayout.addWidget(hbox2)

        self.setLayout(mainVBoxLayout)
        
app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())