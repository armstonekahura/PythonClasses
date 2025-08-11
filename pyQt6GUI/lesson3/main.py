from PyQt6.QtWidgets import (QWidget,
                             QApplication,
                             QLabel,
)
from PyQt6.QtGui import QPixmap, QFont
import sys

class Window(QWidget):


    def __init__(self):
        super().__init__()

        self.setWindowTitle("ArMarX")
        self.setGeometry(0,0,400,600)

        
        with open ('car.png'):
            imageLabel = QLabel(self)
            pixmap = QPixmap('car.png')
            imageLabel.setPixmap(pixmap)
            imageLabel.move(50,20)

        nameLabel = QLabel(self)
        nameLabel.setText("Range Rover")
        nameLabel.setFont(QFont("Arial", 20))
        nameLabel.move(115, 200)

        engineLabel = QLabel(self)
        engineLabel.setText("Engine Capacity: 4l TFS")
        engineLabel.setFont(QFont("",16))
        engineLabel.move(20, 250)

        featureLabel = QLabel(self)
        featureLabel.setText("Features: ABS, EBD, ADAS")
        featureLabel.setFont(QFont("",15))
        featureLabel.move(20, 280)

        modelLabel = QLabel(self)
        modelLabel.setText("Model:      Sport, 2.2 petrol")
        modelLabel.setFont(QFont("", 14))
        modelLabel.move(20, 310)

        priceLabel = QLabel(self)
        priceLabel.setText("Price:          Ksh. 12M")
        priceLabel.setFont(QFont("", 13))
        priceLabel.move(20, 340)


app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())