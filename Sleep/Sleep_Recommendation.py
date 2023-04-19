import sys
import Sleep.resource_rc

from PyQt5.QtCore import (QCoreApplication, QDateTime,
    QMetaObject, QRect,
    QSize)
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QDateEdit, QLabel, QPushButton, QSizePolicy, QWidget, QPlainTextEdit)
from PyQt5 import QtWidgets
from Sleep.Sleep import Sleep
from Sleep.Sleep_Plot import *
import  MainMenu.mainmenu as main

class Ui_Widget(QWidget, Sleep):
    def __init__(self):
        
        super().__init__()
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
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        Widget.setMinimumSize(QSize(1366, 720))
        Widget.setMaximumSize(QSize(1366, 720))
        self.bg = QLabel(Widget)
        self.bg.setObjectName(u"label2")
        self.bg.setEnabled(True)
        self.bg.setGeometry(QRect(0, 0, 1366, 720))
        sizePolicy.setHeightForWidth(self.bg.sizePolicy().hasHeightForWidth())
        self.bg.setSizePolicy(sizePolicy)
        self.bg.setMinimumSize(QSize(1366, 720))
        self.bg.setMaximumSize(QSize(1366, 720))
        self.bg.setStyleSheet(f"background-image: url({main.image_path})")
        self.sleepViz = QLabel(Widget)
        self.sleepViz.setObjectName(u"label")
        self.sleepViz.setEnabled(True)
        self.sleepViz.setGeometry(QRect(0, 0, 1366, 720))
        self.sleepViz.setStyleSheet(u"border-image: url(./Sleep/vstock/sleep recommendation fg.png)")
        self.chronoType = QLabel(Widget)
        self.chronoType.setObjectName(u"chronoType")
        self.chronoType.setEnabled(True)
        self.chronoType.setGeometry(QRect(705, 293, 509, 155))
        self.chronoType.setStyleSheet(u"border-image: url(./Sleep/vstock/bearChronoType.jpg)")
        
        self.rec = QLabel(Widget)
        self.rec.setObjectName(u"recommendation")
        self.rec.setEnabled(True)
        self.rec.setGeometry(QRect(715, 525, 509, 50))
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
        data = self.getWeekSleepDuration(id = None)
        print(data)
        startDuration = PlotCanvasRec(self , 4, 4, 100, data)
        startDuration.move(153,257)
        self.labelRecommendation = QLabel(Widget)
        self.labelRecommendation.setObjectName(u"DurationChart")
        self.labelRecommendation.setEnabled(True)
        self.labelRecommendation.setGeometry(153,257,508,310)
        self.labelRecommendation.setStyleSheet("border-image: url(./Sleep/vis_result/recommendation.png)")
        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
        
        self.show()
    # setupUi
    def the_button_was_clicked(self):
        print("Ke click AW")
        from MainMenu.main_menu_GUI import Main_Menu_GUI
        self.main_menu = Main_Menu_GUI()
        self.main_menu.show()
        self.hide()
        
    def retranslateUi(self, Widget):
        self.test = u"You should sleep more"
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.rec.setText(QCoreApplication.translate("Widget", self.test, None))
        self.rec1.setText(QCoreApplication.translate("Widget", self.test, None))
        self.nextButton.setText(QCoreApplication.translate("Widget", u"", None))
        self.labelRecommendation.setText(QCoreApplication.translate("Widget", u"", None))
        self.sleepViz.setText("")
    # retranslateUi
    
    def getDate(self):
        return self.dateEdit.dateTime()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = Ui_Widget()
    window.show()

    app.exec()