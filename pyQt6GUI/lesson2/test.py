from PyQt6.QtWidgets import (QWidget,
                             QApplication,
                             QLabel
)
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ArMarX test")
        self.setGeometry(0,0,400,600)

        label = QLabel(self)
        label.setText("ArMarX Test")
        label.move(50, 50)


app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())