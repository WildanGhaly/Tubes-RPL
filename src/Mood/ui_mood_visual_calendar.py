# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mood_visual_calendar.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import MainMenu.mainmenu as mainmenu


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(720, 480)
        Dialog.setMinimumSize(QtCore.QSize(720, 480))
        Dialog.setMaximumSize(QtCore.QSize(720, 480))
        self.calendar_mood_visual = QtWidgets.QCalendarWidget(Dialog)
        self.calendar_mood_visual.setGeometry(QtCore.QRect(0, 0, 720, 431))
        self.calendar_mood_visual.setStyleSheet("background-image: url(:/newPrefix/images/default_background.jpg);")
        self.calendar_mood_visual.setObjectName("calendar_mood_visual")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 720, 480))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(720, 480))
        self.label.setMaximumSize(QtCore.QSize(720, 480))
        self.label.setStyleSheet(f"border-image: url({mainmenu.image_path});\n")
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 440, 701, 26))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.calendar_mood_visual_ok = QtWidgets.QPushButton(self.layoutWidget)
        self.calendar_mood_visual_ok.setStyleSheet("background-color: rgb(13, 255, 0);\n"
"font: 700 10pt \"Arial\";")
        self.calendar_mood_visual_ok.setObjectName("calendar_mood_visual_ok")
        self.horizontalLayout.addWidget(self.calendar_mood_visual_ok)
        self.calendar_mood_visual_cancel = QtWidgets.QPushButton(self.layoutWidget)
        self.calendar_mood_visual_cancel.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"\n"
"font: 700 10pt \"Arial\";")
        self.calendar_mood_visual_cancel.setObjectName("calendar_mood_visual_cancel")
        self.horizontalLayout.addWidget(self.calendar_mood_visual_cancel)
        self.label.raise_()
        self.calendar_mood_visual.raise_()
        self.layoutWidget.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "TextLabel"))
        self.calendar_mood_visual_ok.setText(_translate("Dialog", "OK"))
        self.calendar_mood_visual_cancel.setText(_translate("Dialog", "CANCEL"))
import Mood.resource_rc
