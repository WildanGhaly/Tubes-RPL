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
        self.sleepViz.setStyleSheet(u"background-image: url(:/newPrefix/vstock/sleep time input fg.png)")
        self.plainTextEdit = QPlainTextEdit(Widget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(680, 244, 275, 50))
        self.plainTextEdit = QPlainTextEdit(Widget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(680, 344, 275, 50))
        self.plainTextEdit = QPlainTextEdit(Widget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(730, 444, 225, 50))
        
        self.nextButton = QPushButton(Widget)
        self.nextButton.setObjectName(u"nextButton")
        self.nextButton.setGeometry(QRect(600, 547, 170, 72))
        self.nextButton.setStyleSheet("QPushButton{background: transparent;}")
        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
        
        self.show()
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        # self.nextButton.setText(QCoreApplication.translate("Widget", u"NEXT", None))
        self.sleepViz.setText("")
    # retranslateUi
    
    def getDate(self):
        return self.dateEdit.dateTime()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = Ui_Widget()
    window.show()

    app.exec()