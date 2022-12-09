# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Qt.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import random
from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(816, 610)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.rockButton = QtWidgets.QPushButton(self.centralwidget)
        self.rockButton.setGeometry(QtCore.QRect(40, 420, 221, 101))
        self.rockButton.setObjectName("rockButton")
        self.paperButton = QtWidgets.QPushButton(self.centralwidget)
        self.paperButton.setGeometry(QtCore.QRect(280, 420, 221, 101))
        self.paperButton.setObjectName("paperButton")
        self.scissorButton = QtWidgets.QPushButton(self.centralwidget)
        self.scissorButton.setGeometry(QtCore.QRect(540, 420, 221, 101))
        self.scissorButton.setObjectName("scissorButton")
        self.main_text = QtWidgets.QLabel(self.centralwidget)
        self.main_text.setGeometry(QtCore.QRect(210, 90, 371, 81))
        font = QtGui.QFont()
        font.setPointSize(33)
        self.main_text.setFont(font)
        self.main_text.setTextFormat(QtCore.Qt.AutoText)
        self.main_text.setObjectName("main_text")
        self.side_label = QtWidgets.QLabel(self.centralwidget)
        self.side_label.setGeometry(QtCore.QRect(340, 160, 200, 16))
        self.side_label.setObjectName("side_label")
        self.main_image = QtWidgets.QLabel(self.centralwidget)
        self.main_image.setGeometry(QtCore.QRect(20, 190, 781, 211))
        self.main_image.setText("")
        self.main_image.setPixmap(QtGui.QPixmap("test.png"))
        self.main_image.setObjectName("main_image")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 816, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.rockButton.clicked.connect(self.rockButton_command)
        self.paperButton.clicked.connect(self.paperButton_command)
        self.scissorButton.clicked.connect(self.scissorButton_command)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rock, Paper, Scissors!"))
        self.rockButton.setText(_translate("MainWindow", "Rock"))
        self.paperButton.setText(_translate("MainWindow", "Paper"))
        self.scissorButton.setText(_translate("MainWindow", "Scissors"))
        self.main_text.setText(_translate("MainWindow", "Choose your hand!"))
        self.side_label.setText(_translate("MainWindow", "(AI on left, User on right)"))

    

    def rockButton_command(self):
        result_a = "user_rock_win"
        result_b = "user_paper_win"
        result_c = "user_scissors_win"
        result_d = "ai_rock_win"
        result_e = "ai_paper_win"
        result_f = "ai_scissors_win"
        result_g = "rock_tie"
        result_h = "paper_tie"
        result_i = "scissors_tie"
        print ("You chose: Rock")
        #self.main_image.setPixmap(QtGui.QPixmap("user_rock_win.png"))
        verdict = game("rock")
        if verdict == result_a:
            self.main_image.setGeometry(QtCore.QRect(170, 190, 781, 211))
            self.main_image.setPixmap(QtGui.QPixmap("user_rock_win"))
        
        elif verdict == result_b:
            self.main_image.setGeometry(QtCore.QRect(170, 190, 781, 211))
            self.main_image.setPixmap(QtGui.QPixmap("user_paper_win"))
            
        elif verdict == result_c:
            self.main_image.setGeometry(QtCore.QRect(170, 190, 781, 211))
            self.main_image.setPixmap(QtGui.QPixmap("user_scissors_win"))
            
        elif verdict == result_d:
            self.main_image.setGeometry(QtCore.QRect(170, 190, 781, 211))
            self.main_image.setPixmap(QtGui.QPixmap("ai_rock_win"))
            
        elif verdict == result_e:
            self.main_image.setGeometry(QtCore.QRect(170, 190, 781, 211))
            self.main_image.setPixmap(QtGui.QPixmap("ai_paper_win"))
            
        elif verdict == result_f:
            self.main_image.setGeometry(QtCore.QRect(170, 190, 781, 211))
            self.main_image.setPixmap(QtGui.QPixmap("ai_scissors_win"))
            
        elif verdict == result_g:
            self.main_image.setGeometry(QtCore.QRect(170, 190, 781, 211))
            self.main_image.setPixmap(QtGui.QPixmap("rock_tie"))
            
        elif verdict == result_h:
            self.main_image.setGeometry(QtCore.QRect(170, 190, 781, 211))
            self.main_image.setPixmap(QtGui.QPixmap("paper_tie"))
            
        elif verdict == result_i:
            self.main_image.setGeometry(QtCore.QRect(170, 190, 781, 211))
            self.main_image.setPixmap(QtGui.QPixmap("scissors_tie"))
        
    def paperButton_command(self):
        result_a = "user_rock_win"
        result_b = "user_paper_win"
        result_c = "user_scissors_win"
        result_d = "ai_rock_win"
        result_e = "ai_paper_win"
        result_f = "ai_scissors_win"
        result_g = "rock_tie"
        result_h = "paper_tie"
        result_i = "scissors_tie"
        print ("You chose: Paper")
        
        verdict = game("paper")
        if verdict == result_a:
            self.main_image.setGeometry(QtCore.QRect(170, 190, 781, 211))
            self.main_image.setPixmap(QtGui.QPixmap("user_rock_win"))
        
        elif verdict == result_b:
            self.main_image.setGeometry(QtCore.QRect(170, 190, 781, 211))
            self.main_image.setPixmap(QtGui.QPixmap("user_paper_win"))
            
        elif verdict == result_c:
            self.main_image.setGeometry(QtCore.QRect(170, 190, 781, 211))
            self.main_image.setPixmap(QtGui.QPixmap("user_scissors_win"))
            
        elif verdict == result_d:
            self.main_image.setGeometry(QtCore.QRect(170, 190, 781, 211))
            self.main_image.setPixmap(QtGui.QPixmap("ai_rock_win"))
            
        elif verdict == result_e:
            self.main_image.setGeometry(QtCore.QRect(170, 190, 781, 211))
            self.main_image.setPixmap(QtGui.QPixmap("ai_paper_win"))
            
        elif verdict == result_f:
            self.main_image.setGeometry(QtCore.QRect(170, 190, 781, 211))
            self.main_image.setPixmap(QtGui.QPixmap("ai_scissors_win"))
            
        elif verdict == result_g:
            self.main_image.setGeometry(QtCore.QRect(170, 190, 781, 211))
            self.main_image.setPixmap(QtGui.QPixmap("rock_tie"))
            
        elif verdict == result_h:
            self.main_image.setGeometry(QtCore.QRect(170, 190, 781, 211))
            self.main_image.setPixmap(QtGui.QPixmap("paper_tie"))
            
        elif verdict == result_i:
            self.main_image.setGeometry(QtCore.QRect(170, 190, 781, 211))
            self.main_image.setPixmap(QtGui.QPixmap("scissors_tie"))

    def scissorButton_command(self):
        result_a = "user_rock_win"
        result_b = "user_paper_win"
        result_c = "user_scissors_win"
        result_d = "ai_rock_win"
        result_e = "ai_paper_win"
        result_f = "ai_scissors_win"
        result_g = "rock_tie"
        result_h = "paper_tie"
        result_i = "scissors_tie"
        print ("You chose: Scissors")
        verdict = game("scissors")
        
        if verdict == result_a:
            self.main_image.setGeometry(QtCore.QRect(170, 190, 781, 211))
            self.main_image.setPixmap(QtGui.QPixmap("user_rock_win"))
        
        elif verdict == result_b:
            self.main_image.setGeometry(QtCore.QRect(170, 190, 781, 211))
            self.main_image.setPixmap(QtGui.QPixmap("user_paper_win"))
            
        elif verdict == result_c:
            self.main_image.setGeometry(QtCore.QRect(170, 190, 781, 211))
            self.main_image.setPixmap(QtGui.QPixmap("user_scissors_win"))
            
        elif verdict == result_d:
            self.main_image.setGeometry(QtCore.QRect(170, 190, 781, 211))
            self.main_image.setPixmap(QtGui.QPixmap("ai_rock_win"))
            
        elif verdict == result_e:
            self.main_image.setGeometry(QtCore.QRect(170, 190, 781, 211))
            self.main_image.setPixmap(QtGui.QPixmap("ai_paper_win"))
            
        elif verdict == result_f:
            self.main_image.setGeometry(QtCore.QRect(170, 190, 781, 211))
            self.main_image.setPixmap(QtGui.QPixmap("ai_scissors_win"))
            
        elif verdict == result_g:
            self.main_image.setGeometry(QtCore.QRect(170, 190, 781, 211))
            self.main_image.setPixmap(QtGui.QPixmap("rock_tie"))
            
        elif verdict == result_h:
            self.main_image.setGeometry(QtCore.QRect(170, 190, 781, 211))
            self.main_image.setPixmap(QtGui.QPixmap("paper_tie"))
            
        elif verdict == result_i:
            self.main_image.setGeometry(QtCore.QRect(170, 190, 781, 211))
            self.main_image.setPixmap(QtGui.QPixmap("scissors_tie"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    def game(choice):
        user_score = 0
        ai_score = 0
        possible_moves = ["rock", "paper", "scissors"]
        result_a = "user_rock_win"
        result_b = "user_paper_win"
        result_c = "user_scissors_win"
        result_d = "ai_rock_win"
        result_e = "ai_paper_win"
        result_f = "ai_scissors_win"
        result_g = "rock_tie"
        result_h = "paper_tie"
        result_i = "scissors_tie"

        computer_action = random.choice(possible_moves)

        if computer_action == "rock":
            if choice == "rock":
                print("You Tie!")
                return result_g
            elif choice == "paper":
                print("You Won!")
                return result_b
                user_score += 1
            else:
                print("You Lost!")
                ai_score += 1
                return result_d
        elif computer_action == "paper":
            if choice == "rock":
                print("You Lost!")
                ai_score += 1
                return result_e
            elif choice == "paper":
                print("You Tie!")
                return result_h
            else:
                print("You Won!")
                user_score += 1
                return result_c
        else:
            if choice == "rock":
                print("You Won!")
                user_score += 1
                return result_a
            elif choice == "paper":
                print("You Lost!")
                ai_score += 1
                return result_f
            else:
                print("You Tie!")
                return result_i
                
    sys.exit(app.exec_())
