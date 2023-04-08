# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mood_visual.ui'
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
        self.mood_visual_background = QLabel(Form)
        self.mood_visual_background.setObjectName(u"mood_visual_background")
        self.mood_visual_background.setGeometry(QRect(0, 0, 1920, 1080))
        sizePolicy.setHeightForWidth(self.mood_visual_background.sizePolicy().hasHeightForWidth())
        self.mood_visual_background.setSizePolicy(sizePolicy)
        self.mood_visual_background.setMinimumSize(QSize(1920, 1080))
        self.mood_visual_background.setMaximumSize(QSize(1920, 1080))
        self.mood_visual_background.setStyleSheet(u"border-image: url(:/newPrefix/images/mood_visual.jpg);")
        self.label_one_day_mood = QLabel(Form)
        self.label_one_day_mood.setObjectName(u"label_one_day_mood")
        self.label_one_day_mood.setGeometry(QRect(327, 374, 490, 490))
        sizePolicy.setHeightForWidth(self.label_one_day_mood.sizePolicy().hasHeightForWidth())
        self.label_one_day_mood.setSizePolicy(sizePolicy)
        self.label_one_day_mood.setMinimumSize(QSize(490, 490))
        self.label_one_day_mood.setMaximumSize(QSize(711, 490))
        self.label_one_day_mood.setStyleSheet(u"font: 700 italic 51pt \"Comic Sans MS\";")
        self.label_one_week_mood = QLabel(Form)
        self.label_one_week_mood.setObjectName(u"label_one_week_mood")
        self.label_one_week_mood.setGeometry(QRect(1104, 374, 490, 490))
        sizePolicy.setHeightForWidth(self.label_one_week_mood.sizePolicy().hasHeightForWidth())
        self.label_one_week_mood.setSizePolicy(sizePolicy)
        self.label_one_week_mood.setMinimumSize(QSize(490, 490))
        self.label_one_week_mood.setMaximumSize(QSize(490, 490))
        self.label_one_week_mood.setStyleSheet(u"font: 700 italic 51pt \"Comic Sans MS\";")
        self.mood_visual_next = QPushButton(Form)
        self.mood_visual_next.setObjectName(u"mood_visual_next")
        self.mood_visual_next.setGeometry(QRect(1660, 945, 211, 91))
        self.mood_visual_next.setFlat(True)
        self.mood_visual_select_date = QPushButton(Form)
        self.mood_visual_select_date.setObjectName(u"mood_visual_select_date")
        self.mood_visual_select_date.setGeometry(QRect(541, 968, 197, 45))
        self.mood_visual_select_date.setContextMenuPolicy(Qt.NoContextMenu)
        self.mood_visual_select_date.setStyleSheet(u"font: 900 italic 16pt \"Segoe UI\";\n"
"color: rgb(168, 168, 168);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.mood_visual_background.setText("")
        self.label_one_day_mood.setText("")
        self.label_one_week_mood.setText("")
        self.mood_visual_next.setText("")
        self.mood_visual_select_date.setText(QCoreApplication.translate("Form", u"SELECT", None))
    # retranslateUi

