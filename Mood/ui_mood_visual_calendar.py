# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mood_visual_calendar.ui'
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QDialog, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QWidget)
import resource_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(720, 480)
        Dialog.setMinimumSize(QSize(720, 480))
        Dialog.setMaximumSize(QSize(720, 480))
        self.calendar_mood_visual = QCalendarWidget(Dialog)
        self.calendar_mood_visual.setObjectName(u"calendar_mood_visual")
        self.calendar_mood_visual.setGeometry(QRect(0, 0, 720, 431))
        self.calendar_mood_visual.setStyleSheet(u"background-image: url(:/newPrefix/images/default_background.jpg);")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 720, 480))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(720, 480))
        self.label.setMaximumSize(QSize(720, 480))
        self.label.setStyleSheet(u"border-image: url(:/newPrefix/images/default_background.jpg);")
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 440, 701, 26))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.calendar_mood_visual_ok = QPushButton(self.widget)
        self.calendar_mood_visual_ok.setObjectName(u"calendar_mood_visual_ok")
        self.calendar_mood_visual_ok.setStyleSheet(u"background-color: rgb(13, 255, 0);\n"
"font: 700 10pt \"Arial\";")

        self.horizontalLayout.addWidget(self.calendar_mood_visual_ok)

        self.calendar_mood_visual_cancel = QPushButton(self.widget)
        self.calendar_mood_visual_cancel.setObjectName(u"calendar_mood_visual_cancel")
        self.calendar_mood_visual_cancel.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"\n"
"font: 700 10pt \"Arial\";")

        self.horizontalLayout.addWidget(self.calendar_mood_visual_cancel)

        self.label.raise_()
        self.calendar_mood_visual.raise_()
        self.widget.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.calendar_mood_visual_ok.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.calendar_mood_visual_cancel.setText(QCoreApplication.translate("Dialog", u"CANCEL", None))
    # retranslateUi

