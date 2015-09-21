# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'oran.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(290, 421)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 10, 47, 13))
        self.label.setObjectName("label")
        self.oran1Edit = QtWidgets.QLineEdit(Form)
        self.oran1Edit.setGeometry(QtCore.QRect(30, 30, 61, 20))
        self.oran1Edit.setObjectName("oran1Edit")
        self.oran2Edit = QtWidgets.QLineEdit(Form)
        self.oran2Edit.setGeometry(QtCore.QRect(30, 50, 61, 20))
        self.oran2Edit.setObjectName("oran2Edit")
        self.oran3Edit = QtWidgets.QLineEdit(Form)
        self.oran3Edit.setGeometry(QtCore.QRect(30, 70, 61, 20))
        self.oran3Edit.setObjectName("oran3Edit")
        self.oran4Edit = QtWidgets.QLineEdit(Form)
        self.oran4Edit.setGeometry(QtCore.QRect(30, 90, 61, 20))
        self.oran4Edit.setObjectName("oran4Edit")
        self.oran5Edit = QtWidgets.QLineEdit(Form)
        self.oran5Edit.setGeometry(QtCore.QRect(30, 110, 61, 20))
        self.oran5Edit.setObjectName("oran5Edit")
        self.resultEdit = QtWidgets.QTextEdit(Form)
        self.resultEdit.setGeometry(QtCore.QRect(30, 170, 231, 241))
        self.resultEdit.setObjectName("resultEdit")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 150, 81, 16))
        self.label_2.setObjectName("label_2")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(100, 10, 71, 91))
        self.groupBox.setObjectName("groupBox")
        self.k3Radio = QtWidgets.QRadioButton(self.groupBox)
        self.k3Radio.setGeometry(QtCore.QRect(10, 20, 41, 17))
        self.k3Radio.setObjectName("k3Radio")
        self.k4Radio = QtWidgets.QRadioButton(self.groupBox)
        self.k4Radio.setGeometry(QtCore.QRect(10, 40, 41, 17))
        self.k4Radio.setObjectName("k4Radio")
        self.k5Radio = QtWidgets.QRadioButton(self.groupBox)
        self.k5Radio.setGeometry(QtCore.QRect(10, 60, 41, 17))
        self.k5Radio.setObjectName("k5Radio")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(180, 10, 81, 91))
        self.groupBox_2.setObjectName("groupBox_2")
        self.s3Radio = QtWidgets.QRadioButton(self.groupBox_2)
        self.s3Radio.setGeometry(QtCore.QRect(10, 20, 41, 17))
        self.s3Radio.setObjectName("s3Radio")
        self.s4Radio = QtWidgets.QRadioButton(self.groupBox_2)
        self.s4Radio.setGeometry(QtCore.QRect(10, 40, 41, 17))
        self.s4Radio.setObjectName("s4Radio")
        self.s5Radio = QtWidgets.QRadioButton(self.groupBox_2)
        self.s5Radio.setGeometry(QtCore.QRect(10, 60, 41, 17))
        self.s5Radio.setObjectName("s5Radio")

        self.retranslateUi(Form)
        self.k5Radio.clicked.connect(Form.kRadioClicked)
        self.k4Radio.clicked.connect(Form.kRadioClicked)
        self.k3Radio.clicked.connect(Form.kRadioClicked)
        self.s5Radio.clicked.connect(Form.sRadioClicked)
        self.s4Radio.clicked.connect(Form.sRadioClicked)
        self.s3Radio.clicked.connect(Form.sRadioClicked)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Oranlar"))
        self.oran1Edit.setText(_translate("Form", "0.0"))
        self.oran2Edit.setText(_translate("Form", "0.0"))
        self.oran3Edit.setText(_translate("Form", "0.0"))
        self.oran4Edit.setText(_translate("Form", "0.0"))
        self.oran5Edit.setText(_translate("Form", "0.0"))
        self.label_2.setText(_translate("Form", "Hesap Sonuçları"))
        self.groupBox.setTitle(_translate("Form", "Kolon Sayısı"))
        self.k3Radio.setText(_translate("Form", "3"))
        self.k4Radio.setText(_translate("Form", "4"))
        self.k5Radio.setText(_translate("Form", "5"))
        self.groupBox_2.setTitle(_translate("Form", "Sistem Sayısı"))
        self.s3Radio.setText(_translate("Form", "3"))
        self.s4Radio.setText(_translate("Form", "4"))
        self.s5Radio.setText(_translate("Form", "5"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

