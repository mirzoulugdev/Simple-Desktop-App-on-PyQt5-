#PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap

#System
from os import system
system('clear')

#Components
from components import MainLabel, Label, InputText, Input, Button, SocialIcon, AccountLabel


class LogInPage(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(375, 750)
        self.setWindowTitle("Login")
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

        self.welcomeLabel = MainLabel(self, "Welcome", 170)
        self.smallLabel = Label(self, "Login to your account", 210)

        self.emailText = InputText(self, "Email", 300)
        self.emailInput = Input(self, "Email", 335)

        self.passwordText = InputText(self, "Password", 400)
        self.passwordInput = Input(self, "Password", 435)

        self.loginButton = Button(self, "Login", 540)

        self.accountLabel = AccountLabel(self, "Don't have an account?", 50, 600)
        self.accountLabel = AccountLabel(self, "Create Now", 230, 600)

        self.googleIconBtn = SocialIcon(self, "assets/google.png", 80, 680)
        self.facebookIconBtn = SocialIcon(self, "assets/facebook.png", 160, 680)
        self.instagramIconBtn = SocialIcon(self, "assets/instagram.png", 240, 680)


