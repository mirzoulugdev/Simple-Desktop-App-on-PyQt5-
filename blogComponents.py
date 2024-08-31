from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QGroupBox, QVBoxLayout, QLineEdit, QTextEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt


class Label(QLabel):
    def __init__(self, window: QWidget, y: int, x: int, title: str, size: int):
        super().__init__(window)
        self.textSize = size
        self.move(x, y)
        self.setStyleSheet(f"""
            font-size: {self.textSize}px;
            font-weight: bold;
            
        """)
        self.setText(title)
        self.setAlignment(Qt.AlignCenter)
        self.adjustSize()


class OtherLabel(QLabel):
    def __init__(self, window: QWidget, y: int, x: int, text: str, size: int, color: str):
        super().__init__(window)
        self.color = color
        self.textSize = size

        self.move(x, y)
        self.setText(text)
        self.setStyleSheet(f"""
            font-size: {self.textSize}px;
            color: {self.color};
        """)
        self.setAlignment(Qt.AlignCenter)
        self.adjustSize()

class Button(QPushButton):
    def __init__(self, window, path, x, y, sizeA, sizeB):
        super().__init__(window)
        self.setIcon(QIcon(path))
        self.setIconSize(QSize(sizeA, sizeB))
        self.setFixedSize(sizeA, sizeB)
        self.setStyleSheet("background-color: None; border: None")
        self.move(x, y)

class ClickButton(QPushButton):
    def __init__(self, window, x, y, text):
        super().__init__(window)
        self.setGeometry(x, y, 150, 40)
        self.setText(text)
        self.setStyleSheet("""
            QPushButton{
                font-size: 18px;
                color: white;
                background-color: #7C4EE4;
                border-radius: 5px;
                border: 2px solid #7C4EE4;
            }
            QPushButton::hover{
                background-color: #9368f2;
            }
            QPushButton::pressed{
                background-color: white;
                color: #7C4EE4;
                border: 2px solid #7C4EE4;
            }
        """)        


class Cards(QGroupBox):
    def __init__(self, window, path: str, title: str, description: str):
        super().__init__(window)

        layout = QVBoxLayout()

        icon_label = QLabel()
        icon_label.setPixmap(QIcon(path).pixmap(48, 48))
        icon_label.setAlignment(Qt.AlignCenter)

        title_label = QLabel(title)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 20px; font-weight: bold;")


        description_label = QLabel(description)
        description_label.setAlignment(Qt.AlignCenter)
        description_label.setStyleSheet("font-size: 18px")


        layout.addWidget(icon_label)
        layout.addWidget(title_label)
        layout.addWidget(description_label)

        self.setLayout(layout)
        self.setStyleSheet("""
            QGroupBox {
                border: 1px solid #e0e0e0;
                border-radius: 10px;
                background-color: #f5f2f2;
                padding: 15px;
                margin: 10px;
            }
            QLabel {
                color: #6e6e6e;
            }
        """)

        self.setFixedSize(320, 250)

class Input(QLineEdit):
    def __init__(self, window, x, y, placeHolderText):
        super().__init__(window)
        self.setGeometry(x, y, 300, 50)
        self.setPlaceholderText(placeHolderText)
        self.setStyleSheet("""
            font-size: 20px;
            border-radius: 5px;
            border: 1px solid #e0dce8;
        """)


class TextArea(QTextEdit):
    def __init__(self, window, placeHolderText, x, y):
        super().__init__(window)
        self.setGeometry(x, y, 680, 80)
        self.setPlaceholderText(placeHolderText)
        self.setStyleSheet("border: 1px solid #e0dce8; border-radius: 5px; font-size: 20px")