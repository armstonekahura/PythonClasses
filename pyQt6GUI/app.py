from PyQt6.QtWidgets import QApplication, QMainWindow

app = QApplication([])

window = QMainWindow()

window.setFixedSize(400, 500)
window.show()

app.exec()