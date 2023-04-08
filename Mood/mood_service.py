from mood import Mood as m
import csv

class Mood_Service(m):
    def __init__(self):
        super().__init__()
    
    def validate_mood(self, moods):
        return True
    
    def add_mood(self, moods):
        if not self.validate_mood(moods):
            return False
        
        self.mood.append(self.moodToInt(moods))
        
        with open(self.filename, 'w', newline='') as file:
            csv.writer(file).writerows([['ID','Joy', 'Sadness', 'Anger', 'Fear', 'Disgust', 'Surprise', 'Trust', 'Anticipation']] + self.mood)
        
        return True;
    