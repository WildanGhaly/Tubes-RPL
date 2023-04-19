import sys
# import resource_rc
from Mood.ui_mood_input_rev1 import Ui_Form as uMoodInput 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout,QSizePolicy
from PyQt5 import QtWidgets
from datetime import date, datetime
from Mood.mood_service import Mood_Service

class Mood_Form(QWidget, uMoodInput, Mood_Service):
    def __init__(self):
        super().__init__()
        Mood_Service.__init__(self)
        self.setupUi(self)
        self.submitButtonMood.clicked.connect(self.do_something)
        self.pushButton_back.clicked.connect(self.back_to_main_menu)
        
    def do_something(self):
        now = datetime.now().strftime("%H%M%S")
        dateNow = date.today().strftime("%Y%m%d")
        hasilData = []
        hasilData.append(dateNow)
        hasilData.append(now)
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
        
        from MainMenu.main_menu_GUI import Main_Menu_GUI as uw
        self.main_menu = uw()
        self.main_menu.show()
        self.hide()

    def back_to_main_menu(self):
        from MainMenu.main_menu_GUI import Main_Menu_GUI as uw
        self.main_menu = uw()
        self.main_menu.show()
        self.hide()

# app = QtWidgets.QApplication(sys.argv)

# window = Mood_Form()
# window.show()

# sys.exit(app.exec_())
