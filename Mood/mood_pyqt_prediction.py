import resource_rc
import ui_mood_prediction as uw 
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout,QSizePolicy
import sys
from PySide6 import QtWidgets
from datetime import date, datetime
from mood_service import Mood_Service

class Mood_Prediction(QWidget, uw.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
                
app = QtWidgets.QApplication(sys.argv)

window = Mood_Prediction()
window.show()

app.exec()