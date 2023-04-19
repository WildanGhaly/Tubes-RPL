import Mood.resource_rc
import Mood.ui_mood_feedback as uw 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout,QSizePolicy
import sys
from PyQt5 import QtWidgets
from datetime import date, datetime
import csv

class Mood_Feedback(QWidget, uw.Ui_mood_feedback):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.submit_button.clicked.connect(self.submit_button_click)
        
    def submit_button_click(self):
        if (self.text_edit.toPlainText() == ""):
            self.text_edit.setText("No feedback")
        filename = "Mood/feedback.csv"
        header = ["rating", "feedback"]
        rating = str(self.rating_slider.value())
        feedback = self.text_edit.toPlainText()

        with open(filename, mode="a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([rating, feedback])
    
        from MainMenu.main_menu_GUI import Main_Menu_GUI as uw
        self.main_menu = uw()
        self.main_menu.show()
        self.hide()
        