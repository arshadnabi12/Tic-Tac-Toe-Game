import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets,QtGui
from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MainWidow(QDialog):
	def __init__(self):		
		super(MainWidow,self).__init__()
		loadUi("pblui_screen1.ui",self)
		self.pushButton.clicked.connect(self.gotoscreen2)
		self.pushButton_2.clicked.connect(self.gotoexit)
	def gotoscreen2(self):
		widget.setCurrentIndex(widget.currentIndex()+1)
	def gotoexit(self):
		sys.exit(0)
class Screen2(QDialog):
	def __init__(self):
		super().__init__()

		self.uicomponents()
	def uicomponents(self):
		self.turn=0
		self.times=0
		self.buttonlist=[]
		for i in range(3):
			temp=[]
			for i in range(3):
				temp.append((QPushButton(self)))
			self.buttonlist.append(temp)
		for i in range(3):
			for j in range(3):
				self.buttonlist[i][j].setGeometry(90*i+400,90*j+200,80,80)
				self.buttonlist[i][j].setStyleSheet("background-color: rgb(0, 0, 0);")
				self.buttonlist[i][j].clicked.connect(self.action_called)
				font=QtGui.QFont()
				font.setPointSize(20)
				self.buttonlist[i][j].setFont(font)
		self.label=QLabel(self)
		self.label.setGeometry(200,480,700,70)
		self.label.setStyleSheet("QLabel" "{" "background-color:white;" "border:black" "}")
		self.label.setAlignment(Qt.AlignCenter)
	
		reset_game=QPushButton("Reset",self)
		reset_game.setGeometry(400,550,100,50)
		reset_game.setStyleSheet("background:rgb(0,255,0)")
		reset_game.clicked.connect(self.reset_action)
		back=QPushButton("Go back",self)
		back.setGeometry(550,550,100,50)
		back.setStyleSheet("background-color: rgb(85, 85, 255)")
		back.clicked.connect(self.go)
	def go(self):
		widget.setCurrentIndex(widget.currentIndex()-1)
	def reset_action(self):
		# resetting values
		self.turn = 0
		self.times = 0

		# making label text empty:
		self.label.setText("")


		# traversing push list
		for buttons in self.buttonlist:
			for button in buttons:
				# making all the button enabled
				button.setEnabled(True)
				# removing text of all the buttons
				button.setText("")
	
	def action_called(self):

		self.times += 1

		# getting button which called the action
		button = self.sender()

		# making button disabled
		button.setEnabled(False)

		# checking the turn
		if self.turn == 0:
			button.setText("X")
			
			self.turn = 1
		else:
			button.setText("O")
			self.turn = 0

		# call the winner checker method
		win = self.who_wins()
		
		# text
		text = ""

		# if winner is decided
		if win == True:
			# if current chance is 0
			if self.turn == 0:
				# O has won
				text="<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#55007f;\">Congratulations..player 'O'..!!  You won the game.</span></p></body></html>"
				
			# X has won
			else:
				text="<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#55007f;\">Congratulations..player 'X'..!!  You won the game.</span></p></body></html>"

			# disabling all the buttons
			for buttons in self.buttonlist:
				for push in buttons:
					push.setEnabled(False)

		# if winner is not decided
		# and total times is 9
		elif self.times == 9:
			text = text="<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#55007f;\">Matched drawed..!</span></p></body></html>"

		# setting text to the label
		self.label.setText(text)

	def who_wins(self):

		# checking if any row crossed
		for i in range(3):
			if self.buttonlist[0][i].text() == self.buttonlist[1][i].text() \
					and self.buttonlist[0][i].text() == self.buttonlist[2][i].text() \
					and self.buttonlist[0][i].text() != "":
				return True

		# checking if any column crossed
		for i in range(3):
			if self.buttonlist[i][0].text() == self.buttonlist[i][1].text() \
					and self.buttonlist[i][0].text() == self.buttonlist[i][2].text() \
					and self.buttonlist[i][0].text() != "":
				return True

		# checking if diagonal crossed
		if self.buttonlist[0][0].text() == self.buttonlist[1][1].text() \
				and self.buttonlist[0][0].text() == self.buttonlist[2][2].text() \
				and self.buttonlist[0][0].text() != "":
			return True

		# if other diagonal is crossed
		if self.buttonlist[0][2].text() == self.buttonlist[1][1].text() \
				and self.buttonlist[1][1].text() == self.buttonlist[2][0].text() \
				and self.buttonlist[0][2].text() != "":
			return True


		#if nothing is crossed
		return False
app=QApplication(sys.argv)
widget=QtWidgets.QStackedWidget()
mainwindow=MainWidow()
widget.addWidget(mainwindow)
screen2=Screen2()
widget.addWidget(screen2)
widget.setFixedHeight(920)
widget.setFixedWidth(1050)
widget.show()
sys.exit(app.exec_())