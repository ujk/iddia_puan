# -*- coding: utf-8 -*-

# ujk 150913

from PyQt5 import QtCore, QtGui, QtWidgets
from main_ui import *
from resEkran_ui import *

lines = []
resHomeNr = 0
resVisitorNr = 0
resHomeScore = 0
resVisitorScore = 0
fileName = ""

teamLabel = []     #takım isimleri
evgLabel = []      #ev galibiyetleri
depgLabel = []     #deplasman galibiyetleri
evbLabel = []      #ev beraberlikleri
depbLabel = []     #deplasman beraberlikleri
atLabel = []       #attığı gol
yeLabel = []       #yediği gol
puanLabel = []     #iddia puanı

def selectLig(self,selection):
	global lines
	global fileName
	global teamLabel     #takım isimleri
	global evgLabel      #ev galibiyetleri
	global depgLabel     #deplasman galibiyetleri
	global evbLabel      #ev beraberlikleri
	global depbLabel     #deplasman beraberlikleri
	global atLabel       #attığı gol
	global yeLabel       #yediği gol
	global puanLabel     #iddia puanı

	if selection == "Türkiye Süper Lig":
		fileName = "turkiye.txt"
	else:
		fileName = "turkiye.txt"
	file = open(fileName,'r')
	lines = file.readlines()
	file.close()
	length = len(lines)
	for i in range(0,length):
		splitted = lines[i].split(",")
		teamLabel.append(QtWidgets.QLabel(splitted[0]))
		ui.gridLayout.addWidget(teamLabel[i],i+2,0)
		evgLabel.append(QtWidgets.QLabel(splitted[1]))
		ui.gridLayout.addWidget(evgLabel[i],i+2,1)
		evgLabel[i].setAlignment(QtCore.Qt.AlignCenter)
		depgLabel.append(QtWidgets.QLabel(splitted[2]))
		ui.gridLayout.addWidget(depgLabel[i],i+2,2)
		depgLabel[i].setAlignment(QtCore.Qt.AlignCenter)
		evbLabel.append(QtWidgets.QLabel(splitted[3]))
		ui.gridLayout.addWidget(evbLabel[i],i+2,3)
		evbLabel[i].setAlignment(QtCore.Qt.AlignCenter)
		depbLabel.append(QtWidgets.QLabel(splitted[4]))
		ui.gridLayout.addWidget(depbLabel[i],i+2,4)
		depbLabel[i].setAlignment(QtCore.Qt.AlignCenter)
		atLabel.append(QtWidgets.QLabel(splitted[5]))
		ui.gridLayout.addWidget(atLabel[i],i+2,5)
		atLabel[i].setAlignment(QtCore.Qt.AlignCenter)
		yeLabel.append(QtWidgets.QLabel(splitted[6]))
		ui.gridLayout.addWidget(yeLabel[i],i+2,6)
		yeLabel[i].setAlignment(QtCore.Qt.AlignCenter)
		puanLabel.append(QtWidgets.QLabel(splitted[7].rstrip()))
		ui.gridLayout.addWidget(puanLabel[i],i+2,7)
		puanLabel[i].setAlignment(QtCore.Qt.AlignCenter)
		
		ui.resEntryButton.setEnabled(True)
		if i%2==0:
			teamLabel[i].setStyleSheet("background-color: lime; font: 10pt;")
			evgLabel[i].setStyleSheet("background-color: lime; font: 10pt;")
			depgLabel[i].setStyleSheet("background-color: lime; font: 10pt;")
			evbLabel[i].setStyleSheet("background-color: lime; font: 10pt;")
			depbLabel[i].setStyleSheet("background-color: lime; font: 10pt;")
			atLabel[i].setStyleSheet("background-color: lime; font: 10pt;")
			yeLabel[i].setStyleSheet("background-color: lime; font: 10pt;")
			puanLabel[i].setStyleSheet("background-color: lime; font: 10pt;")
		else:
			teamLabel[i].setStyleSheet("background-color: white; font: 10pt;")
			evgLabel[i].setStyleSheet("background-color: white; font: 10pt;")
			depgLabel[i].setStyleSheet("background-color: white; font: 10pt;")
			evbLabel[i].setStyleSheet("background-color: white; font: 10pt;")
			depbLabel[i].setStyleSheet("background-color: white; font: 10pt;")
			atLabel[i].setStyleSheet("background-color: white; font: 10pt;")
			yeLabel[i].setStyleSheet("background-color: white; font: 10pt;")
			puanLabel[i].setStyleSheet("background-color: white; font: 10pt;")



