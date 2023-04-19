import Quotes.rc_edit
import Quotes.Quotes_edit_GUI as uw 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout,QSizePolicy
import sys
from PyQt5 import QtWidgets
from datetime import date, datetime

class Quotes_Edit_Call(QWidget, uw.QEdit):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)

# app = QtWidgets.QApplication(sys.argv)

# MainWindow = Sleep_Input_Call()
# MainWindow.show()


# sys.exit(app.exec_())