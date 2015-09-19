# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainForm(object):
    def setupUi(self, mainForm):
        mainForm.setObjectName("mainForm")
        mainForm.resize(725, 74)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainForm.sizePolicy().hasHeightForWidth())
        mainForm.setSizePolicy(sizePolicy)
        self.horizontalLayout = QtWidgets.QHBoxLayout(mainForm)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(mainForm)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 4, 1, 1)
        self.label_8 = QtWidgets.QLabel(mainForm)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 6, 1, 1)
        self.label_7 = QtWidgets.QLabel(mainForm)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 5, 1, 1)
        self.resEntryButton = QtWidgets.QPushButton(mainForm)
        self.resEntryButton.setEnabled(False)
        self.resEntryButton.setObjectName("resEntryButton")
        self.gridLayout.addWidget(self.resEntryButton, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(mainForm)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(mainForm)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(mainForm)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.selectComboBox = QtWidgets.QComboBox(mainForm)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.selectComboBox.setFont(font)
        self.selectComboBox.setCurrentText("")
        self.selectComboBox.setObjectName("selectComboBox")
        self.selectComboBox.addItem("")
        self.selectComboBox.addItem("")
        self.gridLayout.addWidget(self.selectComboBox, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(mainForm)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 3, 1, 1)
        self.saveButton = QtWidgets.QPushButton(mainForm)
        self.saveButton.setEnabled(False)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout.addWidget(self.saveButton, 0, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(mainForm)
        self.label_2.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(mainForm)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 7, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)

        self.retranslateUi(mainForm)
        self.selectComboBox.setCurrentIndex(-1)
        self.selectComboBox.currentIndexChanged['QString'].connect(mainForm.selectLig)
        self.resEntryButton.clicked.connect(mainForm.resEntry)
        self.saveButton.clicked.connect(mainForm.saveTable)
        QtCore.QMetaObject.connectSlotsByName(mainForm)

    def retranslateUi(self, mainForm):
        _translate = QtCore.QCoreApplication.translate
        mainForm.setWindowTitle(_translate("mainForm", "İddia Ana Ekran"))
        self.label_6.setText(_translate("mainForm", "Deplasm. Beraber"))
        self.label_8.setText(_translate("mainForm", "Yediği Gol"))
        self.label_7.setText(_translate("mainForm", "Attığı Gol"))
        self.resEntryButton.setText(_translate("mainForm", "Sonuç Girişi"))
        self.label_3.setText(_translate("mainForm", "Evinde Galip"))
        self.label_4.setText(_translate("mainForm", "Deplasm. Galip"))
        self.label.setText(_translate("mainForm", "LİG:"))
        self.selectComboBox.setItemText(0, _translate("mainForm", "Türkiye Süper Lig"))
        self.selectComboBox.setItemText(1, _translate("mainForm", "Almanya Bundesliga"))
        self.label_5.setText(_translate("mainForm", "Evinde Beraber"))
        self.saveButton.setText(_translate("mainForm", "Tabloyu Kaydet"))
        self.label_2.setText(_translate("mainForm", "Takım"))
        self.label_9.setText(_translate("mainForm", "Puan"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainForm = QtWidgets.QWidget()
    ui = Ui_mainForm()
    ui.setupUi(mainForm)
    mainForm.show()
    sys.exit(app.exec_())

