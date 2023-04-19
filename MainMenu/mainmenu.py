from PyQt5 import QtCore, QtGui, QtWidgets
# import sys
# sys.path.append('..')

from History.history_GUI import history_GUI as history_window
from Mood.mood_pyqt import Mood_Form as mood_window
from Journal.JournalInput_Call import Journal_GUI_Call as journal_window
from Sleep.Sleep_Input_GUI import Ui_Widget as sleep_window
from Quotes.Choose_Call import Quotes_Choose_Call as quotes_window
from Quotes.Quotes_Popup_Call import Quotes_Popup_Call as quotes_popup

first_run = True

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        global first_run
        global pixmap
        print(first_run)
        if first_run:
            self.getRandomQuotes()
            first_run = False
        else:
            self.background_changed = False
            MainWindow.setObjectName("MainWindow")
            MainWindow.resize(1366, 720)
            MainWindow.setStyleSheet("")
            self.centralwidget = QtWidgets.QWidget(MainWindow)
            self.centralwidget.setObjectName("centralwidget")
            self.label = QtWidgets.QLabel(self.centralwidget)
            self.label.setGeometry(QtCore.QRect(0, 0, 1371, 721))
            self.label.setText("")
            pixmap = self.label.setPixmap(QtGui.QPixmap('mainmenu/background.jpg'))
            self.label.setObjectName("label")
            self.label_3 = QtWidgets.QLabel(self.centralwidget)
            self.label_3.setGeometry(QtCore.QRect(0, 0, 1371, 721))
            self.label_3.setText("")
            self.label_3.setPixmap(QtGui.QPixmap('mainmenu/display.png'))
            self.label_3.setObjectName("label_3")
            self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton_2.setGeometry(QtCore.QRect(160, 230, 351, 161))
            self.pushButton_2.setStyleSheet("background-image: url('mainmenu/moodbutton.png');\n"
    "border: none;\n"
    "")
            self.pushButton_2.setText("")
            self.pushButton_2.setFlat(False)
            self.pushButton_2.setObjectName("pushButton_2")
            self.pushButton_2.clicked.connect(self.printmood)
            self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton_3.setGeometry(QtCore.QRect(850, 230, 351, 161))
            self.pushButton_3.setStyleSheet("background-image: url('mainmenu/journalbutton.png');\n"
    "border: none;\n"
    "")
            self.pushButton_3.setText("")
            self.pushButton_3.setFlat(False)
            self.pushButton_3.setObjectName("pushButton_3")
            self.pushButton_3.clicked.connect(self.printjournal)
            self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton_4.setGeometry(QtCore.QRect(160, 420, 351, 161))
            self.pushButton_4.setStyleSheet("background-image: url('mainmenu/sleepbutton.png');\n"
    "border: none;\n"
    "")
            self.pushButton_4.setText("")
            self.pushButton_4.setFlat(False)
            self.pushButton_4.setObjectName("pushButton_4")
            self.pushButton_4.clicked.connect(self.printsleep)
            self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton_5.setGeometry(QtCore.QRect(850, 420, 351, 161))
            self.pushButton_5.setStyleSheet("background-image: url('mainmenu/quotesbutton.png');\n"
    "border: none;\n"
    "")
            self.pushButton_5.setText("")
            self.pushButton_5.setFlat(False)
            self.pushButton_5.setObjectName("pushButton_5")
            self.pushButton_5.clicked.connect(self.printquotes)
            self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton_6.setGeometry(QtCore.QRect(540, 560, 281, 121))
            self.pushButton_6.setStyleSheet("background-image: url('mainmenu/infobutton.png');\n"
    "border: none;\n"
    "")
            self.pushButton_6.setText("")
            self.pushButton_6.setFlat(False)
            self.pushButton_6.setObjectName("pushButton_6")
            self.pushButton_6.clicked.connect(self.openInfo)
            self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton_7.setGeometry(QtCore.QRect(1180, 620, 161, 71))
            self.pushButton_7.setStyleSheet("background-image: url('mainmenu/quit.png');\n"
    "border: none;\n"
    "")
            self.pushButton_7.setText("")
            self.pushButton_7.setFlat(False)
            self.pushButton_7.setObjectName("pushButton_7")
            self.pushButton_7.clicked.connect(MainWindow.close)


            self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton_8.setGeometry(QtCore.QRect(40, 620, 161, 71))
            self.pushButton_8.setStyleSheet("background-image: url('mainmenu/changebg.png');\n"
    "border: none;\n"
    "")
            self.pushButton_8.setText("")
            self.pushButton_8.setFlat(False)
            self.pushButton_8.setObjectName("pushButton_8")
            self.pushButton_8.clicked.connect(self.changeBackground)

            self.retranslateUi(MainWindow)
            QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    # Untuk test   
    def printmood(self):
        print("Mood udah bisa")
        self.mood = mood_window()
        self.mood.show()
        self.hide()

    def printjournal(self):
        print("Journal udah bisa")
        self.journal = journal_window()
        self.journal.show()
        self.hide()

    def printsleep(self):
        print("Sleep udah bisa")
        self.sleep = sleep_window()
        self.sleep.show()
        self.hide()

    def printquotes(self):
        print("Quotes udah bisa")
        self.quotes = quotes_window()
        self.quotes.show()
        self.hide()
        
    def openInfo(self):
        print("Info udah bisa")
        self.history = history_window()
        self.history.show()
        self.hide()
    
    def getRandomQuotes(self):
        print("Show Quotes")
        self.quotes = quotes_popup()
        self.quotes.show()
        self.hide()

    def changeBackground(self):
        print("Change Background")
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setNameFilter("Images (*.jpg)")
        file_dialog.setDefaultSuffix("jpg")
        file_path, _ = file_dialog.getOpenFileName()
            
        if file_path:
            pixmap = QtGui.QPixmap(file_path).scaled(self.label.width(), self.label.height())
            self.background_changed = True
        else:
            return
        
        self.label.setPixmap(pixmap)
       
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
