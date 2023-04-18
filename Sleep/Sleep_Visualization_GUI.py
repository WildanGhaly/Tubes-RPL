import sys
import Sleep.resource_rc

from PyQt5.QtCore import (QCoreApplication, QDateTime,
    QMetaObject, QRect,
    QSize)
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QDateEdit, QLabel, QPushButton, QSizePolicy, QWidget)
from PyQt5 import QtWidgets
from Sleep.Sleep import Sleep
from Sleep.Sleep_Plot import *

class Ui_Widget(QWidget, Sleep):
    def __init__(self):
        
        super().__init__()
        Sleep.__init__(self)
        self.title='Sleep'
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
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        Widget.setMinimumSize(QSize(1366, 720))
        Widget.setMaximumSize(QSize(1366, 720))
        self.sleepViz = QLabel(Widget)
        self.sleepViz.setObjectName(u"label")
        self.sleepViz.setEnabled(True)
        self.sleepViz.setGeometry(QRect(0, 0, 1366, 720))
        sizePolicy.setHeightForWidth(self.sleepViz.sizePolicy().hasHeightForWidth())
        self.sleepViz.setSizePolicy(sizePolicy)
        self.sleepViz.setMinimumSize(QSize(1366, 720))
        self.sleepViz.setMaximumSize(QSize(1366, 720))
        self.sleepViz.setStyleSheet(u"background-image: url(:/newPrefix/vstock/sleep time visualization fg.png)")

        self.nextButton = QPushButton(Widget)
        self.nextButton.setObjectName(u"nextButton")
        self.nextButton.setGeometry(QRect(1165, 617, 155, 72))
        self.nextButton.setStyleSheet(u"QPushButton{background: transparent;}")
        self.nextButton.clicked.connect(self.next)
        
        font = QFont()
        font.setPointSize(20)
        # self.nextButton.setFont(font)
        self.dateEdit = QDateEdit(Widget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(382, 630, 150, 45))
        self.dateEdit.setStyleSheet("\n"
            "font: 700 10pt \"Segoe Script\";\n"
            "alternate-background-color: rgb(255, 85, 0);\n"
            "selection-color: rgb(170, 0, 0);\n"
            "selection-background-color: rgb(170, 0, 0);\n"
            "border-color: rgb(0, 0, 0);\n")
        #Start Sleep Chart
        date = self.dateEdit.date()
        
        date.toString()
        start = self.getWeekStartSleepHour(id=None)
        startSleepChart = PlotCanvas(self , 4, 4, 100, start)
        startSleepChart.move(149,265)
        self.startPlot = QWidget(startSleepChart)
        self.startPlot.setObjectName(u"Start Chart")
        self.startPlot.setGeometry(QRect(149,265,330,300))
        #Duration Sleep Chart
        dur = self.getWeekSleepDuration(id=None)
        durationSleep = PlotCanvas(self , 4, 4, 100, dur)
        durationSleep.move(520,265)

        #endSleepChart
        end = self.getWeekEndSleepHour(id=None)
        endSleepChart = PlotCanvas(self , 4, 4, 100, end)
        endSleepChart.move(890,265)
        # self.nextButton.raise_()
        self.dateEdit.raise_()

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
        
        self.show()
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.nextButton.setText(QCoreApplication.translate("Widget", u"", None))
        self.sleepViz.setText("")
    # retranslateUi
    
    def getDate(self):
        return self.dateEdit.dateTime()

    def next(self):
        from MainMenu.main_menu_GUI import Main_Menu_GUI
        self.main_menu = Main_Menu_GUI()
        self.main_menu.show()
        self.hide()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = Ui_Widget()
    window.show()

    app.exec()