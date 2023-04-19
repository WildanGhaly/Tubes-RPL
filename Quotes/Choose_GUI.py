# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testQuotesI2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import Quotes.Quotes_Service as QS
import  MainMenu.mainmenu as main
from PyQt5.QtWidgets import (QDateEdit, QLabel, QPushButton, QSizePolicy, QWidget, QPlainTextEdit, QMessageBox)

class QChoose(QS.Quotes_Service):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1366, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1366, 720))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1366, 720))
        self.label.setMinimumSize(QtCore.QSize(1366, 720))
        self.label.setMaximumSize(QtCore.QSize(1366, 720))

        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.label.setEnabled(True)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        # self.label.setStyleSheet("background-image: url(:/newPrefix/select quotes menu fg.png);")
        self.label.setStyleSheet(f"background-image: url({main.image_path});\n"
"border-image: url(./Quotes/image/select quotes menu fg black.png);")
        self.label.setText("")
        self.label.setObjectName("label")

        self.add_choose = QtWidgets.QPushButton(self.centralwidget)
        self.add_choose.setGeometry(QtCore.QRect(300, 570, 141, 51))
        self.add_choose.setStyleSheet("background-color: transparent;")
        self.add_choose.setText("")
        self.add_choose.setObjectName("add_choose")
        self.add_choose.clicked.connect(self.add)

        self.edit_choose = QtWidgets.QPushButton(self.centralwidget)
        self.edit_choose.setGeometry(QtCore.QRect(940, 570, 141, 51))
        self.edit_choose.setStyleSheet("background-color: transparent;")
        self.edit_choose.setText("")
        self.edit_choose.setObjectName("edit_choose")
        self.edit_choose.clicked.connect(self.edit)

        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setGeometry(QtCore.QRect(25, 25, 88, 86))
        self.backButton.setStyleSheet("QPushButton{background: transparent;}")
        self.backButton.clicked.connect(self.back)


        # MainWindow.setCentralWidget(self.centralwidget)
        # self.menubar = QtWidgets.QMenuBar(MainWindow)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 1366, 21))
        # self.menubar.setObjectName("menubar")
        # MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def add(self):
        print("add")
        from Quotes.Quotes_Input_Call import Quotes_Input_Call
        self.add_quotes_window = Quotes_Input_Call()
        self.add_quotes_window.show()
        self.hide()
        

    def edit(self):
        print("edit")
        from Quotes.Quotes_edit_Call import Quotes_Edit_Call
        self.add_quotes_window = Quotes_Edit_Call()
        self.add_quotes_window.show()
        self.hide()
    
    def back(self):
        from MainMenu.main_menu_GUI import Main_Menu_GUI
        self.main_menu = Main_Menu_GUI()
        self.main_menu.show()
        self.hide()


import Quotes.rc_choose

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = QChoose()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
