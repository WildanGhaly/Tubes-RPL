# import resource_rc
import History.history as uw 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout,QSizePolicy
import sys
from PyQt5 import QtWidgets
from datetime import date, datetime

class history_GUI(QWidget, uw.Ui_MainWindows):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    