# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtjournallist.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class JournalList(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        MainWindow.setStyleSheet("background-image: url(:/Journal/background.jpg);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1366, 720))
        self.widget.setStyleSheet("background: transparent;\n"
"image: url(:/Journal/journal list fg.png);")
        self.widget.setObjectName("widget")
        self.contentFrame = QtWidgets.QFrame(self.widget)
        self.contentFrame.setGeometry(QtCore.QRect(132, 270, 1101, 267))
        self.contentFrame.setStyleSheet("background: transparent;\n"
"image: transparent;")
        self.contentFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contentFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contentFrame.setObjectName("contentFrame")
        self.contentView = QtWidgets.QTableWidget(self.contentFrame)
        self.contentView.setGeometry(QtCore.QRect(0, 0, 1101, 267))
        self.contentView.setGridStyle(QtCore.Qt.NoPen)
        self.contentView.setRowCount(0)
        self.contentView.setObjectName("contentView")
        self.contentView.setColumnCount(0)
        self.contentView.horizontalHeader().setSortIndicatorShown(False)
        self.dRight = QtWidgets.QPushButton(self.widget)
        self.dRight.setGeometry(QtCore.QRect(620, 570, 51, 51))
        self.dRight.setAutoFillBackground(False)
        self.dRight.setStyleSheet("image: transparent;")
        self.dRight.setText("")
        self.dRight.setObjectName("dRight")
        self.dLeft = QtWidgets.QPushButton(self.widget)
        self.dLeft.setGeometry(QtCore.QRect(690, 570, 51, 51))
        self.dLeft.setAutoFillBackground(False)
        self.dLeft.setStyleSheet("image: transparent;")
        self.dLeft.setText("")
        self.dLeft.setObjectName("dLeft")
        self.next = QtWidgets.QPushButton(self.widget)
        self.next.setGeometry(QtCore.QRect(1080, 570, 151, 51))
        self.next.setAutoFillBackground(False)
        self.next.setStyleSheet("image: transparent;")
        self.next.setText("")
        self.next.setObjectName("next")
        self.dateChoose = QtWidgets.QPushButton(self.widget)
        self.dateChoose.setGeometry(QtCore.QRect(1090, 210, 148, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateChoose.sizePolicy().hasHeightForWidth())
        self.dateChoose.setSizePolicy(sizePolicy)
        self.dateChoose.setStyleSheet("image: transparent;\n"
"background: transparent;")
        self.dateChoose.setText("")
        self.dateChoose.setObjectName("dateChoose")
        # MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "JournalList"))
import Journal.Journal_rc
