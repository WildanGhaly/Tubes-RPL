# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testQuotesI4.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsOpacityEffect
import Quotes_Service as QS
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextCharFormat, QColor


class QPopUp(QS.Quotes_Service):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1366, 720)
        Dialog.setMinimumSize(QtCore.QSize(1366, 720))
        Dialog.setMaximumSize(QtCore.QSize(1366, 720))
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 1366, 720))
        self.label.setMinimumSize(QtCore.QSize(1366, 720))
        self.label.setMaximumSize(QtCore.QSize(1366, 720))
        self.label.setStyleSheet("background-image: url(:/newPrefix/mendapat quotes fg.png);")
        self.label.setText("")
        self.label.setObjectName("label")

        self.textEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(200, 407, 965, 181))
        self.textEdit.setStyleSheet("background-color: transparent;")
        self.textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit.setObjectName("textEdit")
        font = QFont("Arial", 22)
        self.textEdit.setFont(font)
        self.textEdit.setReadOnly(True)
        self.textEdit.setPlainText(self.get_random_quote())
        # opacity_effect = QGraphicsOpacityEffect()
        # opacity_effect.setOpacity(0)  # Set the opacity value between 0 and 1
        # self.textEdit.setGraphicsEffect(opacity_effect)
        # self.textEdit.setStyleSheet("background-color: transparent;")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
    

import rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = QPopUp()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
