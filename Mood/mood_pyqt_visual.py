import resource_rc
import ui_mood_visual as uw 
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
import sys
from PySide6 import QtWidgets
from mood_service import Mood_Service
from mood_pyqt_visual_calendar import Mood_Form_Calendar as mfc
import plotly.graph_objects as go
import numpy as np
import matplotlib.pyplot as plt

class Mood_Visual(QWidget, uw.Ui_Form):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.mood_visual_select_date.clicked.connect(self.do_something_select_date)
        
    def do_something_select_date(self):
        self.input_cal = mfc()
        self.input_cal.show()
        self.input_cal.calendar_mood_visual_ok.clicked.connect(self.do_something_calendar_ok)
        self.input_cal.calendar_mood_visual_cancel.clicked.connect(self.do_somethong_calendar_cancel)

    def do_something_calendar_ok(self):
        self.input_cal.close()
        self.mood_visual_select_date.setText(self.input_cal.calendar_mood_visual.selectedDate().toString(Qt.ISODate))
        self.mood_visual_selected_to_calculate = int(self.input_cal.calendar_mood_visual.selectedDate().toString("yyyyMMdd"))
        print (self.mood_visual_selected_to_calculate)
        self.calculate_one_day()
        self.calculate_one_week()
        
    def do_somethong_calendar_cancel(self):
        print ("cancel")
        self.input_cal.close()
        
    def calculate_one_day(self):
        self.mood = Mood_Service()
        self.mood_found = self.mood.find_mood(self.mood_visual_selected_to_calculate)
        if (self.mood_found == []):
            self.label_one_day_mood.clear()
            self.label_one_day_mood.setStyleSheet(u"font: 700 italic 51pt \"Comic Sans MS\";")
            self.label_one_day_mood.setText("No data found")
            # self.layout().addWidget(self.label_one_day_mood)
        else:
            self.mood_8 = [0,0,0,0, 0,0,0,0]
            for j in range (8):
                for i in range (len(self.mood_found)):
                    self.mood_8[j] += int(self.mood_found[i][j+2])
                self.mood_8[j] = self.mood_8[j]/len(self.mood_found)
            
            category = ['joy','sadness','anger','fear',
                        'disgust','surprise','trust','anticipation']
            
            plt.style.use('ggplot')

            subjects=category
            theRadar=self.mood_8

            angles=np.linspace(0,2*np.pi,len(subjects), endpoint=False)
            angles=np.concatenate((angles,[angles[0]]))

            subjects.append(subjects[0])
            theRadar.append(theRadar[0])

            fig=plt.figure(figsize=(6,6))
            ax=fig.add_subplot(polar=True)
            ax.plot(angles,theRadar, 'o--', color='g', label='Mood')

            ax.fill(angles, theRadar, alpha=0.25, color='g')
            ax.set_thetagrids(angles * 180/np.pi, subjects)

            plt.grid(True)
            plt.tight_layout()
            plt.legend()
            plt.savefig('./images/mood_visual_one_day_result.png')
            
            self.label_one_day_mood.clear()
            self.label_one_day_mood.setStyleSheet("border-image: url(./images/mood_visual_one_day_result.png);")
            
    def calculate_one_week(self):
        self.mood = Mood_Service()
        self.mood_found = self.mood.find_mood(self.mood_visual_selected_to_calculate)
        if (self.mood_found == []):
            self.label_one_week_mood.clear()
            self.label_one_week_mood.setStyleSheet(u"font: 700 italic 51pt \"Comic Sans MS\";")
            self.label_one_week_mood.setText("No data found")
        else:
            count = 0;
            data = [];
            week = [];
            print("=================================")
            for i in range (30):
                self.mood_found = self.mood.find_mood(self.mood_visual_selected_to_calculate)
                if (self.mood_found != []):
                    self.mood_8 = [0,0,0,0, 0,0,0,0]
                    for j in range (8):
                        for k in range (len(self.mood_found)):
                            self.mood_8[j] += int(self.mood_found[k][j+2])
                        self.mood_8[j] = self.mood_8[j]/len(self.mood_found)
                    data.append(self.mood_8)
                    count += 1
                    week.append(self.mood_found[0][0])
                    print (self.mood_found[0][0])
                
                self.mood_visual_selected_to_calculate = Mood_Service.subtract_one_day(self.mood_visual_selected_to_calculate)
                # print(count)
                if count == 7:
                    break
            
            print("Count", count)
            print("=================================")
            for i in range (len(data)):
                print(data[i])
            print("=================================")
            print(week)
        
            if count == 7:
                num = [1,2,3,4,5,6,7]
                fig, ax = plt.subplots()
                new_data = []
                new_one_data = []
                category = ['Joy', 'Sadness', 'Anger', 'Fear', 'Disgust', 'Surprise', 'Trust', 'Anticipation']
                for i in range (8):
                    new_one_data.clear()
                    for j in range (7):
                        new_one_data.append(data[j][i])
                    print(new_data)
                    ax.plot(num, new_one_data, label=category[i])

                ax.legend()
                plt.savefig('./images/mood_visual_one_week_result.png')
                self.label_one_week_mood.clear()
                self.label_one_week_mood.setStyleSheet("border-image: url(./images/mood_visual_one_week_result.png);")
            else:
                self.label_one_week_mood.clear()
                self.label_one_week_mood.setStyleSheet(u"font: 700 italic 51pt \"Comic Sans MS\";")
                self.label_one_week_mood.setText("Data is\nnot enough")
    
app = QtWidgets.QApplication(sys.argv)

window = Mood_Visual()
window.show()

app.exec()