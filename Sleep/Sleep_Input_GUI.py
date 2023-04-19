import sys
import Sleep.resource_rc

from PyQt5.QtCore import (QCoreApplication, QDateTime,
    QMetaObject, QRect,
    QSize)
from PyQt5.QtGui import QFont 
from PyQt5.QtWidgets import (QDateEdit, QLabel, QPushButton, QSizePolicy, QWidget, QPlainTextEdit, QMessageBox)
from PyQt5 import QtWidgets
from datetime import datetime, date
from Sleep.Sleep_Service import Sleep_Service
from Sleep.Sleep import Sleep

from Sleep.Sleep_Plot import *

class Ui_Widget(QWidget, Sleep_Service, Sleep):
    def __init__(self):
        
        super().__init__()
        self.title='Sleep Input'
        self.left = 0
        self.top = 0
        self.width = 1366
        self.height = 720
        self.setupUi(self)
    
    def setupUi(self, Widget):
        self.setWindowTitle(self.title)
        # self.setGeometry(self.left, self.top, self.width, self.height)
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1366, 720)
        Widget.setMinimumSize(QSize(1366, 720))
        Widget.setMaximumSize(QSize(1366, 720))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        self.bg = QLabel(Widget)
        self.bg.setObjectName(u"label")
        self.bg.setEnabled(True)
        self.bg.setGeometry(QRect(0, 0, 1366, 720))
        sizePolicy.setHeightForWidth(self.bg.sizePolicy().hasHeightForWidth())
        self.bg.setSizePolicy(sizePolicy)
        self.bg.setMinimumSize(QSize(1366, 720))
        self.bg.setMaximumSize(QSize(1366, 720))
        self.bg.setStyleSheet(u"border-image: url(./Sleep/vstock/background.jpg)")
        self.sleepViz = QLabel(Widget)
        self.sleepViz.setObjectName(u"label")
        self.sleepViz.setEnabled(True)
        self.sleepViz.setGeometry(QRect(0, 0, 1366, 720))
        self.sleepViz.setMinimumSize(QSize(1366, 720))
        self.sleepViz.setMaximumSize(QSize(1366, 720))
        self.sleepViz.setStyleSheet(u"border-image: url(./Sleep/vstock/sleep time input fg.png)")
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
        self.plainTextEdit1.setGeometry(QRect(680, 378, 275, 50))
        self.plainTextEdit1.setStyleSheet("\n"
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
        self.backButton = QPushButton(Widget)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setGeometry(QRect(25, 25, 88, 86))
        self.backButton.setStyleSheet("QPushButton{background: transparent;}")
        self.backButton.clicked.connect(self.back)
        # self.nextButton.connect()
        self.retranslateUi(Widget)
        QMetaObject.connectSlotsByName(Widget)
        
        self.show()
    # setupUi
    def back(self):
        from MainMenu.main_menu_GUI import Main_Menu_GUI
        self.main_menu = Main_Menu_GUI()
        self.main_menu.show()
        self.hide()
    
    def the_button_was_clicked(self):
        hourStartDone = False
        hourEndDone=False
        countStart = 0
        countEnd = 0
        hasilData = []
        self.startClock = self.plainTextEdit.toPlainText()
        self.endClock = self.plainTextEdit1.toPlainText()
        self.dates = date.today().strftime("%d%m%Y")
        self.dates += datetime.now().strftime("%H%M%S")
        print(self.startClock)
        # if((self.startClock.find('.') ==-1 or self.startClock.find(':') == -1) and (self.endClock.find('.') ==-1 or self.endClock.find(':') == -1)):
        #     invalid = True
        if self.startClock != '' and self.endClock != '':
            hourStart = ''
            minuteStart = ''
            for i in self.startClock:
                if(i=="." or i=="."):
                    hourStartDone =True
                    continue
                if not hourStartDone:
                    countStart+=1
                    hourStart  += i
                if(hourStartDone):
                    countStart+=1
                    minuteStart += i
                else:
                    pass
            print(countStart)
            hourEnd = ''
            minuteEnd = ''
            for i in self.endClock:
                if(i=="." or i=="."):
                    hourEndDone =True
                    continue
                if not hourEndDone:
                    countEnd+=1
                    hourEnd  += i
                if(hourEndDone):
                    countEnd+=1
                    minuteEnd += i
                else:
                    pass
            print(countEnd)
            if self.validate_sleep(hourStart, minuteStart, hourEnd, minuteEnd):
                hasilData.append(self.dates)
                hasilData.append(hourStart)
                hasilData.append(minuteStart)
                hasilData.append(hourEnd)
                hasilData.append(minuteEnd)
                hasilData.append(self.duration_count(hourStart, minuteStart, hourEnd, minuteEnd))
                Sleep.add_Sleep(self, hasilData)
                from MainMenu.main_menu_GUI import Main_Menu_GUI
                self.main_menu = Main_Menu_GUI()
                self.main_menu.show()
                self.hide()
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Warning")
                msg.setText("Invalid time")
                msg.setStyleSheet("\n"
                    "font: 700 15pt \"Segoe Script\";\n"
                    "alternate-background-color: rgb(255, 85, 0);\n"
                    "selection-color: rgb(170, 0, 0);\n"
                    "selection-background-color: rgb(170, 0, 0);\n"
                    "border-color: rgb(0, 0, 0);\n")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Warning")
            msg.setText("Some field is empty!")
            msg.setIcon(QMessageBox.Critical)
            msg.setStyleSheet("\n"
                    "font: 700 15pt \"Segoe Script\";\n"
                    "alternate-background-color: rgb(255, 85, 0);\n"
                    "selection-color: rgb(170, 0, 0);\n"
                    "selection-background-color: rgb(170, 0, 0);\n"
                    "border-color: rgb(0, 0, 0);\n")
            msg.exec_()
        self.plainTextEdit.clear()
        self.plainTextEdit1.clear()
        

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.nextButton.setText(QCoreApplication.translate("Widget", u"", None))
        self.backButton.setText(QCoreApplication.translate("Widget",u"Back", None))
        self.sleepViz.setText("")
    # retranslateUi
    
    def getDate(self):
        return self.dateEdit.dateTime()


# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)

#     window = Ui_Widget()
#     window.show()

#     app.exec()