import sys
import resource_rc

from PySide6.QtCore import (QCoreApplication, QDateTime,
    QMetaObject, QRect,
    QSize)
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QDateEdit, QLabel, QPushButton, QSizePolicy, QWidget, QPlainTextEdit)
from PySide6 import QtWidgets

from Sleep_Plot import *

class Ui_Widget(QWidget):
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
        self.sleepViz.setStyleSheet(u"background-image: url(:/newPrefix/vstock/sleep recommendation fg.png)")
        self.chronoType = QLabel(Widget)
        self.chronoType.setObjectName(u"chronoType")
        self.chronoType.setEnabled(True)
        self.chronoType.setGeometry(QRect(705, 293, 509, 155))
        sizePolicy.setHeightForWidth(self.chronoType.sizePolicy().hasHeightForWidth())
        self.chronoType.setSizePolicy(sizePolicy)
        self.chronoType.setMinimumSize(QSize(0,0))
        self.chronoType.setMaximumSize(QSize(1000,1000))
        self.chronoType.setStyleSheet(u"background-image: url(:/newPrefix/vstock/bearChronoType.jpg)")
        
        self.rec = QLabel(Widget)
        self.rec.setObjectName(u"recommendation")
        self.rec.setEnabled(True)
        self.rec.setGeometry(QRect(715, 525, 509, 50))
        sizePolicy.setHeightForWidth(self.rec.sizePolicy().hasHeightForWidth())
        self.rec.setSizePolicy(sizePolicy)
        self.rec.setStyleSheet("\n"
            "font: 700 15pt \"Segoe Script\";\n"
            "alternate-background-color: rgb(255, 85, 0);\n"
            "selection-color: rgb(170, 0, 0);\n"
            "selection-background-color: rgb(170, 0, 0);\n"
            "border-color: rgb(0, 0, 0);\n")
        self.rec1 = QLabel(Widget)
        self.rec1.setObjectName(u"recommendation")
        self.rec1.setEnabled(True)
        self.rec1.setGeometry(QRect(415, 635, 509, 50))
        sizePolicy.setHeightForWidth(self.rec1.sizePolicy().hasHeightForWidth())
        self.rec1.setSizePolicy(sizePolicy)
        self.rec1.setStyleSheet("\n"
            "font: 700 15pt \"Segoe Script\";\n"
            "alternate-background-color: rgb(255, 85, 0);\n"
            "selection-color: rgb(170, 0, 0);\n"
            "selection-background-color: rgb(170, 0, 0);\n"
            "border-color: rgb(0, 0, 0);\n")
        self.nextButton = QPushButton(Widget)
        self.nextButton.setObjectName(u"nextButton")
        self.nextButton.setGeometry(QRect(1175, 620, 170, 72))
        self.nextButton.setStyleSheet("QPushButton{background: transparent}")
        self.nextButton.clicked.connect(self.the_button_was_clicked)
        
        startSleepChart = PlotCanvasRec(self, width=5, height=4)
        startSleepChart.move(153,257)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
        
        self.show()
    # setupUi
    def the_button_was_clicked(self):
        print("Ke click AW")
    def retranslateUi(self, Widget):
        self.test = u"You should sleep more"
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.rec.setText(QCoreApplication.translate("Widget", self.test, None))
        self.rec1.setText(QCoreApplication.translate("Widget", self.test, None))
        self.nextButton.setText(QCoreApplication.translate("Widget", u"", None))
        self.sleepViz.setText("")
    # retranslateUi
    
    def getDate(self):
        return self.dateEdit.dateTime()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = Ui_Widget()
    window.show()

    app.exec()