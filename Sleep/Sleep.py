import csv
import csv
import datetime
class Sleep:
    def sleepToInt(self, row):
        return [
            int(row[0]), int(row[1]), int(row[2]),
            int(row[3])
        ]
    def __init__(self):
        self.filename = './Sleep/Sleep.csv'
        with open(self.filename, 'r') as file:
            csvreader = csv.reader(file)
            next(csvreader)  # Skip header row
            self.sleep = [self.sleepToInt(row)
                         for row in csvreader]

    def get_sleep_id(self, index):
        return self.sleep[index][0]
    
    def add_Sleep(self, sleepAdd):
        self.sleep.append(sleepAdd)
        print(sleepAdd)
        
        with open(self.filename, 'w', newline='') as file:
            csv.writer(file).writerows([['Id(HHBBTTTTJJMM)','jamTidur','menitTidur','durasi(menit)']] + self.sleep)
        
    



    