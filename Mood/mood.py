import csv

class mood:
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
            
    