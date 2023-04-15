# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mood_input_rev1.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QSlider, QWidget)
import resource_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1360, 720)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(1360, 720))
        Form.setMaximumSize(QSize(1360, 720))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setGeometry(QRect(0, 0, 1360, 720))
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(1360, 720))
        self.label.setMaximumSize(QSize(1360, 720))
        self.label.setStyleSheet(u"background-image: url(:/PrefixV1/images/mood input fg.png);")
        self.horizontalSlider_joy = QSlider(Form)
        self.horizontalSlider_joy.setObjectName(u"horizontalSlider_joy")
        self.horizontalSlider_joy.setGeometry(QRect(185, 226, 375, 26))
        self.horizontalSlider_joy.setOrientation(Qt.Horizontal)
        self.horizontalSlider_sadness = QSlider(Form)
        self.horizontalSlider_sadness.setObjectName(u"horizontalSlider_sadness")
        self.horizontalSlider_sadness.setGeometry(QRect(185, 344, 375, 26))
        self.horizontalSlider_sadness.setOrientation(Qt.Horizontal)
        self.horizontalSlider_anger = QSlider(Form)
        self.horizontalSlider_anger.setObjectName(u"horizontalSlider_anger")
        self.horizontalSlider_anger.setGeometry(QRect(185, 459, 375, 26))
        self.horizontalSlider_anger.setOrientation(Qt.Horizontal)
        self.horizontalSlider_fear = QSlider(Form)
        self.horizontalSlider_fear.setObjectName(u"horizontalSlider_fear")
        self.horizontalSlider_fear.setGeometry(QRect(185, 573, 375, 26))
        self.horizontalSlider_fear.setOrientation(Qt.Horizontal)
        self.horizontalSlider_disgust = QSlider(Form)
        self.horizontalSlider_disgust.setObjectName(u"horizontalSlider_disgust")
        self.horizontalSlider_disgust.setGeometry(QRect(817, 226, 375, 26))
        self.horizontalSlider_disgust.setOrientation(Qt.Horizontal)
        self.horizontalSlider_surprise = QSlider(Form)
        self.horizontalSlider_surprise.setObjectName(u"horizontalSlider_surprise")
        self.horizontalSlider_surprise.setGeometry(QRect(817, 344, 375, 26))
        self.horizontalSlider_surprise.setOrientation(Qt.Horizontal)
        self.horizontalSlider_trust = QSlider(Form)
        self.horizontalSlider_trust.setObjectName(u"horizontalSlider_trust")
        self.horizontalSlider_trust.setGeometry(QRect(817, 459, 375, 26))
        self.horizontalSlider_trust.setOrientation(Qt.Horizontal)
        self.horizontalSlider_anticipation = QSlider(Form)
        self.horizontalSlider_anticipation.setObjectName(u"horizontalSlider_anticipation")
        self.horizontalSlider_anticipation.setGeometry(QRect(817, 573, 375, 26))
        self.horizontalSlider_anticipation.setOrientation(Qt.Horizontal)
        self.submitButtonMood = QPushButton(Form)
        self.submitButtonMood.setObjectName(u"submitButtonMood")
        self.submitButtonMood.setGeometry(QRect(1130, 650, 150, 50))
        self.submitButtonMood.setMinimumSize(QSize(0, 50))
        self.submitButtonMood.setMaximumSize(QSize(150, 50))
        self.submitButtonMood.setStyleSheet(u"\n"
"font: 700 20pt \"Segoe Script\";\n"
"alternate-background-color: rgb(255, 85, 0);\n"
"selection-color: rgb(170, 0, 0);\n"
"selection-background-color: rgb(170, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"border-image: url(:/PrefixV1/images/submit button.png);")
        icon = QIcon()
        iconThemeName = u"application-x-executable"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.submitButtonMood.setIcon(icon)
        self.submitButtonMood.setIconSize(QSize(150, 50))
        self.submitButtonMood.setAutoDefault(False)
        self.submitButtonMood.setFlat(False)

        self.retranslateUi(Form)

        self.submitButtonMood.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.submitButtonMood.setText("")
    # retranslateUi

