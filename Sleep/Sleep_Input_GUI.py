import csv
import tkinter as tk
import Sleep_Service as SS
from tkinter import messagebox

class FormSleep(SS.Sleep_Service):
    
    def __init__(self, root):
        super().__init__()
        self.root = root
        self.root.geometry("600x400")
        self.root.title("Input Data Tidur")

        self.sleep_label = tk.Label(self.root, text="Time Sleep", font=('Arial', 18))
        self.sleep_label.place(relx=0.5, rely=0.1, anchor="center")

        self.jam_start_label = tk.Label(self.root, text="Start Time:")
        self.jam_start_label.place(relx=0.4, rely=0.4, anchor="center")

        self.jam_start_entry = tk.Entry(self.root, width=5)
        self.jam_start_entry.place(relx=0.51, rely=0.4, anchor="center")

        self.menit_start_entry = tk.Entry(self.root, width=5)
        self.menit_start_entry.place(relx=0.6, rely=0.4, anchor="center")

        self.jam_selesai_label = tk.Label(self.root, text="End Time:")
        self.jam_selesai_label.place(relx=0.4, rely=0.5, anchor="center")

        self.jam_selesai_entry = tk.Entry(self.root, width=5)
        self.jam_selesai_entry.place(relx=0.51, rely=0.5, anchor="center")

        self.menit_selesai_entry = tk.Entry(self.root, width=5)
        self.menit_selesai_entry.place(relx=0.6, rely=0.5, anchor="center")

        self.simpan_button = tk.Button(self.root, text="Submit", command=self.submit_button)
        self.simpan_button.place(relx=0.94, rely=0.94, anchor="se")

    def submit_button(self):
        jam_start = self.jam_start_entry.get()
        menit_start = self.menit_start_entry.get()
        jam_selesai = self.jam_selesai_entry.get()
        menit_selesai = self.menit_selesai_entry.get()

        if(self.validate_sleep(jam_start, menit_start, jam_selesai, menit_selesai)):
            self.create_sleep(jam_start, menit_start, jam_selesai, menit_selesai)
            messagebox.showinfo("Success", "Data Tidur Berhasil Disimpan")
        else:
            messagebox.showerror("Error", "Data Tidur Gagal Disimpan")




root = tk.Tk()
app = FormSleep(root)
root.mainloop()
