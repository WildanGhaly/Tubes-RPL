from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindows(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1371, 721))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap('background.jpg'))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1361, 721))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("showinfo.png"))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 260, 341, 71))
        self.pushButton.setStyleSheet("background: transparent;")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.moodVisualization)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 350, 301, 71))
        self.pushButton_2.setStyleSheet("background: transparent;")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.moodPrediction)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(820, 260, 341, 71))
        self.pushButton_3.setStyleSheet("background: transparent;")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.sleepVisualization)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(780, 350, 411, 71))
        self.pushButton_4.setStyleSheet("background: transparent;")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.sleepRecommendation)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(570, 570, 221, 81))
        self.pushButton_5.setStyleSheet("background: transparent;")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.journalList)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    # Cek button
    def moodVisualization(self):
        print("Mood Visualization bisa")
    def moodPrediction(self):
        print("Mood Prediction bisa")
    def journalList(self):
        print("Journal List bisa")
    def sleepVisualization(self):
        print("Sleep Visualization bisa")
    def sleepRecommendation(self):
        print("Sleep Recommendation bisa")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindows()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
