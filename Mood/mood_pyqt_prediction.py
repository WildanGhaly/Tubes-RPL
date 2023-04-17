import Mood.resource_rc
import Mood.ui_mood_prediction as uw 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout,QSizePolicy
import sys
from PyQt5 import QtWidgets
from datetime import date, datetime
from Mood.mood_service import Mood_Service
import numpy as np
import matplotlib.pyplot as plt

class Mood_Prediction(QWidget, uw.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.calculate_mood_prediction()
        self.mood_prediction_next_button.clicked.connect(self.do_something_next)
    
    def do_something_next(self):
        from MainMenu.main_menu_GUI import Main_Menu_GUI as uw
        self.main_menu = uw()
        self.main_menu.show()
        self.hide()
    
    def calculate_mood_prediction(self):
        self.mood = Mood_Service()
        dateNow = date.today().strftime("%Y%m%d")
        self.mood_found = self.mood.find_mood(dateNow)
        count = 0;
        data = [];
        week = [];
        print("=================================")
        for i in range (30):
            self.mood_found = self.mood.find_mood(dateNow)
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
            
            dateNow = Mood_Service.subtract_one_day(dateNow)
            # print(count)
            if count == 15:
                break
        
        print("Count", count)
        print("=================================")
        for i in range (len(data)):
            print(data[i])
        print("=================================")
        print(week)
    
        if count == 15:
            self.predict_data = []
            num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
            fig, ax = plt.subplots()
            new_one_data = []
            self.category = ['Joy', 'Sadness', 'Anger', 'Fear', 'Disgust', 'Surprise', 'Trust', 'Anticipation']
            for i in range (8):
                avg_prediction = 0;
                new_one_data.clear()
                for j in range (15):
                    new_one_data.append(data[j][i])
                    avg_prediction += data[j][i]
                avg_prediction = avg_prediction/15
                self.predict_data.append(avg_prediction)
                ax.plot(num, new_one_data, label=self.category[i])

            plt.gca().invert_xaxis()
            ax.legend()
            plt.savefig('./Mood/images/mood_visual_fifteen_days_result.png')
            self.mood_prediction_graph.clear()
            self.mood_prediction_graph.setStyleSheet("border-image: url(./Mood/images/mood_visual_fifteen_days_result.png);")
            self.show_mood_prediction()
            
        else:
            self.mood_prediction_graph.clear()
            self.mood_prediction_graph.setStyleSheet(u"font: 700 italic 51pt \"Comic Sans MS\";")
            self.mood_prediction_graph.setText("  Data is\n  not enough")
            
    def show_mood_prediction(self):
        plt.style.use('ggplot')
        subjects=self.category
        theRadar=self.predict_data

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
        plt.savefig('./Mood/images/mood_prediction_result.png')
        
        self.mood_prediction_label.clear()
        self.mood_prediction_label.setStyleSheet("border-image: url(./Mood/images/mood_prediction_result.png);")
                
# app = QtWidgets.QApplication(sys.argv)

# window = Mood_Prediction()
# window.show()

# sys.exit(app.exec_())