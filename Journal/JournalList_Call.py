import Journal.Journal_rc
import Journal.JournalList_GUI as uw 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout,QSizePolicy
import sys
from PyQt5 import QtWidgets
from datetime import date, datetime
from Journal.JournalDatabase import JournalDatabase
from Mood.mood_pyqt_visual_calendar import Mood_Form_Calendar as mfc

class Journal_GUI_Call(QWidget, uw.JournalList, JournalDatabase):
    def __init__(self):
        super().__init__()
        JournalDatabase.__init__(self)
        self.setupUi(self)
        self.dateChoose.clicked.connect(self.chooseDate)
    def chooseDate(self):
        self.dateChoice = mfc()
        self.dateChoice.show()
        self.dateChoice.calendar_mood_visual_ok.clicked.connect(self.do_something_calendar_ok) # taken from mood
        self.dateChoice.calendar_mood_visual_cancel.clicked.connect(self.do_somethong_calendar_cancel)
    def do_something_calendar_ok(self):
        self.dateChoice.close()
        self.dateChoose.setText(self.dateChoice.calendar_mood_visual.selectedDate().toString(Qt.ISODate))
    def do_somethong_calendar_cancel(self):
        self.dateChoice.close()

# app = QtWidgets.QApplication(sys.argv)

# window = Journal_GUI_Call()
# window.show()

# sys.exit(app.exec_())