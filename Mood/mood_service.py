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
            csv.writer(file).writerows([['Date', 'ID', 'Joy', 'Sadness', 'Anger', 'Fear', 'Disgust', 'Surprise', 'Trust', 'Anticipation']] + self.mood)
        
        return True
        
    # date in int format
    def find_mood(self, date):
        moodFound = []
        for i in range (0, len(self.mood)):
            if int(self.mood[i][0]) == int(date):
                moodFound.append(self.mood[i])
        return moodFound
        
    