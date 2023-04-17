import Journal.Journal_rc
import Journal.JournalInput_GUI as uw 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout,QSizePolicy
import sys
from PyQt5 import QtWidgets
from datetime import date, datetime

class Journal_GUI_Call(QWidget, uw.JournalInput):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)

# app = QtWidgets.QApplication(sys.argv)

# window = Journal_GUI_Call()
# window.show()

# sys.exit(app.exec_())