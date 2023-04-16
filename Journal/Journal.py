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
    def __init__(self, journalElems : list[str]):   # input as csv
        self.ID = journalElems[0]
        self.content = journalElems[1]
        self.title = journalElems[2]
    # def __init__(self, journalObject):   # ctor
    #     self.ID = journalObject.getID()
    #     self.content = journalObject.content
    #     self.title = journalObject.title
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
    def setID(self, ID=datetime.datetime.now()):
        ret = "%02d%02d%04d%02d%02d" % (
            ID.day,
            ID.month,
            ID.year,
            ID.hour,
            ID.minute
        )
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
        ret = Journal(["000000000000", content, title])
        ret.setID()
        return ret
    def toCSV(self):
        return [self.ID, self.content, self.title]


# tempJournals = Journals()
# tempJournals.showJournals()
# tempJournals.addJournal(Journal.makeJournal().toCSV())