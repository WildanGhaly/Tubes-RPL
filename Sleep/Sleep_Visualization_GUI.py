import sys
import Mood.ui_mood_visual as uw
from PyQt5.QtCore import (QCoreApplication, QDateTime,
    QMetaObject, QRect, Qt,
    QSize)
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QDateEdit, QLabel, QPushButton, QSizePolicy, QWidget)
from PyQt5 import QtWidgets
from Sleep.Sleep import Sleep
from Sleep.Sleep_Plot import *
from Mood.mood_pyqt_visual_calendar import Mood_Form_Calendar as mfc

class Ui_Widget(QWidget, Sleep, uw.Ui_Form):
    def __init__(self):
        super().__init__()
        self.title='Sleep'
        self.left = 0
        self.top = 0
        self.width = 1366
        self.height = 720
        self.sleep_visual_selected_to_calculate = ''
        self.setupUi(self)
        self.start = []
        self.dur = []
        self.end = []
        
    def do_something_select_date(self):
        self.input_cal = mfc()
        self.input_cal.show()
        self.input_cal.calendar_mood_visual_ok.clicked.connect(self.do_something_calendar_ok)
        self.input_cal.calendar_mood_visual_cancel.clicked.connect(self.do_somethong_calendar_cancel)

    def do_something_calendar_ok(self):
        self.input_cal.close()
        self.dateEdit.setText(self.input_cal.calendar_mood_visual.selectedDate().toString(Qt.ISODate))
        self.sleep_visual_selected_to_calculate = str(self.input_cal.calendar_mood_visual.selectedDate().toString("ddMMyyyy"))
        # print (self.sleep_visual_selected_to_calculate)
        self.start = self.getWeekStartSleepHour(id=self.sleep_visual_selected_to_calculate)
        self.dur = self.getWeekSleepDuration(id=self.sleep_visual_selected_to_calculate)
        self.end = self.getWeekEndSleepHour(id=self.sleep_visual_selected_to_calculate)
        startSleepChart = PlotCanvas(self , 4, 4, 100, self.start, 'start')
        startSleepChart.move(149,265)
        durationSleep = PlotCanvas(self , 4, 4, 100, self.dur, 'duration')
        durationSleep.move(520,265)
        endSleepChart = PlotCanvas(self , 4, 4, 100, self.end, 'end')
        endSleepChart.move(890,265)
        self.labelStart.clear()
        self.labelDur.clear()
        self.labelEnd.clear()
        self.labelStart.setStyleSheet("border-image: url(./Sleep/vis_result/start.png)")
        self.labelDur.setStyleSheet("border-image: url(./Sleep/vis_result/duration.png)")
        self.labelEnd.setStyleSheet("border-image: url(./Sleep/vis_result/end.png)")
    def do_somethong_calendar_cancel(self):
        print ("cancel")
        self.input_cal.close()
    
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
        self.bg = QLabel(Widget)
        self.bg.setObjectName(u"label")
        self.bg.setEnabled(True)
        self.bg.setGeometry(QRect(0, 0, 1366, 720))
        sizePolicy.setHeightForWidth(self.bg.sizePolicy().hasHeightForWidth())
        self.bg.setSizePolicy(sizePolicy)
        self.bg.setMinimumSize(QSize(1366, 720))
        self.bg.setMaximumSize(QSize(1366, 720))
        self.bg.setStyleSheet(u"border-image: url(./Sleep/vstock/background.jpg)")
        self.sleepViz = QLabel(Widget)
        self.sleepViz.setObjectName(u"label")
        self.sleepViz.setEnabled(True)
        self.sleepViz.setGeometry(QRect(0, 0, 1366, 720))
        sizePolicy.setHeightForWidth(self.sleepViz.sizePolicy().hasHeightForWidth())
        self.sleepViz.setSizePolicy(sizePolicy)
        self.sleepViz.setMinimumSize(QSize(1366, 720))
        self.sleepViz.setMaximumSize(QSize(1366, 720))
        self.sleepViz.setStyleSheet(u"border-image: url(./Sleep/vstock/sleep time visualization fg.png)")

        self.nextButton = QPushButton(Widget)
        self.nextButton.setObjectName(u"nextButton")
        self.nextButton.setGeometry(QRect(1165, 617, 155, 72))
        self.nextButton.setStyleSheet(u"QPushButton{background: transparent;}")
        self.nextButton.clicked.connect(self.next)
        
        font = QFont()
        font.setPointSize(20)
        # self.nextButton.setFont(font)
        self.dateEdit = QPushButton(Widget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(378, 630, 150, 45))
        self.dateEdit.setStyleSheet("\n"
            "font: 700 10pt \"Segoe Script\";\n"
            "alternate-background-color: rgb(255, 85, 0);\n"
            "selection-color: rgb(170, 0, 0);\n"
            "selection-background-color: rgb(170, 0, 0);\n"
            "border-color: rgb(0, 0, 0);\n")
        self.dateEdit.clicked.connect(self.do_something_select_date)
        #Start Sleep Chart
        self.labelStart = QLabel(Widget)
        self.labelStart.setObjectName(u"StartChart")
        self.labelStart.setEnabled(True)
        self.labelStart.setGeometry(149,265,330,300)
        
        #Duration Sleep Chart
        self.labelDur = QLabel(Widget)
        self.labelDur.setObjectName(u"DurChart")
        self.labelDur.setEnabled(True)
        self.labelDur.setGeometry(520,265,330,300)
        #endSleepChart
        self.labelEnd = QLabel(Widget)
        self.labelEnd.setObjectName(u"EndChart")
        self.labelEnd.setEnabled(True)
        self.labelEnd.setGeometry(890,265,330,300)
        
        # self.nextButton.raise_()
        self.dateEdit.raise_()
        self.retranslateUi(Widget)
        QMetaObject.connectSlotsByName(Widget)
        self.show()
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.nextButton.setText(QCoreApplication.translate("Widget", u"", None))
        self.dateEdit.setText(QCoreApplication.translate("Widget", u"SELECT", None))
        self.sleepViz.setText("")
    # retranslateUi
    
    def getDate(self):
        return self.dateEdit.dateTime()

    def next(self):
        from MainMenu.main_menu_GUI import Main_Menu_GUI
        self.main_menu = Main_Menu_GUI()
        self.main_menu.show()
        self.hide()


# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)

#     window = Ui_Widget()
#     window.show()

#     app.exec()