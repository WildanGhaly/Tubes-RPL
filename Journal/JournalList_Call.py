import Journal.Journal_rc
import Journal.JournalList_GUI as uw 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout,QSizePolicy
import sys
from PyQt5 import QtWidgets, QtCore
from datetime import date, datetime
from Journal.JournalDatabase import JournalDatabase
from Mood.mood_pyqt_visual_calendar import Mood_Form_Calendar as mfc

class Journal_GUI_Call(QWidget, uw.JournalList, JournalDatabase):
    def __init__(self):
        super().__init__()
        JournalDatabase.__init__(self)
        self.setupUi(self)
        self.dateChoose.clicked.connect(self.chooseDate)
        self.dRight.clicked.connect(self.do_something_right)
        self.dLeft.clicked.connect(self.do_something_left)
    def chooseDate(self):
        self.dateChoice = mfc()
        self.dateChoice.show()
        self.dateChoice.calendar_mood_visual_ok.clicked.connect(self.do_something_calendar_ok) # taken from mood
        self.dateChoice.calendar_mood_visual_cancel.clicked.connect(self.do_somethong_calendar_cancel)
    def do_something_calendar_ok(self):
        self.dateChoice.close()
        self.dateChoose.setText(self.dateChoice.calendar_mood_visual.selectedDate().toString(Qt.ISODate))
        self.calculate_journal()
    def do_somethong_calendar_cancel(self):
        self.dateChoice.close()
    def calculate_journal(self):
        self.date_choosen = self.dateChoose.text().replace("-","")
        self.journal_text = self.findJournal(self.date_choosen)
        
        print(self.journal_text)
        if (self.journal_text == None):
            # TIDO set text di label (buat label dulu)
            pass
        else:
            # TIDO set text di label (buat label dulu)
            pass
        
    def do_something_right(self):
        selected_date_str = self.dateChoose.text()
        selected_date = QtCore.QDate.fromString(selected_date_str, "yyyy-MM-dd")
        next_date = selected_date.addDays(-1)
        date_string = next_date.toString(Qt.ISODate)
        self.dateChoose.setText(date_string)
        self.calculate_journal()
    def do_something_left(self):
        selected_date_str = self.dateChoose.text()
        selected_date = QtCore.QDate.fromString(selected_date_str, "yyyy-MM-dd")
        previous_date = selected_date.addDays(1)
        date_string = previous_date.toString(Qt.ISODate)
        self.dateChoose.setText(date_string)
        self.calculate_journal()


# app = QtWidgets.QApplication(sys.argv)

# window = Journal_GUI_Call()
# window.show()

# sys.exit(app.exec_())