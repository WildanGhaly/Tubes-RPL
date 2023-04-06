import tkinter as tk
import customtkinter as ctk
from PIL import ImageTk, Image
import os
import shutil
import glob
from pathlib import Path

global bgImg

mainGUI = tk.Tk()
mainGUI.geometry('1920x1080')
canvas = tk.Canvas(mainGUI, width=1920, height=1080, highlightthickness=0)
canvas.pack(fill="both",expand=True)

bgImg = tk.PhotoImage(file= "Stock/bg2.png")

canvas.create_image(0,0, image=bgImg , anchor='nw')
get_var_image = tk.StringVar()

def bgChange(): 
  image_path = tk.filedialog.askopenfilename(initialdir = "/", title = "Select image", filetype = (("png files", "*.png"), ("all files", "*.*")))
  get_var_image.set(image_path)
  print(image_path)
  print(get_var_image)
  img = Image.open(image_path)
  img = ImageTk.PhotoImage(img.resize((1920, 1080)))
  default = Path("Stock/default.png")
  if(not Path.exists(default)):
      os.rename("Stock/bg2.png","Stock/default.png")
  else:
      os.remove("Stock/bg2.png")
  shutil.copy2(image_path, "Stock/")
  os.rename("Stock/"+Path(image_path).name, "Stock/bg2.png")
  updateState()
  

def updateState():
    global bgImg
    bgImg = tk.PhotoImage(file= "Stock/bg2.png")
    canvas.create_image(0,0, image=bgImg, anchor='nw')
    mainGUI.after(1000,updateState)

button_folder = tk.Button(mainGUI, 
        text = "Change Background", 
        command=bgChange,
        font=("Helvetica", 24)
        )
button_folder.place(x = 36, y = 200)
updateState()
mainGUI.mainloop()