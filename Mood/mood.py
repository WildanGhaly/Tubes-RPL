import csv

class Mood:
    # Konstruktor
    def __init__(self):
        self.filename = './mood.csv'
        with open(self.filename, 'r') as file:
            csvreader = csv.reader(file)
            next(csvreader)  # Skip header row
            self.mood = [[int(row[0]), int(row[1]), int(row[2]),
                          int(row[3]), int(row[4]), int(row[5]),
                          int(row[6]), int(row[7]), int(row[8])
                          ] for row in csvreader]
            
    def moodToInt(self, row):
        return [
            int(row[0]), int(row[1]), int(row[2]),
            int(row[3]), int(row[4]), int(row[5]),
            int(row[6]), int(row[7]), int(row[8])
        ]
    
    # Getter
    def get_mood(self, index):
        allMood = []
        for i in range (1, 9):
            allMood.append(self.mood[index][i])
        return allMood
    
    def get_mood_desc(self, index):
        allMood = []
        for i in range (0, 9):
            allMood.append(self.mood[index][i])
        return allMood

    def get_specific_mood(self, index, indexMood):
        return self.mood[index][indexMood]
    
    
# moodS = mood()
# print(moodS.get_mood(0))