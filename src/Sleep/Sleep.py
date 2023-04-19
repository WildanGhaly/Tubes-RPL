import csv
import csv
import datetime
import re
class Sleep:
    def sleepToInt(self, row):
        return [
            int(row[0]), int(row[1]), int(row[2]),
            int(row[3]), int(row[4]), int(row[5])
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
    
    def getWeekSleepDuration(self, id):
        allSleep = []
        if(id==None):
            for i in range (len(self.sleep)-7, len(self.sleep)):
                allSleep.append(self.sleep[i][5])
            return allSleep
        else:
            idx = -1
            for i in range (len(self.sleep)):
                if id == (str(self.sleep[i][0]))[:8]:
                    # print((self.sleep[i][0])[:8])
                    idx = i
            
            if (idx == None):
                for i in range(idx[len(idx)-1]-7, idx[len(idx)-1]):
                    allSleep.append(self.sleep[i][5])
                return allSleep
            else:
                for i in range(idx-7, idx):
                    allSleep.append(self.sleep[i][5])
                return allSleep
    
    def getWeekEndSleepMinute(self, id):
        allSleep = []
        if(id==None):
            for i in range (len(self.sleep)-7, len(self.sleep)):
                allSleep.append(self.sleep[i][4])
            return allSleep
        else:
            idx = -1
            for i in range (len(self.sleep)):
                if id == (str(self.sleep[i][0]))[:8]:
                    # print((self.sleep[i][0])[:8])
                    idx = i
            
            if (idx == None):
                return None
            else:
                for i in range(idx-7, idx):
                    allSleep.append(self.sleep[i][4])
                return allSleep
            
    def getWeekEndSleepHour(self, id):
        allSleep = []
        if(id==None):
            for i in range (len(self.sleep)-7, len(self.sleep)):
                allSleep.append(self.sleep[i][3])
            return allSleep
        else:
            idx = -1
            for i in range (len(self.sleep)):
                if id == (str(self.sleep[i][0]))[:8]:
                    # print((self.sleep[i][0])[:8])
                    idx = i
            
            if (idx == None):
                return None
            else:
                for i in range(idx-7, idx):
                    allSleep.append(self.sleep[i][3])
                return allSleep
        
            
    def getWeekStartSleepMinute(self, id):
        allSleep = []
        if(id==None):
            for i in range (len(self.sleep)-7, len(self.sleep)):
                allSleep.append(self.sleep[i][2])
            return allSleep
        else:
            idx = -1
            for i in range (len(self.sleep)):
                if id == (str(self.sleep[i][0]))[:8]:
                    idx = i
                # print(id)
                # print((self.sleep[i][0])[:8])
            
            if (idx == None):
                return None
            else:
                for i in range(idx-7, idx):
                    allSleep.append(self.sleep[i][2])
                return allSleep
            
    def getWeekStartSleepHour(self, id: str):
        allSleep = []
        if(id==None):
            for i in range (len(self.sleep)-7, len(self.sleep)):
                allSleep.append(self.sleep[i][1])
            return allSleep
        else:
            idx = -1
            for i in range (len(self.sleep)):
                if id == (str(self.sleep[i][0]))[:8]:
                    # print((self.sleep[i][0])[:8])
                    idx = i
            
            if (idx == -1):
                return None
            else:
                for i in range(idx-7, idx):
                    allSleep.append(self.sleep[i][1])
                return allSleep
    
    def add_Sleep(self, sleepAdd):
        self.sleep.append(sleepAdd)
        print(sleepAdd)
        
        with open(self.filename, 'w', newline='') as file:
            csv.writer(file).writerows([['Id(HHBBTTTTJJMM)','jamTidurStart','menitTidurStart','jamTidurEnd','menitTidurEnd','durasi(menit)']] + self.sleep)
        
    



    