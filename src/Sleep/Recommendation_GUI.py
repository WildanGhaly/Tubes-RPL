import csv
import tkinter as tk
import Recommendation as R
from tkinter import messagebox


class Recommendation_GUI(R.Recommendation):
    
    def __init__(self, root, date):
        super().__init__(date)
        self.root = root
        self.root.geometry("600x400")
        self.root.title("Recommendation")

        self.sleep_label = tk.Label(self.root, text="Sleep Recommendation", font=('Arial', 18))
        self.sleep_label.place(relx=0.5, rely=0.1, anchor="center")
        



        # self.jam_start_label = tk.Label(self.root, text="Start Time:")
        # self.jam_start_label.place(relx=0.4, rely=0.4, anchor="center")

        # self.jam_start_entry = tk.Entry(self.root, width=5)
        # self.jam_start_entry.place(relx=0.51, rely=0.4, anchor="center")

        # self.menit_start_entry = tk.Entry(self.root, width=5)
        # self.menit_start_entry.place(relx=0.6, rely=0.4, anchor="center")

        # self.jam_selesai_label = tk.Label(self.root, text="End Time:")
        # self.jam_selesai_label.place(relx=0.4, rely=0.5, anchor="center")

        # self.jam_selesai_entry = tk.Entry(self.root, width=5)
        # self.jam_selesai_entry.place(relx=0.51, rely=0.5, anchor="center")

        # self.menit_selesai_entry = tk.Entry(self.root, width=5)
        # self.menit_selesai_entry.place(relx=0.6, rely=0.5, anchor="center")

        # self.simpan_button = tk.Button(self.root, text="Submit", command=self.submit_button)
        # self.simpan_button.place(relx=0.94, rely=0.94, anchor="se")


root = tk.Tk()
app = Recommendation_GUI(root, "042023")
root.mainloop()