# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qtjournalinputKrWPUX.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import Journal_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1366, 800)
        MainWindow.setMinimumSize(QSize(599, 800))
        MainWindow.setMaximumSize(QSize(1920, 1080))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-image: url(:/Journal/background.jpg);")
        MainWindow.setAnimated(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(800, 600))
        self.centralwidget.setMaximumSize(QSize(1920, 1080))
        self.centralwidget.setStyleSheet(u"background: transparent;\n"
"image: transparent;")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, -70, 1361, 941))
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet(u"image: url(:/Journal/journal input fg.png);")
        self.scrollArea_2 = QScrollArea(self.widget)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setGeometry(QRect(130, 380, 1101, 271))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy)
        self.scrollArea_2.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        self.scrollArea_2.setFont(font)
        self.scrollArea_2.setStyleSheet(u"background: transparent;\n"
"image: transparent;")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1099, 269))
        self.plainTextEdit_2 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setGeometry(QRect(0, 0, 1101, 271))
        sizePolicy.setHeightForWidth(self.plainTextEdit_2.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_2.setSizePolicy(sizePolicy)
        self.plainTextEdit_2.setFont(font)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QRect(1060, 670, 171, 71))
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet(u"background: transparent;\n"
"image: transparent;")
        self.pushButton_2.setFlat(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Journal Input", None))
        self.plainTextEdit_2.setPlaceholderText("")
        self.pushButton_2.setText("")
    # retranslateUi

