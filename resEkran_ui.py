# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resEkran.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_resEntryDialog(object):
    def setupUi(self, resEntryDialog):
        resEntryDialog.setObjectName("resEntryDialog")
        resEntryDialog.resize(400, 186)
        self.buttonBox = QtWidgets.QDialogButtonBox(resEntryDialog)
        self.buttonBox.setGeometry(QtCore.QRect(40, 150, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(resEntryDialog)
        self.label.setGeometry(QtCore.QRect(40, 20, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(resEntryDialog)
        self.label_2.setGeometry(QtCore.QRect(240, 20, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.homeCombo = QtWidgets.QComboBox(resEntryDialog)
        self.homeCombo.setGeometry(QtCore.QRect(10, 50, 171, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.homeCombo.setFont(font)
        self.homeCombo.setObjectName("homeCombo")
        self.visitorCombo = QtWidgets.QComboBox(resEntryDialog)
        self.visitorCombo.setGeometry(QtCore.QRect(210, 50, 171, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.visitorCombo.setFont(font)
        self.visitorCombo.setObjectName("visitorCombo")
        self.homeSpin = QtWidgets.QSpinBox(resEntryDialog)
        self.homeSpin.setGeometry(QtCore.QRect(70, 90, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.homeSpin.setFont(font)
        self.homeSpin.setObjectName("homeSpin")
        self.visitorSpin = QtWidgets.QSpinBox(resEntryDialog)
        self.visitorSpin.setGeometry(QtCore.QRect(270, 90, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.visitorSpin.setFont(font)
        self.visitorSpin.setObjectName("visitorSpin")

        self.retranslateUi(resEntryDialog)
        self.buttonBox.accepted.connect(resEntryDialog.accept)
        self.buttonBox.rejected.connect(resEntryDialog.reject)
        self.homeCombo.currentIndexChanged['int'].connect(resEntryDialog.resChanged)
        self.visitorCombo.currentIndexChanged['int'].connect(resEntryDialog.resChanged)
        self.homeSpin.valueChanged['int'].connect(resEntryDialog.resChanged)
        self.visitorSpin.valueChanged['int'].connect(resEntryDialog.resChanged)
        QtCore.QMetaObject.connectSlotsByName(resEntryDialog)

    def retranslateUi(self, resEntryDialog):
        _translate = QtCore.QCoreApplication.translate
        resEntryDialog.setWindowTitle(_translate("resEntryDialog", "Sonuç Girme Penceresi"))
        self.label.setText(_translate("resEntryDialog", "Ev Sahibi"))
        self.label_2.setText(_translate("resEntryDialog", "Deplasman"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    resEntryDialog = QtWidgets.QDialog()
    ui = Ui_resEntryDialog()
    ui.setupUi(resEntryDialog)
    resEntryDialog.show()
    sys.exit(app.exec_())

