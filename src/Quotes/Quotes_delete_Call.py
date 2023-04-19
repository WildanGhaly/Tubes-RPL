# import Quotes.rc_edit
import Quotes.Quotes_Delete_GUI as uw 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout,QSizePolicy
import sys
from PyQt5 import QtWidgets
from datetime import date, datetime

class Quotes_Delete_Call(QWidget, uw.QDelete):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)