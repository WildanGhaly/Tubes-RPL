import resource_rc
import ui_mood_visual as uw 
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout,QSizePolicy
import sys
from PySide6 import QtWidgets
from datetime import date, datetime
from mood_service import Mood_Service
from mood_pyqt_visual_calendar import Mood_Form_Calendar as mfc

class Mood_Visual(QWidget, uw.Ui_Form):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.mood_visual_select_date.clicked.connect(self.do_something_select_date)
        
    def do_something_select_date(self):
        self.input_cal = mfc()
        self.input_cal.show()
        self.input_cal.calendar_mood_visual_ok.clicked.connect(self.do_something_calendar_ok)
        self.input_cal.calendar_mood_visual_cancel.clicked.connect(self.do_somethong_calendar_cancel)

    def do_something_calendar_ok(self):
        print (self.input_cal.calendar_mood_visual.selectedDate().toString(Qt.ISODate))
        self.input_cal.close()
        
    def do_somethong_calendar_cancel(self):
        print ("cancel")
        self.input_cal.close()
    
app = QtWidgets.QApplication(sys.argv)

window = Mood_Visual()
window.show()

app.exec()