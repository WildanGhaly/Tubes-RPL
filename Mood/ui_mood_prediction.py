# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mood_prediction.ui'
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
    QWidget)
import resource_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1920, 1080)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(1920, 1080))
        Form.setMaximumSize(QSize(1920, 1080))
        self.mood_prediction_background = QLabel(Form)
        self.mood_prediction_background.setObjectName(u"mood_prediction_background")
        self.mood_prediction_background.setGeometry(QRect(0, 0, 1920, 1080))
        sizePolicy.setHeightForWidth(self.mood_prediction_background.sizePolicy().hasHeightForWidth())
        self.mood_prediction_background.setSizePolicy(sizePolicy)
        self.mood_prediction_background.setMinimumSize(QSize(1920, 1080))
        self.mood_prediction_background.setMaximumSize(QSize(1920, 1080))
        self.mood_prediction_background.setStyleSheet(u"background-image: url(:/newPrefix/images/mood_prediction.jpg);")
        self.mood_prediction_graph = QLabel(Form)
        self.mood_prediction_graph.setObjectName(u"mood_prediction_graph")
        self.mood_prediction_graph.setGeometry(QRect(217, 372, 713, 493))
        self.mood_prediction_graph.setStyleSheet(u"font: 700 italic 51pt \"Comic Sans MS\";")
        self.mood_prediction_label = QLabel(Form)
        self.mood_prediction_label.setObjectName(u"mood_prediction_label")
        self.mood_prediction_label.setGeometry(QRect(1180, 372, 355, 355))
        self.mood_prediction_label.setStyleSheet(u"font: 700 italic 51pt \"Comic Sans MS\";")
        self.mood_prediction_saran_button = QPushButton(Form)
        self.mood_prediction_saran_button.setObjectName(u"mood_prediction_saran_button")
        self.mood_prediction_saran_button.setGeometry(QRect(1080, 778, 540, 71))
        self.mood_prediction_saran_button.setFlat(True)
        self.mood_prediction_next_button = QPushButton(Form)
        self.mood_prediction_next_button.setObjectName(u"mood_prediction_next_button")
        self.mood_prediction_next_button.setGeometry(QRect(1690, 942, 151, 97))
        self.mood_prediction_next_button.setFlat(True)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.mood_prediction_background.setText("")
        self.mood_prediction_graph.setText("")
        self.mood_prediction_label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Belum Bisa</p><p>Ditentukan</p></body></html>", None))
        self.mood_prediction_saran_button.setText("")
        self.mood_prediction_next_button.setText("")
    # retranslateUi

