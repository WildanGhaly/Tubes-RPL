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
        
        
        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
        
        self.show()
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        # self.nextButton.setText(QCoreApplication.translate("Widget", u"", None))
        self.sleepViz.setText("")
    # retranslateUi
    
    def getDate(self):
        return self.dateEdit.dateTime()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = Ui_Widget()
    window.show()

    app.exec()
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
        

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
        
        self.show()
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        # self.nextButton.setText(QCoreApplication.translate("Widget", u"", None))
        self.sleepViz.setText("")
    # retranslateUi
    
    def getDate(self):
        return self.dateEdit.dateTime()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = Ui_Widget()
    window.show()

    app.exec()