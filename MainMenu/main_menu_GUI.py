import MainMenu.mainmenu as uw 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout,QSizePolicy
import sys
from PyQt5 import QtWidgets
from datetime import date, datetime

class Main_Menu_GUI(QWidget, uw.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    
# app = QtWidgets.QApplication(sys.argv)

# window = Main_Menu_GUI()
# window.show()

# sys.exit(app.exec_())