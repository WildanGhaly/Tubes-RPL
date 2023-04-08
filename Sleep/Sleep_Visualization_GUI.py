import sys

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QFrame, QGraphicsView,
    QLabel, QPushButton, QSizePolicy, QWidget)

from Sleep_Plot import *

class Ui_Widget(QWidget):
    def __init__(self):
        
        super().__init__()
        self.title='Sleep'
        self.left = 0
        self.top = 0
        self.width = 1920
        self.height = 1080
        self.setupUi(self)
    
    def setupUi(self, Widget):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1920, 1080)
        Widget.setMinimumSize(QSize(1920, 1080))
        Widget.setSizeIncrement(QSize(1920, 1080))
        Widget.setBaseSize(QSize(1920, 1080))
        
        self.pushButton = QPushButton(Widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(1720, 900, 170, 80))
        
        font = QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.dateEdit = QDateEdit(Widget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(400, 915, 171, 41))
        self.pilihTanggalText = QLabel(Widget)
        self.pilihTanggalText.setObjectName(u"pilihTanggalText")
        self.pilihTanggalText.setGeometry(QRect(220, 900, 371, 61))
        self.pilihTanggalText.setFont(font)
        
        #BackGround
        # self.background = QGraphicsView(Widget)
        # self.background.setObjectName(u"background")
        # self.background.setGeometry(QRect(0, 0, 1920, 1080))
        # self.background.setMinimumSize(QSize(1920, 1080))
        # self.background.setMaximumSize(QSize(1920, 1080))
        
        #Judul
        self.JudulText = QLabel(Widget)
        self.JudulText.setObjectName(u"JudulText")
        self.JudulText.setGeometry(QRect(100, 30, 1691, 71))
        self.JudulText.setAlignment(Qt.AlignCenter)
        self.JudulText.setFont(font)
        
        #Start Sleep Chart
        startSleepChart = PlotCanvas(self, width=5, height=4)
        startSleepChart.move(20,250)
        # self.frame = QFrame(startSleepChart)
        # self.frame.setObjectName(u"frame")
        # self.frame.setGeometry(QRect(20, 250, 600, 600))
        # self.frame.setFrameShape(QFrame.StyledPanel)
        # self.frame.setFrameShadow(QFrame.Raised)
        self.startSleepChart = QLabel(Widget)
        self.startSleepChart.setObjectName(u"startSleepChart")
        self.startSleepChart.setGeometry(QRect(20, 180, 601, 71))
        self.startSleepChart.setAlignment(Qt.AlignCenter)
        
        #Duration Sleep Chart
        durationSleep = PlotCanvas(self, width=5, height=4)
        durationSleep.move(650,250)
        self.durationSleepChart = QLabel(Widget)
        self.durationSleepChart.setObjectName(u"durationSleepChart")
        self.durationSleepChart.setGeometry(QRect(650, 180, 601, 71))
        self.durationSleepChart.setAlignment(Qt.AlignCenter)
        # self.frame_2 = QFrame(Widget)
        # self.frame_2.setObjectName(u"frame_2")
        # self.frame_2.setGeometry(QRect(650, 250, 600, 600))
        # self.frame_2.setFrameShape(QFrame.StyledPanel)
        # self.frame_2.setFrameShadow(QFrame.Raised)
        
        #endSleepChart
        self.endSleepChart = QLabel(Widget)
        self.endSleepChart.setObjectName(u"endSleepChart")
        self.endSleepChart.setGeometry(QRect(1270, 180, 601, 71))
        self.endSleepChart.setAlignment(Qt.AlignCenter)
        endSleepChart = PlotCanvas(self, width=5, height=4)
        endSleepChart.move(1270,250)
        # self.frame_3 = QFrame(Widget)
        # self.frame_3.setObjectName(u"frame_3")
        # self.frame_3.setGeometry(QRect(1270, 250, 600, 600))
        # self.frame_3.setFrameShape(QFrame.StyledPanel)
        # self.frame_3.setFrameShadow(QFrame.Raised)
        
        
        # self.background.raise_()
        self.pilihTanggalText.raise_()
        self.pushButton.raise_()
        self.dateEdit.raise_()
        self.JudulText.raise_()
        # self.frame.raise_()
        self.startSleepChart.raise_()
        self.durationSleepChart.raise_()
        # self.frame_2.raise_()
        self.endSleepChart.raise_()
        # self.frame_3.raise_()

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
        
        self.show()
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"NEXT", None))
        self.pilihTanggalText.setText(QCoreApplication.translate("Widget", u"Pilih Tanggal:", None))
        self.JudulText.setText(QCoreApplication.translate("Widget", u"Sleep Time Visualization", None))
        self.startSleepChart.setText(QCoreApplication.translate("Widget", u" Start Sleep Chart", None))
        self.durationSleepChart.setText(QCoreApplication.translate("Widget", u" Start Sleep Chart", None))
        self.endSleepChart.setText(QCoreApplication.translate("Widget", u" Start Sleep Chart", None))
    # retranslateUi

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ui_Widget()
    sys.exit(app.exec_())