import tkinter as tk
from tkinter import *
from datetime import date
from datetime import datetime
import mood_service as ms

class MoodApp(ms.Mood_Service):
    # List untuk data
    data_list = []

    def __init__(self, master):
        super().__init__()
        
        # Setup background
        self.master = master
        self.master.title('Input Mood')
        self.master.geometry('1920x1920')
        self.master.config(bg='orange')

        # Membuat labels
        self.label1 = tk.Label(text='INPUT MOOD',font=('Helvetica', 45),bg='orange')
        self.label1.place(x=570,y=60)

        self.labelJoy = tk.Label(text='Joy (rasa bahagia)',font=('Helvetica', 12),bg='orange')
        self.labelJoy.place(x=100,y=190)

        self.labelSadness = tk.Label(text='Sadness (rasa sedih)',font=('Helvetica', 12),bg='orange')
        self.labelSadness.place(x=100,y=315)

        self.labelAnger = tk.Label(text='Anger (rasa marah)',font=('Helvetica', 12),bg='orange')
        self.labelAnger.place(x=100,y=440)

        self.labelFear = tk.Label(text='Fear (rasa takut)',font=('Helvetica', 12),bg='orange')
        self.labelFear.place(x=100,y=565)

        self.labelDisgust = tk.Label(text='Disgust (rasa jijik)',font=('Helvetica', 12),bg='orange')
        self.labelDisgust.place(x=830,y=190)

        self.labelSurprise = tk.Label(text='Surprise (rasa terkejut)',font=('Helvetica', 12),bg='orange')
        self.labelSurprise.place(x=830,y=315)

        self.labelTrust = tk.Label(text='Trust (rasa percaya)',font=('Helvetica', 12),bg='orange')
        self.labelTrust.place(x=830,y=440)

        self.labelAnticipation = tk.Label(text='Anticipation (rasa antisipasi)',font=('Helvetica', 12),bg='orange')
        self.labelAnticipation.place(x=830,y=565)

        # Membuar gambar scales
        self.scales = []
        for i in range(8):
            scale = Scale(from_=0, to=10, length=600, tickinterval=1, orient=HORIZONTAL)
            self.scales.append(scale)
        
        # Mengatur posisi scales
        self.scales[0].place(x=100,y=225)
        self.scales[1].place(x=100,y=350)
        self.scales[2].place(x=100,y=475)
        self.scales[3].place(x=100,y=600)
        self.scales[4].place(x=830,y=225)
        self.scales[5].place(x=830,y=350)
        self.scales[6].place(x=830,y=475)
        self.scales[7].place(x=830,y=600)

        # Membuat tombol untuk submit
        self.button = tk.Button(text='Submit',font=('Helvetica', 18),bg='#E9EBEE',activebackground='#BFC7CE',borderwidth=0,relief='solid',command=self.button_click, height=1, width=7)
        self.button.place(x=1332, y=700)
    
    # ketika tombol ditekan
    def button_click(self):
        # ambil data dari scales untuk dimasukkan ke csv
        now = datetime.now().strftime("%H%M%S")
        dateNow = date.today().strftime("%d%m%Y")
        hasilData = []
        hasilData.append(int(dateNow+now))
        for scale in self.scales:
            hasilData.append(scale.get())
        
        print(hasilData)
        self.add_mood(hasilData)
        

# Menjalankan program
if __name__ == '__main__':
    root = Tk()
    app = MoodApp(root)
    root.mainloop()