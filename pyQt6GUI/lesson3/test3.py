from PyQt6.QtWidgets import (QApplication,
                             QMainWindow,
                             QVBoxLayout,
                             QHBoxLayout,
                             QPushButton,
                             QLabel
)

import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ArmarX")
        self.setGeometry(100, 100, 600, 400)

        self.create_main_layout()


        # Example: Main application window layout
    def create_main_layout(self):
        # Main vertical layout
        main_layout = QVBoxLayout()
        
        # Menu bar (horizontal)
        menu_layout = QHBoxLayout()
        menu_layout.addWidget(QPushButton("File"))
        menu_layout.addWidget(QPushButton("Edit"))
        menu_layout.addWidget(QPushButton("View"))
        menu_layout.addWidget(QPushButton("Help"))
        main_layout.addLayout(menu_layout)
        
        # Content area (horizontal split)
        content_layout = QHBoxLayout()
        
        # Left sidebar (vertical)
        sidebar_layout = QVBoxLayout(self)
        sidebar_layout.addWidget(QLabel("Navigation"))
        sidebar_layout.addWidget(QPushButton("Dashboard"))
        sidebar_layout.addWidget(QPushButton("Messages"))
        sidebar_layout.addWidget(QPushButton("Settings"))
        sidebar_layout.addStretch()
        content_layout.addLayout(sidebar_layout, 1)  # 1 part width
        
        # Main content area (vertical)
        main_content_layout = QVBoxLayout()
        main_content_layout.addWidget(QLabel("Main Content Area"))
        # Add your main content widgets here
        main_content_layout.addStretch()
        content_layout.addLayout(main_content_layout, 3)  # 3 parts width
        
        main_layout.addLayout(content_layout, 1)  # 1 part height
        
        # Status bar (horizontal)
        status_layout = QHBoxLayout()
        status_layout.addWidget(QLabel("Ready"))
        status_layout.addStretch()
        status_layout.addWidget(QLabel("2023"))
        main_layout.addLayout(status_layout)
        
        self.setLayout(main_content_layout)
    
app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())