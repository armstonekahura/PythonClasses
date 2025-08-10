from PyQt6.QtWidgets import (QWidget,
                             QApplication,
                             QLabel,
)
from PyQt6.QtGui import QPixmap
import sys

class Window(QWidget):


    def __init__(self):
        super().__init__()

        self.setWindowTitle("ArMarX")
        self.setGeometry(0,0,400,600)

        label = QLabel(self)
        label.setText("Hello ArMarX")
        label.move(50,50)


        with open ('car.png'):
            imageLabel = QLabel(self)
            pixmap = QPixmap('car.png')
            imageLabel.setPixmap(pixmap)
            imageLabel.move(30,100)


app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())
