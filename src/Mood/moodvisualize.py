import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import csv
import pandas as pd

class MatplotlibGui:
    def __init__(self, master):
        self.master = master
        self.master.title('Visualize Mood')
        self.master.geometry('1920x1080')

        # create a Matplotlib figure and axes
        self.figure, self.ax = plt.subplots()

        # read csv file
        df = pd.read_csv('mood.csv')
        x = range(1, len(df.index) + 1)
        self.ax.plot(x,df['Sadness'], color='red', label='Joy')

        # create a FigureCanvasTkAgg widget and add it to the window
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.master)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()

if __name__ == '__main__':
    root = tk.Tk()
    app = MatplotlibGui(root)
    root.mainloop()
