import sys
import resource_rc

from PySide6.QtCore import (QCoreApplication, QDateTime,
    QMetaObject, QRect,
    QSize)
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QDateEdit, QLabel, QPushButton, QSizePolicy, QWidget)
from PySide6 import QtWidgets

from Sleep_Plot import *

class Ui_Widget(QWidget):
    def __init__(self):
        
        super().__init__()
        self.title='Sleep'
        self.left = 0
        self.top = 0
        self.width = 1920
        self.height = 1080
        self.setupUi(self)
    
    def setupUi(self, Widget):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1920, 1080)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        Widget.setMinimumSize(QSize(1920, 1080))
        Widget.setMaximumSize(QSize(1920, 1080))
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setGeometry(QRect(0, 0, 1920, 1080))
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(1920, 1080))
        self.label.setMaximumSize(QSize(1920, 1080))
        self.label.setStyleSheet(u"background-image: url(:/newPrefix/vstock/sleep_viz.jpg)")

        
        self.nextButton = QPushButton(Widget)
        self.nextButton.setObjectName(u"nextButton")
        self.nextButton.setGeometry(QRect(1665, 940, 225, 100))
        self.nextButton.setStyleSheet(u"\n"
            "font: 700 20pt \"Segoe Script\";\n"
            "alternate-background-color: rgb(255, 85, 0);\n"
            "selection-color: rgb(170, 0, 0);\n"
            "selection-background-color: rgb(170, 0, 0);\n"
            "border-color: rgb(0, 0, 0);")
        
        font = QFont()
        font.setPointSize(20)
        self.nextButton.setFont(font)
        self.dateEdit = QDateEdit(Widget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(538, 968, 195, 45))
        #Start Sleep Chart
        startSleepChart = PlotCanvas(self, width=5, height=4)
        startSleepChart.move(211,395)
        
        #Duration Sleep Chart
        durationSleep = PlotCanvas(self, width=5, height=4)
        durationSleep.move(735,395)

        #endSleepChart
        endSleepChart = PlotCanvas(self, width=5, height=4)
        endSleepChart.move(1260,395)
        
        self.nextButton.raise_()
        self.dateEdit.raise_()

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
        
        self.show()
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.nextButton.setText(QCoreApplication.translate("Widget", u"NEXT", None))
        self.label.setText("")
    # retranslateUi
    
    def getDate(self):
        return self.dateEdit.dateTime()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = Ui_Widget()
    window.show()

    app.exec()