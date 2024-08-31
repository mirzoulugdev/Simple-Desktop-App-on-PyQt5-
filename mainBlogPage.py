#PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt

#Components
from blogComponents import Label, OtherLabel, Button, ClickButton, Cards, Input, TextArea

#System
from os import system
system('clear')

class BlogPage(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1000, 1000)
        self.setWindowTitle("Zarrin")
        self.setWindowIcon(QIcon("assets/zarrinIcon.png"))
        
        self.backgroundLabel = QLabel(self)
        pixmap = QPixmap("assets/backgroundImage.png")
        self.backgroundLabel.setPixmap(pixmap)
        self.backgroundLabel.setScaledContents(True)
        self.backgroundLabel.resize(self.size())

       
    

        self.mainIcon = Button(self, "assets/Zarrin.png", 30, 15, 40, 40)
        self.IconLabel = Label(self, 20, 90, "Zarrin", size=28)
        self.blogLabel = OtherLabel(self, 20, 550, "Blog", 20, '#7C4EE4')
        self.aboutLabel = OtherLabel(self, 20, 640, "About", 20, '#333333')
        self.searchIcon = Button(self, "assets/search.png", x=730, y=20, sizeA=20, sizeB=20)
        self.clickButton = ClickButton(self, 800, 10, "Contact Us") 

        self.centerLabel = Label(self, 150, 390, "Get in Touch", 35)   

        self.descriptionLabel = OtherLabel(self, 220, 260, "Contact us to publish your content and show ads to our", 20, "#757575") 

        self.descriptionLabel2 = OtherLabel(self, 250, 370, "website and get a good reach.", 20, "#757575")  


        cards_layout = QHBoxLayout()

        office_card = Cards(self, "assets/round.png", "Office", "Victoria Street, London, UK")
        email_card = Cards(self, "assets/envelope.png", "Email", "hello@zarrin.com")
        phone_card = Cards(self, "assets/phone-call.png", "Phone", "(001) 2342 3451")

        cards_layout.addWidget(office_card)
        cards_layout.addWidget(email_card)
        cards_layout.addWidget(phone_card)
        self.setLayout(cards_layout)

        self.contactUs = Label(self, 670, 400, "Contact Us", 35)
        self.nameLabel = OtherLabel(self, 720, 70, "Name", 18, 'black')
        self.nameInput = Input(self, 70, 750, "Name...")

        self.emailLabel = OtherLabel(self, 720, 450, "Email", 18, 'black')
        self.emailInput = Input(self, 450, 750, "Email...")

        self.message = OtherLabel(self, 820, 70, "Message", 18, 'black')

        self.textArea = TextArea(self, "Message...", 70, 850)

        self.sendMessageButton = ClickButton(self, 800, 820, "Send Message")

        