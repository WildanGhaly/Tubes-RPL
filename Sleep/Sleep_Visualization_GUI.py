import csv
import tkinter as tk
import Sleep_Service as SS
from tkinter import messagebox

class SVisualization(SS.Sleep_Service):
    
    def __init__(self, root):
        super().__init__()
        self.root = root
        self.root.geometry("600x400")
        self.root.title("Visualization")

        self.sleep_label = tk.Label(self.root, text="Sleep Visualization", font=('Arial', 18))
        self.sleep_label.place(relx=0.5, rely=0.1, anchor="center")

root = tk.Tk()
app = SVisualization(root)
root.mainloop()