import csv

class Sleep:
    def __init__(self):
        self.filename = './Sleep.csv'
        with open(self.filename, 'r') as file:
            csvreader = csv.reader(file)
            self.sleep = []
            next(csvreader)
            try:
                for i, baris in enumerate(csvreader):
                    id, jamTidur, menitTidur, durasi = map(int, baris)
                    id = str(id)
                    self.sleep.append([id, jamTidur, menitTidur, durasi])
            except:
                pass

    def get_sleep_id(self, index):
        return self.sleep[index][0]
                



    