from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon

app = QApplication([])

window = QMainWindow()

window.setMinimumSize(400, 500)
window.setWindowTitle("Armstone")
window.setWindowIcon(QIcon("arm.png"))
window.show()

app.exec()