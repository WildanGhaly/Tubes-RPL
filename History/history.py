from PyQt5 import QtCore, QtGui, QtWidgets
import MainMenu.mainmenu as mainmenu



class Ui_MainWindows(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 720)
        self.centralwidget_history = QtWidgets.QWidget(MainWindow)
        self.centralwidget_history.setObjectName("centralwidget")
        self.label_history = QtWidgets.QLabel(self.centralwidget_history)
        self.label_history.setGeometry(QtCore.QRect(0, 0, 1371, 721))
        self.label_history.setText("")
        self.label_history.setPixmap(QtGui.QPixmap(f"{mainmenu.image_path}"))
        self.label_history.setObjectName("label")
        self.label_history_2 = QtWidgets.QLabel(self.centralwidget_history)
        self.label_history_2.setGeometry(QtCore.QRect(0, 0, 1361, 721))
        self.label_history_2.setText("")
        self.label_history_2.setPixmap(QtGui.QPixmap("history/showinfo.png"))
        self.label_history_2.setObjectName("label_2")
        self.pushButton_history = QtWidgets.QPushButton(self.centralwidget_history)
        self.pushButton_history.setGeometry(QtCore.QRect(210, 260, 341, 71))
        self.pushButton_history.setStyleSheet("background: transparent;")
        self.pushButton_history.setText("")
        self.pushButton_history.setObjectName("pushButton")
        self.pushButton_history.clicked.connect(self.moodVisualization)
        self.pushButton_history_2 = QtWidgets.QPushButton(self.centralwidget_history)
        self.pushButton_history_2.setGeometry(QtCore.QRect(230, 350, 301, 71))
        self.pushButton_history_2.setStyleSheet("background: transparent;")
        self.pushButton_history_2.setText("")
        self.pushButton_history_2.setObjectName("pushButton_2")
        self.pushButton_history_2.clicked.connect(self.moodPrediction)
        self.pushButton_history_3 = QtWidgets.QPushButton(self.centralwidget_history)
        self.pushButton_history_3.setGeometry(QtCore.QRect(820, 260, 341, 71))
        self.pushButton_history_3.setStyleSheet("background: transparent;")
        self.pushButton_history_3.setText("")
        self.pushButton_history_3.setObjectName("pushButton_3")
        self.pushButton_history_3.clicked.connect(self.sleepVisualization)
        self.pushButton_history_4 = QtWidgets.QPushButton(self.centralwidget_history)
        self.pushButton_history_4.setGeometry(QtCore.QRect(780, 350, 411, 71))
        self.pushButton_history_4.setStyleSheet("background: transparent;")
        self.pushButton_history_4.setText("")
        self.pushButton_history_4.setObjectName("pushButton_4")
        self.pushButton_history_4.clicked.connect(self.sleepRecommendation)
        self.pushButton_history_5 = QtWidgets.QPushButton(self.centralwidget_history)
        self.pushButton_history_5.setGeometry(QtCore.QRect(570, 570, 221, 81))
        self.pushButton_history_5.setStyleSheet("background: transparent;")
        self.pushButton_history_5.setText("")
        self.pushButton_history_5.setObjectName("pushButton_5")
        self.pushButton_history_5.clicked.connect(self.journalList)
        # MainWindow.setCentralWidget(self.centralwidget_history)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    # Cek button
    def moodVisualization(self):
        from Mood.mood_pyqt_visual import Mood_Visual
        print("Mood Visualization bisa")
        self.mood_visual = Mood_Visual()
        self.mood_visual.show()
        self.hide()
    def moodPrediction(self):
        from Mood.mood_pyqt_prediction import Mood_Prediction
        print("Mood Prediction bisa")
        self.mood_prediction = Mood_Prediction()
        self.mood_prediction.show()
        self.hide()
    def journalList(self):
        from Journal.JournalList_Call import Journal_GUI_Call as JournalList
        self.JournalListWindow = JournalList()
        self.JournalListWindow.show()
        print("Journal List bisa")
        self.hide()
    def sleepVisualization(self):
        from Sleep.Sleep_Visualization_GUI import Ui_Widget as Visualization
        print("Sleep Visualization bisa")
        self.visualization_window = Visualization()
        self.visualization_window.show()
        self.hide()
    def sleepRecommendation(self):
        from Sleep.Sleep_Recommendation import Ui_Widget as Recommendation
        print("Sleep Recommendation bisa")
        self.recommendation_window = Recommendation()
        self.recommendation_window.show()
        self.hide()



# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindows()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
