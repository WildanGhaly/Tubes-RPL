import csv

class Recommendation:
    def __init__(self, sleep_date):
        self.sleep_date = sleep_date
        self.getDatabase()

    def calculate_recommendation(self):
        sleep_time = 0
        if sleep_time < 6:
            return "You should sleep more"
        elif sleep_time > 9:
            return "You should sleep less"
        else:
            return "You should sleep normally"
        
    def getDatabase(self):
        filename = './Sleep.csv'
        with open(filename, 'r') as file:
            csvreader = csv.reader(file)
            self.database = []
            next(csvreader)
            try:
                for i, baris in enumerate(csvreader):
                    if self.sleep_date == baris[0][2:8]:
                        id, jamTidur, menitTidur, durasi = map(int, baris)
                        id = str(id)
                        self.database.append([id, jamTidur, menitTidur, durasi])
            except:
                pass

# Rec = Recommendation("042023")
