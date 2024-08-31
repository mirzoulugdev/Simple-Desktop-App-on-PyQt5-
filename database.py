#JSON
from json import dumps,loads

#PyQt5
from PyQt5.QtWidgets import QMessageBox

# #Errors
# from errors import UserAlreadyExist


class Database: 
    def __init__(self):
        self.usersFile = open("./database/users.json", "r+", encoding='utf-8')

    def selectUsers(self) -> list:
        self.rewind()
        users = loads(self.usersFile.read())
        return users
    
    def selectUsername(self, username: str) -> dict | None:
        users = self.selectUsers()

        user = list(filter(lambda user: user["username"] == username, users)) 
        
        return user if user else None
    
    def selectEmail(self, email: str) -> dict | None:
        users = self.selectUsers()

        user = list(filter(lambda user: user["email"] == email, users)) 
        
        return user if user else None
    
    
    
    def register(self, username: str, email: str, phoneNumber: str, password: str):

        foundUsername = self.selectUsername(username)
        foundEmail = self.selectEmail(email)

        if foundUsername:
            return self.alert("Username allaqachon tizimda mavjud!")
        
        if foundEmail:
            return self.alert("Ushbu email tizimda mavjud!")
        
        if len(phoneNumber) != 9:
            return self.alert("Telefon raqam uzunligi 9 tadan kam bo'lmasligi kerak!")
        elif not phoneNumber.startswith(("97", '99', '93', '91', '90', '88', '77', '50')):
            return self.alert("Noto'g'ri telefon raqam kiritdingiz!")
        
        if len(password) < 8:
            return self.alert("Parol 8 tadan kam bo'lmasligi kerak!")
        
        newUser = {
            "username": username,
            "email": email,
            "phoneNumber": phoneNumber,
            "password": password
        }

        USERS = self.selectUsers()
        USERS.append(newUser)

        self.rewind()

        data = dumps(USERS, indent=4)

        self.usersFile.write(data)

        return newUser
    

    def login(self, email: str, password: str):
        
        users = self.selectUsers()
        user = list(filter(lambda user: user["email"] == email and user["password"] == password, users))
        return user if user else None
        





    def alert(self, message: str):
        msg = QMessageBox()
        msg.move(170, 50)
        msg.setInformativeText(message)
        msg.setIcon(QMessageBox.Critical)
        # msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()

    

    def rewind(self):
        self.usersFile.seek(0, 0)
