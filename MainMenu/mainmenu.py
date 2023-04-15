from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 720)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1371, 721))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../design/edit to 1366 x 720/main menu without button.jpg"))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 230, 351, 161))
        self.pushButton_2.setStyleSheet("background-image: url('../../tubes-rpl/mainmenu/moodbutton.png');\n"
"border: none;\n"
"")
        self.pushButton_2.setText("")
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.printmood)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(850, 230, 351, 161))
        self.pushButton_3.setStyleSheet("background-image: url('../../tubes-rpl/mainmenu/journalbutton.png');\n"
"border: none;\n"
"")
        self.pushButton_3.setText("")
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.printjournal)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(160, 420, 351, 161))
        self.pushButton_4.setStyleSheet("background-image: url('../../tubes-rpl/mainmenu/sleepbutton.png');\n"
"border: none;\n"
"")
        self.pushButton_4.setText("")
        self.pushButton_4.setFlat(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.printsleep)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(850, 420, 351, 161))
        self.pushButton_5.setStyleSheet("background-image: url('../../tubes-rpl/mainmenu/quotesbutton.png');\n"
"border: none;\n"
"")
        self.pushButton_5.setText("")
        self.pushButton_5.setFlat(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.printquotes)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(540, 560, 281, 121))
        self.pushButton_6.setStyleSheet("background-image: url('../../tubes-rpl/mainmenu/historybutton.png');\n"
"border: none;\n"
"")
        self.pushButton_6.setText("")
        self.pushButton_6.setFlat(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.printhistory)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(1180, 620, 161, 71))
        self.pushButton_7.setStyleSheet("background-image: url('../../tubes-rpl/mainmenu/quit.png');\n"
"border: none;\n"
"")
        self.pushButton_7.setText("")
        self.pushButton_7.setFlat(False)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(MainWindow.close)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    # Untuk test   
    def printmood(self):
        print("Mood udah bisa")

    def printjournal(self):
        print("Journal udah bisa")

    def printsleep(self):
        print("Sleep udah bisa")

    def printquotes(self):
        print("Quotes udah bisa")
        
    def printhistory(self):
        print("History udah bisa")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
