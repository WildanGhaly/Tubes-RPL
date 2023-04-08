import resource_rc
import ui_mood_visual as uw 
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout,QSizePolicy
import sys
from PySide6 import QtWidgets
from datetime import date, datetime
from mood_service import Mood_Service

class Mood_Form(QWidget, uw.Ui_Form, Mood_Service):
    def __init__(self):
        super().__init__()
        Mood_Service.__init__(self)
        self.setupUi(self)
        
app = QtWidgets.QApplication(sys.argv)

window = Mood_Form()
window.show()

app.exec()