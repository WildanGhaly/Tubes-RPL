import csv
class JournalDatabase:
    DATABASE_HEADER = ["Id(HHBBTTTTJJMM)","IsiJournal","JudulJournal"]
    def __init__(self):
        self.filename = './Journal/Journal.csv'
        with open(self.filename, 'r') as file:
            csvreader = csv.reader(file, lineterminator="\n")
            next(csvreader)  # Skip header row
            self.journals = [Journal(row) for row in csvreader]
    def showJournals(self):
        for i in self.journals:
            print(i)
    def addJournal(self, journal):
        with open(self.filename, 'a') as file:
            csvwriter = csv.writer(file, quoting=1, lineterminator="\n")
            csvwriter.writerow(journal)
    def clearJournal(self):
        with open(self.filename, 'w') as file:
            csvwriter = csv.writer(file, lineterminator="\n")
            csvwriter.writerow(self.DATABASE_HEADER)

# Example 
# ctor journals: membaca journal, dengan letak file yang sudah ditentukan
# awal penggunaan journals, csv-nya akan kosong (hanya ada header)
# tempJournals = Journals()

# tempJournals.showJournals()

# menambahkan 1 objek journal yang sudah disusun menyesuaikan format csv
# makejournal() adalah fungsi menerima input journal dengan input keyboard via CLI
# tempJournals.addJournal(Journal.makeJournal().toCSV())