def resEntry(self,pos):
	global lines
	global resHomeNr
	global resVisitorNr
	global resHomeScore
	global resVisitorScore
	
	dialog = QtWidgets.QDialog()
	dialog.ui = Ui_resEntryDialog()
	dialog.ui.setupUi(dialog)
	dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
	
	for i in range(0,len(lines)):
		name = lines[i].split(",")[0]
		dialog.ui.homeCombo.addItem(name)
		dialog.ui.homeCombo.setCurrentIndex(-1)
		dialog.ui.visitorCombo.addItem(name)
		dialog.ui.visitorCombo.setCurrentIndex(-1)
		
	if dialog.exec_() == 1:
		if resHomeNr>=0 and resVisitorNr>=0:             #bir skor girilmiş
			homestr = lines[resHomeNr].split(",")
			visitorstr = lines[resVisitorNr].split(",")
			if resHomeScore > resVisitorScore:
				homestr[1] = str(int(homestr[1])+1)
			if resHomeScore < resVisitorScore:
				visitorstr[2] = str(int(visitorstr[2])+1)
			if resHomeScore == resVisitorScore:
				homestr[3] = str(int(homestr[3])+1)
				visitorstr[4] = str(int(visitorstr[4])+1)
			homestr[5] = str(int(homestr[5])+resHomeScore)
			visitorstr[5] = str(int(visitorstr[5])+resVisitorScore)
			homestr[6] = str(int(homestr[6])+resVisitorScore)
			visitorstr[6] = str(int(visitorstr[6])+resHomeScore)
			puan = int(homestr[1])*2 + int(homestr[2])*4 + int(homestr[3])*1 + int(homestr[4])*2
			if int(homestr[5]) > int(homestr[6]):
				puan += (int(homestr[1]) + int(homestr[2]) + int(homestr[3]) + int(homestr[4])) * 1
			homestr[7] = str(puan) + "\n"
			puan = int(visitorstr[1])*2 + int(visitorstr[2])*4 + int(visitorstr[3])*1 + int(visitorstr[4])*2
			if int(visitorstr[5]) > int(visitorstr[6]):
				puan += (int(visitorstr[1]) + int(visitorstr[2]) + int(visitorstr[3]) + int(visitorstr[4])) * 1
			visitorstr[7] = str(puan) + "\n"
			lines[resHomeNr] = ",".join(homestr)
			lines[resVisitorNr] = ",".join(visitorstr)
			ui.printResults()
			ui.saveButton.setEnabled(True)
			
			
def resChanged(self,index):
	global resHomeNr
	global resVisitorNr
	global resHomeScore
	global resVisitorScore
	resHomeNr = self.ui.homeCombo.currentIndex()
	resVisitorNr = self.ui.visitorCombo.currentIndex()
	resHomeScore = self.ui.homeSpin.value()
	resVisitorScore = self.ui.visitorSpin.value()



def printResults():
	global lines
	global teamLabel     #takım isimleri
	global evgLabel      #ev galibiyetleri
	global depgLabel     #deplasman galibiyetleri
	global evbLabel      #ev beraberlikleri
	global depbLabel     #deplasman beraberlikleri
	global atLabel       #attığı gol
	global yeLabel       #yediği gol
	global puanLabel     #iddia puanı

	for i in range(0,len(lines)):
		line = lines[i].split(",")
		teamLabel[i].setText(line[0])
		evgLabel[i].setText(line[1])
		depgLabel[i].setText(line[2])
		evbLabel[i].setText(line[3])
		depbLabel[i].setText(line[4])
		atLabel[i].setText(line[5])
		yeLabel[i].setText(line[6])
		puanLabel[i].setText(line[7].rstrip())


def saveTable(self,pos):
	global lines
	global fileName
	
	file = open(fileName,'w')
	file.writelines(lines)
	file.close()
	ui.saveButton.setEnabled(False)
	

QtWidgets.QDialog.resChanged = resChanged	
QtWidgets.QWidget.resEntry = resEntry
QtWidgets.QWidget.selectLig = selectLig
QtWidgets.QWidget.saveTable = saveTable

import sys
app = QtWidgets.QApplication(sys.argv)
mainForm = QtWidgets.QWidget()
ui = Ui_mainForm()
ui.setupUi(mainForm)
ui.printResults = printResults	
mainForm.move(50,50)
mainForm.show()
sys.exit(app.exec_())

