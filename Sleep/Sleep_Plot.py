from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
from PyQt5.QtWidgets import QSizePolicy

import random

class PlotCanvas(FigureCanvas):
    def __init__(self, parent, width, height, dpi, otherData, filename):
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
        self.plot(otherData, filename)
        
    def plot(self, otherData, filename):
        data = []
        for i in range (len(otherData)):
            data.append(int(otherData[i]))
        ypoints = np.array(data)
        print(data)
        xpoints = np.array([1,2,3,4,5,6,7])
        plt.figure().set_figheight(3.125)
        plt.figure().set_figwidth(3.4375)
        plt.plot(xpoints, ypoints)
        savefile='./Sleep/vis_result/'+filename+'.png'
        plt.savefig(savefile)
        
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
        xpoints = np.array(data)
        ypoints = np.array([0, len(data)-1])
        plt.plot(xpoints, ypoints)
        plt.figure().set_figheight(3.2291666667)
        plt.figure().set_figwidth(5.2916666667)
        plt.savefig('./Sleep/vis_result/sleep_visual_recom.png')