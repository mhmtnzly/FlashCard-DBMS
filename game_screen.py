from PyQt5 import QtWidgets,uic
from PyQt5.QtCore import QCoreApplication,QTimer
import game
import menu
from user import User

class Game_Window(QtWidgets.QMainWindow):
    def __init__(self,username,password):
        self.username=username
        self.password=password
        super(Game_Window, self).__init__() 
        uic.loadUi('ui/gamescreen.ui', self)
        self.login_()
        self.pushButton.clicked.connect(self.menu_back)
        
    #     self.start=True #to start counter
    #     self.count=30 #counter 30 representing 3 seconds
    #     timer = QTimer(self)
    #     timer.timeout.connect(self.showTime)
    #     timer.start(100)
        
    # def showTime(self):
    #     if self.start:
    #         self.word.setStyleSheet("background-color: rgb(255, 255, 255,10);\n""color: rgb(0, 255, 0);") 
    #         if self.game.known_words<20:
    #             self.word.setText(self.game.flashcard()[0]) #to show dutch words
    #             self.count -= 1
    #             if self.count == -1:
    #                 self.start = False
    #                 self.true_button.clicked.connect(self.true_button_)
    #                 self.false_button.clicked.connect(self.false_button_)
    #                 self.word.setStyleSheet("background-color: rgb(255, 255, 255,10);\n""color: rgb(0, 0,255);")  
    #                 self.word.setText(self.game1.flashcard()[1]) #to show meaning of dutch words after 3 seconds
    #         else:
    #             self.word.setText("Gefeliciteerd") # after finishing level to show gefeliciteerd
    #             self.next_level.setVisible(True) #next level button activated
    #     if self.start:
    #         text = str(self.count/10) + " s"
    #         self.time_frame.setText(text)
    #     self.show()
    def menu_back(self):
        self.cams = menu.menu_window(self.username,self.password)
        self.cams.show() 
        self.close()
    def login_(self):
        self.user=User(self.username,self.password)
        if self.user.login():
            self.start_()
    def start_(self):
        self.game=game.Game(self.user.progress())
    def true_button_(self):
        if self.start == False:
            self.game.progress(True)
            self.twenty.setText(str(self.game.known_words))
            self.known_word.setText(str(self.game.total_words))
            self.time_improve()
    def false_button_(self):
        if self.start == False:
            self.game.progress(False)
            self.twenty.setText(str(self.game.known_words))
            self.known_word.setText(str(self.game.total_words))
            self.time_improve()
    
    