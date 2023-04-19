import datetime

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
        ret = datetime.datetime(int(tahun),int(bulan),int(hari))
        return ret
    def DatetimeToID(ID=datetime.datetime.now()):
        ret = "%04d%02d%02d" % (
            ID.year,
            ID.month,
            ID.day
            # ID.hour,
            # ID.minute
        )
        return ret
    def setID(self, ID=DatetimeToID()):
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
        ret = Journal([Journal.DatetimeToID(), content, title])
        return ret
    def toCSV(self):
        return [self.ID, self.content.replace('\n','\\n').replace('\t','\\t'), self.title]