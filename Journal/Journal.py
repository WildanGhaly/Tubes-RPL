import csv
import datetime
class Journals:
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
class Journal:
    def __init__(self, journalElems : list[str]):   # input as csv (headers: ID, content, title)
        self.ID = journalElems[0]
        self.content = journalElems[1]
        self.title = journalElems[2]
    def __str__(self):
        return (' '.join([self.ID, self.content, self.title]))
    def getID(self):
        return self.ID
    def getContent(self):
        return self.content
    def getTitle(self):
        return self.title
    def IDtoDatetime(self):
        dtstr12char = self.ID
        hari = dtstr12char[0]+dtstr12char[1]
        bulan = dtstr12char[2]+dtstr12char[3]
        tahun = dtstr12char[4]+dtstr12char[5]+dtstr12char[6]+dtstr12char[7]
        jam = dtstr12char[8]+dtstr12char[9]
        menit = dtstr12char[10]+dtstr12char[11]
        ret = datetime.datetime(int(tahun),int(bulan),int(hari),int(jam),int(menit))
        return ret
    def markIDfromTime(self, ID=datetime.datetime.now()):
        ret = "%02d%02d%04d%02d%02d" % (
            ID.day,
            ID.month,
            ID.year,
            ID.hour,
            ID.minute
        )
        return ret
    def setID(self, ID=markIDfromTime()):
        ret = ID
        self.ID = ret
    def setContent(self, content="<EMPTY>"):
        ret = content
        self.content = ret
    def setTitle(self,title="<NOTITLE>"):
        ret = title
        self.title = ret
    # Journal constructor from keyboard input
    # @returns Journal object
    def makeJournal():
        title = input()
        content = input()
        ret = Journal([Journal.markIDfromTime(), content, title])
        return ret
    def toCSV(self):
        return [self.ID, self.content, self.title]

# Example 
# ctor journals: membaca journal, dengan letak file yang sudah ditentukan
# awal penggunaan journals, csv-nya akan kosong (hanya ada header)
# tempJournals = Journals()

# tempJournals.showJournals()

# menambahkan 1 objek journal yang sudah disusun menyesuaikan format csv
# makejournal() adalah fungsi menerima input journal dengan input keyboard via CLI
# tempJournals.addJournal(Journal.makeJournal().toCSV())