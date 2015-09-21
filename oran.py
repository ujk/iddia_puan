# ujk 150919

from PyQt5 import QtCore, QtGui, QtWidgets
from oran_ui import *

import itertools

kolonCount = 0
sistemCount = 0

def kRadioClicked(self,pos):
	global kolonCount
	
	if ui.k3Radio.isChecked():
		kolonCount = 3
	elif ui.k4Radio.isChecked():
		kolonCount = 4
	elif ui.k5Radio.isChecked():
		kolonCount = 5
	else:
		kolonCount = 0
		
	hesap()
	
	
def sRadioClicked(self,pos):
	global sistemCount
	
	if ui.s3Radio.isChecked():
		sistemCount = 3
	elif ui.s4Radio.isChecked():
		sistemCount = 4
	elif ui.s5Radio.isChecked():
		sistemCount = 5
	else:
		sistemCount = 0
		
	hesap()
	
	
def hesap():
	global kolonCount, sistemCount
	
	ui.resultEdit.clear()
	ui.resultEdit.append("%d kolon oynanmış" % kolonCount)
	
	if (sistemCount == 0 or kolonCount <= sistemCount) and kolonCount >= 3:
		ui.resultEdit.append("sistem oynanmamış")
		oran = 1.0
		for i in range(1,kolonCount+1):
			my_edit = getattr(ui, "oran%dEdit" % i)
			oran *= float(my_edit.text())
		ui.resultEdit.append("TOPLAM ORAN = %10.2f" % oran)
	elif sistemCount >= 3 and kolonCount > sistemCount:
		orans = []
		for i in range(1,kolonCount+1):
			my_edit = getattr(ui, "oran%dEdit" % i)
			orans.append(float(my_edit.text()))
		combies = list(itertools.combinations(orans,sistemCount))
		oranNr = 1
		toplam = 0.0
		for i in combies:
			oran = 1.0
			for j in i:
				oran *= j
			ui.resultEdit.append("ORAN - %d = %10.2f" % (oranNr, oran))
			oranNr += 1
			toplam += oran
		ui.resultEdit.append("\nORANLAR TOPLAMI = %10.2f" % toplam)
	else:
		ui.resultEdit.append("Seçimler Yanlış")
	
	
QtWidgets.QWidget.kRadioClicked = kRadioClicked
QtWidgets.QWidget.sRadioClicked = sRadioClicked

import sys
app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()
sys.exit(app.exec_())

