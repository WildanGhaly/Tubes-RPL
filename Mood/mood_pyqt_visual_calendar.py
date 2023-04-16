import Mood.resource_rc
import Mood.ui_mood_visual_calendar as uw 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout,QSizePolicy
import sys
from PyQt5 import QtWidgets
from datetime import date, datetime
from Mood.mood_service import Mood_Service

class Mood_Form_Calendar(QWidget, uw.Ui_Dialog):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    
        
