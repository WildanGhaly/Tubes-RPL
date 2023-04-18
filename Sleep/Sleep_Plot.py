from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QSizePolicy

import random

class PlotCanvas(FigureCanvas):
    def __init__(self, parent, width, height, dpi, otherData: list):
        fig = Figure(figsize=(4,4), dpi=100)
        self.axes = fig.add_subplot(111)
        parent=None
        FigureCanvas.__init__(self,fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        FigureCanvas.resize(self,330,300)
        self.plot(otherData)
        
    def plot(self, otherData):
        data = []
        for i in range (len(otherData)):
            data.append(int(otherData[i]))
        print(data)
        ax = self.figure.add_subplot(111)
        ax.plot(data,'r-')
        self.draw()
        
class PlotCanvasRec(FigureCanvas):
    def __init__(self, parent, width, height, dpi, otherData):
        fig = Figure(figsize=(4,4), dpi=100)
        self.axes = fig.add_subplot(111)
        parent=None
        FigureCanvas.__init__(self,fig)
        self.setParent(parent)
        FigureCanvas.resize(self,508,310)
        self.plot(otherData)
        
    def plot(self, otherData):
        data = []
        for i in range (len(otherData)):
            data.append(int(otherData[i]))
        print(data)
        ax = self.figure.add_subplot(111)
        ax.plot(data,'r-')
        self.draw()