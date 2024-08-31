#PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap

#System
from os import system
system('clear')

#Components
from components import MainLabel, Button, Label


class MainPage(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(375, 750)
        self.setWindowTitle("Main Page")
        self.setStyleSheet("""
            background-color: black;
        """)
        self.setWindowIcon(QIcon("assets/home.png"))
        
        self.background_label = QLabel(self)
        pixmap = QPixmap("assets/image.png") 
        self.background_label.setPixmap(pixmap)
        self.background_label.setScaledContents(True)
        self.background_label.resize(self.size())

        self.welcomeLabel = MainLabel(self, "Welcome", 170)
        self.bioLabel = Label(self, "Success breeds success.", 230)

        self.signInButton = Button(self, "Sign In", 370)
        self.registerButton = Button(self, "Register", 470)
 

