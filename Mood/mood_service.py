import mood as m
import csv

class Mood_Service(m.mood):
    def __init__(self):
        super().__init__()
    
    def validate_mood(self, moods):
        return True
    
    