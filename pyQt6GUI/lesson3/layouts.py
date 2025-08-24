import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QFormLayout, QPushButton,
    QLabel, QLineEdit, QSpinBox, QTabWidget
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Layout Demo")
        self.setGeometry(100, 100, 600, 400)
        
        # Create tab widget
        tabs = QTabWidget()
        self.setCentralWidget(tabs)
        
        # Add tabs with different layouts
        tabs.addTab(self.createVerticalLayoutTab(), "Vertical")
        tabs.addTab(self.createHorizontalLayoutTab(), "Horizontal")
        tabs.addTab(self.createGridLayoutTab(), "Grid")
        tabs.addTab(self.createFormLayoutTab(), "Form")
        tabs.addTab(self.createNestedLayoutTab(), "Nested")
    
    def createVerticalLayoutTab(self):
        widget = QWidget()
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel("Vertical Layout"))
        layout.addWidget(QPushButton("Button 1"))
        layout.addWidget(QPushButton("Button 2"))
        layout.addWidget(QPushButton("Button 3"))
        layout.addStretch()  # Add stretchable space
        
        widget.setLayout(layout)
        return widget
    
    def createHorizontalLayoutTab(self):
        widget = QWidget()
        layout = QHBoxLayout()
        
        layout.addWidget(QLabel("Horizontal Layout"))
        layout.addWidget(QPushButton("Left"))
        layout.addWidget(QPushButton("Center"))
        layout.addWidget(QPushButton("Right"))
        
        widget.setLayout(layout)
        return widget
    
    def createGridLayoutTab(self):
        widget = QWidget()
        layout = QGridLayout()
        
        layout.addWidget(QLabel("Grid Layout"), 0, 0, 1, 2)  # row, column, rowSpan, colSpan
        layout.addWidget(QPushButton("(0,0)"), 1, 0)
        layout.addWidget(QPushButton("(0,1)"), 1, 1)
        layout.addWidget(QPushButton("(1,0)"), 2, 0)
        layout.addWidget(QPushButton("(1,1)"), 2, 1)
        
        widget.setLayout(layout)
        return widget
    
    def createFormLayoutTab(self):
        widget = QWidget()
        layout = QFormLayout()
        
        layout.addRow("Name:", QLineEdit())
        layout.addRow("Email:", QLineEdit())
        layout.addRow("Age:", QSpinBox())
        layout.addRow(QPushButton("Submit"))
        
        widget.setLayout(layout)
        return widget
    
    def createNestedLayoutTab(self):
        widget = QWidget()
        main_layout = QVBoxLayout()
        
        # Top horizontal layout
        top_layout = QHBoxLayout()
        top_layout.addWidget(QLabel("Nested Layouts"))
        top_layout.addWidget(QPushButton("Help"))
        
        # Middle grid layout
        middle_layout = QGridLayout()
        middle_layout.addWidget(QPushButton("1"), 0, 0)
        middle_layout.addWidget(QPushButton("2"), 0, 1)
        middle_layout.addWidget(QPushButton("3"), 1, 0)
        middle_layout.addWidget(QPushButton("4"), 1, 1)
        
        # Bottom horizontal layout
        bottom_layout = QHBoxLayout()
        bottom_layout.addWidget(QPushButton("OK"))
        bottom_layout.addWidget(QPushButton("Cancel"))
        
        # Add nested layouts to main layout
        main_layout.addLayout(top_layout)
        main_layout.addLayout(middle_layout)
        main_layout.addStretch()
        main_layout.addLayout(bottom_layout)
        
        widget.setLayout(main_layout)
        return widget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())