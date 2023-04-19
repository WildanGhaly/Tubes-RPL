import Journal.Journal_rc
import Journal.JournalInput_GUI as uw 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout,QSizePolicy
import sys
from PyQt5 import QtWidgets
from datetime import date, datetime
import Journal.JournalDatabase as JournalDatabase
from tkinter import messagebox
from Journal.Journal import Journal as jrn
class Journal_GUI_Call(QWidget, uw.JournalInput):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        DB = JournalDatabase.JournalDatabase()
        self.SubmitButton.clicked.connect(self.addToJournalDB)
    def addToJournalDB(self):
        if self.JournalContent.toPlainText().strip()=="":
        # do nothing
                messagebox.showinfo("Failed", "Konten Jurnal kosong.")
        else : 
                addedContent = jrn([jrn.DatetimeToID(),self.JournalContent.toPlainText(),"Title"+jrn.DatetimeToID()])
                self.DB.addJournal(addedContent.toCSV())
                messagebox.showinfo("Success", "Konten Jurnal ditambahkan.")
                from MainMenu.main_menu_GUI import Main_Menu_GUI
                self.main_menu = Main_Menu_GUI()
                self.main_menu.show()
                self.hide()
# app = QtWidgets.QApplication(sys.argv)

# window = Journal_GUI_Call()
# window.show()

# sys.exit(app.exec_())