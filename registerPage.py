#PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap

#System
from os import system
system('clear')

#Components
from components import MainLabel, Label, InputText, Input, Button, SocialIcon, AccountLabel


class RegisterPage(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(375, 750)
        self.setWindowTitle("Register")
        self.setStyleSheet("""
            background-color: black;
        """)
        self.setWindowIcon(QIcon("assets/home.png"))
        self.background_label = QLabel(self)
        pixmap = QPixmap("assets/background.png") 
        self.background_label.setPixmap(pixmap)
        self.background_label.setScaledContents(True)
        self.background_label.resize(375, 250)

        self.backIconButton = SocialIcon(self, "assets/back.png", 15, 25)

        self.welcomeLabel = MainLabel(self, "Register", 100)
        self.smallLabel = Label(self, "Create a new account", 140)

        self.usernameText = InputText(self, "Username", 200)
        self.usernameInput = Input(self, "Username", 235)

        self.emailText = InputText(self, "Email", 300)
        self.emailInput = Input(self, "Email", 335)

        self.phoneNumberText = InputText(self, "Mobile Number", 400)
        self.phoneNumberInput = Input(self, "Mobile Number", 435)

        self.passwordText = InputText(self, "Password", 500)
        self.passwordInput = Input(self, "Password", 535)

        self.registerButton = Button(self, "Register", 640)

        self.accountLabel = AccountLabel(self, "Don't have an account?", 50, 700)
        self.accountLabel = AccountLabel(self, "Create Now", 230, 700)






