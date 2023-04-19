import Quotes.rc_popup
import Quotes.Quotes_Popup as uw 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout,QSizePolicy
import sys
from PyQt5 import QtWidgets
from datetime import date, datetime

class Quotes_Popup_Call(QWidget, uw.QPopUp):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)

# app = QtWidgets.QApplication(sys.argv)

# MainWindow = Quotes_Popup_Call()
# MainWindow.show()


# sys.exit(app.exec_())