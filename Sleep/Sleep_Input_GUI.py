import sys
import Sleep.resource_rc

from PyQt5.QtCore import (QCoreApplication, QDateTime,
    QMetaObject, QRect,
    QSize)
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QDateEdit, QLabel, QPushButton, QSizePolicy, QWidget, QPlainTextEdit, QMessageBox)
from PyQt5 import QtWidgets
from datetime import datetime, date
from Sleep.Sleep import Sleep

from Sleep.Sleep_Plot import *

class Ui_Widget(QWidget, Sleep):
    def __init__(self):
        
        super().__init__()
        __metaclass__ = Sleep
        Sleep.__init__(self)
        self.title='Sleep Input'
        self.left = 0
        self.top = 0
        self.width = 1366
        self.height = 720
        self.setupUi(self)
    
    def setupUi(self, Widget):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1366, 720)
        Widget.setMinimumSize(QSize(1366, 720))
        Widget.setMaximumSize(QSize(1366, 720))
        self.sleepViz = QLabel(Widget)
        self.sleepViz.setObjectName(u"label")
        self.sleepViz.setEnabled(True)
        self.sleepViz.setGeometry(QRect(0, 0, 1366, 720))
        self.sleepViz.setMinimumSize(QSize(1366, 720))
        self.sleepViz.setMaximumSize(QSize(1366, 720))
        self.sleepViz.setStyleSheet(u"background-image: url(:/newPrefix/vstock/sleep time input fg.png)")
        self.plainTextEdit = QPlainTextEdit(Widget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(680, 244, 275, 50))
        self.plainTextEdit.setStyleSheet("\n"
            "font: 700 15pt \"Segoe Script\";\n"
            "alternate-background-color: rgb(255, 85, 0);\n"
            "selection-color: rgb(170, 0, 0);\n"
            "selection-background-color: rgb(170, 0, 0);\n"
            "border-color: rgb(0, 0, 0);\n")
        self.plainTextEdit1 = QPlainTextEdit(Widget)
        self.plainTextEdit1.setObjectName(u"plainTextEdit")
        self.plainTextEdit1.setGeometry(QRect(680, 344, 275, 50))
        self.plainTextEdit1.setStyleSheet("\n"
            "font: 700 15pt \"Segoe Script\";\n"
            "alternate-background-color: rgb(255, 85, 0);\n"
            "selection-color: rgb(170, 0, 0);\n"
            "selection-background-color: rgb(170, 0, 0);\n"
            "border-color: rgb(0, 0, 0);\n")
        self.plainTextEdit2 = QPlainTextEdit(Widget)
        self.plainTextEdit2.setObjectName(u"plainTextEdit")
        self.plainTextEdit2.setGeometry(QRect(730, 444, 225, 50))
        self.plainTextEdit2.setStyleSheet("\n"
            "font: 700 15pt \"Segoe Script\";\n"
            "alternate-background-color: rgb(255, 85, 0);\n"
            "selection-color: rgb(170, 0, 0);\n"
            "selection-background-color: rgb(170, 0, 0);\n"
            "border-color: rgb(0, 0, 0);\n")
        self.nextButton = QPushButton(Widget)
        self.nextButton.setObjectName(u"nextButton")
        self.nextButton.setGeometry(QRect(600, 547, 170, 72))
        self.nextButton.setStyleSheet("QPushButton{background: transparent;}")
        self.nextButton.clicked.connect(self.the_button_was_clicked)
        # self.nextButton.connect()
        self.retranslateUi(Widget)
        QMetaObject.connectSlotsByName(Widget)
        
        self.show()
    # setupUi
    def the_button_was_clicked(self):
        invalid = False
        hourdone=False
        count = 0
        hasilData = []
        self.startClock = self.plainTextEdit.toPlainText()
        self.endClock = self.plainTextEdit1.toPlainText()
        self.duration = self.plainTextEdit2.toPlainText()
        self.dates = date.today().strftime("%d%m%Y")
        self.dates += datetime.now().strftime("%H%M%S")
        print(self.startClock)
        # if((self.startClock.find('.') ==-1 or self.startClock.find(':') == -1) and (self.endClock.find('.') ==-1 or self.endClock.find(':') == -1)):
        #     invalid = True
        if self.startClock != '' and self.endClock != '' and self.duration != '':
            hour = ''
            minute = ''
            for i in self.startClock:
                if(i=="." or i=="."):
                    hourdone =True
                    continue
                if not hourdone:
                    count+=1
                    minute += i
                if(hourdone):
                    count+=1
                    hour  += i
                else:
                    pass
            print(count)
            if count == 4 and hourdone:
                hasilData.append(self.dates)
                hasilData.append(hour)
                hasilData.append(minute)
                hasilData.append(self.duration)
                Sleep.add_Sleep(self, hasilData)
                from MainMenu.main_menu_GUI import Main_Menu_GUI
                self.main_menu = Main_Menu_GUI()
                self.main_menu.show()
                self.hide()
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Warning")
                msg.setText("Invalid time\n Format: HH.MM atau HH:MM")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                
        self.plainTextEdit.clear()
        self.plainTextEdit1.clear()
        self.plainTextEdit2.clear()
        

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.nextButton.setText(QCoreApplication.translate("Widget", u"", None))
        self.sleepViz.setText("")
    # retranslateUi
    
    def getDate(self):
        return self.dateEdit.dateTime()


# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)

#     window = Ui_Widget()
#     window.show()

#     app.exec()