from MainMenu.main_menu_GUI import Main_Menu_GUI as uw
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout,QSizePolicy
import sys
from PyQt5 import QtWidgets
from datetime import date, datetime


app = QtWidgets.QApplication(sys.argv)

window = uw()
window.show()

sys.exit(app.exec_())