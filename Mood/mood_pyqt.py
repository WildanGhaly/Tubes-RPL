import resource_rc
import ui_mood_input_rev1 as uw 
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
        self.submitButtonMood.clicked.connect(self.do_something)
        
    def do_something(self):
        now = datetime.now().strftime("%H%M%S")
        dateNow = date.today().strftime("%d%m%Y")
        hasilData = []
        hasilData.append(dateNow+now)
        hasilData.append(self.horizontalSlider_joy.value())
        hasilData.append(self.horizontalSlider_sadness.value())
        hasilData.append(self.horizontalSlider_anger.value())
        hasilData.append(self.horizontalSlider_fear.value())
        hasilData.append(self.horizontalSlider_disgust.value())
        hasilData.append(self.horizontalSlider_surprise.value())
        hasilData.append(self.horizontalSlider_trust.value())
        hasilData.append(self.horizontalSlider_anticipation.value())
        
        self.add_mood(hasilData)
        
        print(hasilData)


app = QtWidgets.QApplication(sys.argv)

window = Mood_Form()
window.show()

app.exec()