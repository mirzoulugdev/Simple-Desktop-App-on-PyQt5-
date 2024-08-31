from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox

#Pages
from loginPage import LogInPage
from registerPage import RegisterPage
from mainPage import MainPage
from mainBlogPage import BlogPage

#Database
from database import Database



#System
from os import system
system('clear')

class App:
    def __init__(self):
        
        #Windows
        self.loginPage = LogInPage()
        self.registerPage = RegisterPage()
        self.mainPage = MainPage()
        self.blogPage = BlogPage()

        #Database
        self.database = Database()



        self.mainPage.registerButton.clicked.connect(self.registerPageShow)
        self.mainPage.signInButton.clicked.connect(self.signInPageShow)

        self.registerPage.backIconButton.clicked.connect(self.backToMainPage)
        self.loginPage.backIconButton.clicked.connect(self.backToMainPage)

        self.registerPage.registerButton.clicked.connect(self.register)
        
        self.loginPage.loginButton.clicked.connect(self.login)

        self.mainPage.show()

    def registerPageShow(self):
        self.registerPage.show()
        self.mainPage.close()

    def signInPageShow(self):
        self.loginPage.show()
        self.mainPage.close()

    def backToMainPage(self):
        self.mainPage.show()
        self.loginPage.close()
        self.registerPage.close()

    def register(self):
        username = self.registerPage.usernameInput.text()
        email = self.registerPage.emailInput.text()
        phoneNumber = self.registerPage.phoneNumberInput.text()
        password = self.registerPage.passwordInput.text()

        value = self.database.register(username, email, phoneNumber, password)
  
        if value:
            self.alert("Muvaffaqiyatli ro'yxatdan o'tdingiz!!!")
            self.loginPage.show()
            self.registerPage.close()

    def login(self):
        email = self.loginPage.emailInput.text()
        password = self.loginPage.passwordInput.text()

        foundUser = self.database.login(email, password)

        if not foundUser:
            return self.alert("User topilmadi!")
        elif foundUser:
            self.blogPage.show()
            self.loginPage.close()


    def alert(self, title: str):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(title)
        return msg.exec()


app = QApplication([])
window = App()

app.exec()