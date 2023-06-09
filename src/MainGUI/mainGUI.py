import tkinter as tk
from PIL import ImageTk, Image
import os
import shutil
from pathlib import Path
import customtkinter as ctk

global backgroundImg

class mainGUI:
    
    def __init__(self, root):
        self.root = root
        self.root.title('')
        self.root.geometry('1920x1080')
        self.root.resizable(False, False)
        canvas = tk.Canvas(self.root, width=1920, height=1080, highlightthickness=0)
        canvas.pack(fill="both",expand=True)
        global backgroundImg
        backgroundImg = tk.PhotoImage(file= "D:\JASON\KULIAH ITB\MATKUL\SEMESTER 4\Rekayasa Perangkat Lunak\TUGAS BESAR APLIKASI\Tubes-RPL\MainGUI\Stock\\bg2.png")
        
        canvas.create_image(0,0, image=backgroundImg, anchor='nw')
        button_folder = tk.Button(self.root, 
            text = "Change Background", 
            command=self.setBackground,
            font=("Helvetica", 24)
            )
        button_folder.place(x = 36, y = 200)
        self.updateState(canvas)
        
    def setBackground(self): 
        get_var_image = tk.StringVar()
        image_path = tk.filedialog.askopenfilename(initialdir = "/", title = "Select image", filetype = (("png files", "*.png"), ("all files", "*.*")))
        get_var_image.set(image_path)
        print(image_path)
        print(get_var_image)
        img = Image.open(image_path)
        img = ImageTk.PhotoImage(img.resize((1920, 1080)))
        default = Path("MainGUI/Stock/default.png")
        if(not Path.exists(default)):
            os.rename("D:\JASON\KULIAH ITB\MATKUL\SEMESTER 4\Rekayasa Perangkat Lunak\TUGAS BESAR APLIKASI\Tubes-RPL\MainGUI\Stock\\bg2.png","MainGUI/Stock/default.png")
        else:
            os.remove("D:\JASON\KULIAH ITB\MATKUL\SEMESTER 4\Rekayasa Perangkat Lunak\TUGAS BESAR APLIKASI\Tubes-RPL\MainGUI\Stock\\bg2.png")
        shutil.copy2(image_path, "MainGUI/Stock/")
        os.rename("MainGUI/Stock/"+Path(image_path).name, "D:\JASON\KULIAH ITB\MATKUL\SEMESTER 4\Rekayasa Perangkat Lunak\TUGAS BESAR APLIKASI\Tubes-RPL\MainGUI\Stock\\bg2.png")
        self.root.after(1000, self.__init__)
        
    def updateState(self, canvas):
        backgroundImg = tk.PhotoImage(file= "D:\JASON\KULIAH ITB\MATKUL\SEMESTER 4\Rekayasa Perangkat Lunak\TUGAS BESAR APLIKASI\Tubes-RPL\MainGUI\Stock\\bg2.png")
        canvas.create_image(0,0, image=backgroundImg, anchor='nw')
        self.root.after(1000, self.updateState)
        
root = ctk.CTk()
app = mainGUI(root)
root.mainloop()