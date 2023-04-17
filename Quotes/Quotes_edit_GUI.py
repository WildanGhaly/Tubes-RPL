# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testQuotesI3.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QWidget
from PyQt5.QtGui import QFont
from tkinter import messagebox
import csv
import Quotes.Quotes_Service as QS


class QEdit(QS.Quotes_Service):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1366, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1366, 720))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -20, 1366, 720))
        self.label.setMinimumSize(QtCore.QSize(1366, 720))
        self.label.setMaximumSize(QtCore.QSize(1366, 720))
        self.label.setStyleSheet("background-image: url(:/newPrefix/quotes edit fg.png);")
        self.label.setText("")
        self.label.setObjectName("label")

        self.quotes_list = QtWidgets.QComboBox(self.centralwidget)
        self.quotes_list.setGeometry(QtCore.QRect(132, 258, 1101, 86))
        self.quotes_list.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.quotes_list.setStyleSheet("")
        self.quotes_list.setObjectName("quotes_list")
        font = QFont("Arial", 15)
        self.quotes_list.setFont(font)
        self.adding_quotes_Cbox()

        self.new_quotes = QtWidgets.QTextEdit(self.centralwidget)
        self.new_quotes.setGeometry(QtCore.QRect(130, 425, 1102, 88))
        self.new_quotes.setStyleSheet("background-color: transparent;")
        self.new_quotes.setObjectName("new_quotes")
        font = QFont("Arial", 15)
        self.new_quotes.setFont(font)


        self.Submit = QtWidgets.QPushButton(self.centralwidget)
        self.Submit.setGeometry(QtCore.QRect(1080, 540, 141, 71))
        self.Submit.setStyleSheet("background-color: transparent;")
        self.Submit.setText("")
        self.Submit.setObjectName("Submit")
        self.Submit.clicked.connect(self.edit_quote_submit)


        # MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1366, 21))
        self.menubar.setObjectName("menubar")
        # MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def adding_quotes_Cbox(self):
        with open('Quotes/Quotes.csv', 'r') as csvfile:  # Replace with the name of your CSV file
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                quote = row[0] + ".  " + row[1]
                self.quotes_list.addItem(quote)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
    
    def edit_quote_submit(self):
        # call edit_quote function from backend and show success message if it returns true
        selected_quote = self.quotes_list.currentText().split(".  ")
        if self.edit_quote(selected_quote[1], self.new_quotes.toPlainText()):
            messagebox.showinfo("Success", "Quote berhasil diedit.")
            self.new_quotes.setText("")
            self.quotes_list.clear()
            self.adding_quotes_Cbox()
            from MainMenu.main_menu_GUI import Main_Menu_GUI as Main_Menu
            self.main_menu = Main_Menu()
            self.main_menu.show()
            self.hide()
            

            
import Quotes.rc_edit

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = QEdit()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
