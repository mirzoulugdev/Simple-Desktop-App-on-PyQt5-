from PyQt5.QtWidgets import QLabel, QPushButton, QLineEdit, QWidget
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize


class MainLabel(QLabel):
    def __init__(self, window: QWidget, title: str, y: int):
        super().__init__(window)

        self.setText(title)
        self.move(121, y)
        self.setStyleSheet("""
            color: white;
            font-size: 35px;
            font-weight: bold;
            background-color: None;
        """)

class Label(QLabel):
    def __init__(self, window: QWidget, text: str, y: int):
        super().__init__(window)

        self.setText(text)
        self.move(81, y)
        self.setStyleSheet("""
            font-size: 22px;
            color: #C4C4C4;
            background-color: None;
            
        """)

class AccountLabel(QLabel):
    def __init__(self, window: QWidget, txt: str, x: int, y: int):
        super().__init__(window)

        self.setText(txt)
        self.move(x, y)
        self.setStyleSheet("""
            color: white;
            font-size: 16px
            
          
        """)



class InputText(QLabel):
    def __init__(self, window: QWidget, text: str, y: int):
        super().__init__(window)

        self.setText(text)
        self.move(30, y)
        self.setStyleSheet("""
            font-size: 20px;
            color: white
            
        """)

class Input(QLineEdit):
    def __init__(self, window: QWidget, placeHolderText: str, y: int):
        super().__init__(window)
        self.setGeometry(30, y, 315, 48)
        self.setPlaceholderText("  " + placeHolderText)
        self.setStyleSheet("""
                background-color: #FEFCFC;
                font-size: 18px;
                border-radius: 8px;
        """)


class Button(QPushButton):
    def __init__(self, window: QWidget, text: str, y: int):
        super().__init__(window)
        self.setGeometry(40, y, 295, 48)
        self.setText(text)
        self.setStyleSheet("""
            QPushButton{
                background-color: #29B6F6;
                color: white;
                font-size: 22px;
                font-weight: bold;
                border-radius: 22px
            }

            QPushButton::hover{
                background-color: #61c5f2;
                color: white; 
            }
                           
            QPushButton::pressed{
                background-color: white;
                color: #03b0ff; 
            }
        """)

class SocialIcon(QPushButton):
    def __init__(self, window: QWidget, path: str, x: int, y:int):
        super().__init__(window)
        self.setGeometry(x, y, 70, 60)
       
        self.setIcon(QIcon(path))
        self.setIconSize(QSize(45, 45))
        self.setFixedSize(50, 50)
        self.setStyleSheet("""
            QPushButton{
                background-color: None;
                border: None;
            }
                    
            QPushButton::pressed{
                background-color: grey;
                border-radius: 20px;
                                          
            }
        """)

     