# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mood/mood_feedback.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import MainMenu.mainmenu as mainmenu


class Ui_mood_feedback(object):
    def setupUi(self, mood_feedback):
        mood_feedback.setObjectName("mood_feedback")
        mood_feedback.resize(1366, 720)
        mood_feedback.setMinimumSize(QtCore.QSize(1366, 720))
        mood_feedback.setMaximumSize(QtCore.QSize(1366, 720))
        self.background_label = QtWidgets.QLabel(mood_feedback)
        self.background_label.setGeometry(QtCore.QRect(0, 0, 1366, 720))
        self.background_label.setMinimumSize(QtCore.QSize(1366, 720))
        self.background_label.setMaximumSize(QtCore.QSize(1366, 720))
        self.background_label.setStyleSheet(f"background-image: url({mainmenu.image_path});\n"
            "border-image: url(:/Netral/images/new bg mood prediction rate fg.png);")
        self.background_label.setText("")
        self.background_label.setObjectName("background_label")
        self.rating_slider = QtWidgets.QSlider(mood_feedback)
        self.rating_slider.setGeometry(QtCore.QRect(258, 264, 856, 70))
        self.rating_slider.setStyleSheet("")
        self.rating_slider.setOrientation(QtCore.Qt.Horizontal)
        self.rating_slider.setObjectName("rating_slider")
        self.text_edit = QtWidgets.QTextEdit(mood_feedback)
        self.text_edit.setGeometry(QtCore.QRect(116, 468, 1140, 110))
        self.text_edit.setStyleSheet("font: 700 17pt \"Segoe UI\";")
        self.text_edit.setObjectName("text_edit")
        self.submit_button = QtWidgets.QPushButton(mood_feedback)
        self.submit_button.setGeometry(QtCore.QRect(1159, 624, 173, 70))
        self.submit_button.setStyleSheet("")
        self.submit_button.setText("")
        self.submit_button.setAutoDefault(True)
        self.submit_button.setDefault(True)
        self.submit_button.setFlat(True)
        self.submit_button.setObjectName("submit_button")

        self.retranslateUi(mood_feedback)
        QtCore.QMetaObject.connectSlotsByName(mood_feedback)

    def retranslateUi(self, mood_feedback):
        _translate = QtCore.QCoreApplication.translate
        mood_feedback.setWindowTitle(_translate("mood_feedback", "Form"))
        self.text_edit.setHtml(_translate("mood_feedback", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:17pt; font-weight:700; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
import Mood.resource_rc
