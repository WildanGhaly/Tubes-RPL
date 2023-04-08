from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as py
from PySide6.QtWidgets import QSizePolicy

import random

class PlotCanvas(FigureCanvas):
    def __init__(self, parent = None, width=4, height=4, dpi=100):
        fig = Figure(figsize=(width,height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        
        FigureCanvas.__init__(self,fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        FigureCanvas.resize(self,450,460)
        self.plot()
        
    def plot(self):
        data = [random.random() for i in range (25)]
        ax = self.figure.add_subplot(111)
        ax.plot(data,'r-')
        self.draw()