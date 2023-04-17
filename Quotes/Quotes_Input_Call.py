import Quotes.rc_input
import Quotes.Quotes_Input_GUI as uw 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout,QSizePolicy
import sys
from PyQt5 import QtWidgets
from datetime import date, datetime

class Quotes_Input_Call(QWidget, uw.QInput):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)

# app = QtWidgets.QApplication(sys.argv)

# MainWindow = Sleep_Input_Call()
# MainWindow.show()


# sys.exit(app.exec_())