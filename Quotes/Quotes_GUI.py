from PIL import ImageTk, Image
import Quotes_Service as QS
import tkinter as tk
from tkinter import messagebox

class FormQuote(QS.Quotes_Service):
    isDoingSomething = False
    
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.master.title("Quote Editor")
        self.master.geometry("600x400")
        self.master.resizable(False, False)

        # create a canvas and add background image
        self.canvas = tk.Canvas(self.master, width=600, height=400)
        self.canvas.pack(fill="both", expand=True)
        self.bg_image = Image.open("Home.jpg")
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.canvas.create_image(0, 0, anchor="nw", image=self.bg_photo)

        # add buttons for input and edit
        self.input_button = tk.Button(self.master, text="Input Quote", font=("Arial", 16),
                                    bg="light blue", command=self.input_quote_GUI)
        self.input_button.place(relx=0.5, rely=0.35, anchor="center")
        self.edit_button = tk.Button(self.master, text="Edit Quote", font=("Arial", 16),
                                    bg="light green", command=self.edit_quote_GUI)
        self.edit_button.place(relx=0.5, rely=0.5, anchor="center")
        self.input_paragraph = None
        

    def input_quote_GUI(self):
        if self.isDoingSomething:
            return
        self.isDoingSomething = True
        
        # create a new paragraph for input quote
        if self.input_paragraph is not None:
            self.input_paragraph.destroy()
        self.input_paragraph = tk.Frame(self.master, bg="white")
        self.input_paragraph.place(relx=0.5, rely=0.35, anchor="center")

        # add input box
        self.quote_input = tk.Entry(self.input_paragraph, width=40, font=("Arial", 12))
        self.quote_input.pack(side="top", pady=10)
        self.quote_input.insert(0, "Enter quote here")
        self.quote_input.bind("<FocusIn>", lambda args: self.quote_input.delete('0', 'end'))
        self.quote_input.bind("<FocusOut>", lambda args: self.quote_input.insert(0, "Enter quote here"))

        # add submit and cancel buttons
        self.button_paragraph = tk.Frame(self.master, bg="white")
        self.button_paragraph.place(relx=0.5, rely=0.5, anchor="center")
        self.submit_button = tk.Button(self.button_paragraph, text="Submit", font=("Arial", 12),
                                        bg="light blue", command=self.add_quote_submit)
        self.submit_button.pack(side="left", padx=10)
        self.cancel_button = tk.Button(self.button_paragraph, text="Cancel", font=("Arial", 12),
                                        bg="light blue", command=self.cancel_quote)
        self.cancel_button.pack(side="left", padx=10)


    def edit_quote_GUI(self):
        if self.isDoingSomething:
            return
        self.isDoingSomething = True
        
        # create a new paragraph for edit quote
        if self.input_paragraph is not None:
            self.input_paragraph.destroy()
        self.input_paragraph = tk.Frame(self.master, bg="white")
        self.input_paragraph.place(relx=0.5, rely=0.35, anchor="center")

        # add input box and id box
        self.quote_input = tk.Entry(self.input_paragraph, width=40, font=("Arial", 12))
        self.quote_input.pack(side="top", pady=10)
        self.quote_input.insert(0, "Enter new quote here")
        self.quote_input.bind("<FocusIn>", lambda args: self.quote_input.delete('0', 'end'))
        
        self.id_input = tk.Entry(self.input_paragraph, width=10, font=("Arial", 12))
        self.id_input.pack(side="top", pady=10)
        self.id_input.insert(0, "Enter ID here")
        self.id_input.bind("<FocusIn>", lambda args: self.id_input.delete('0', 'end'))


        # add submit and cancel buttons
        self.button_paragraph = tk.Frame(self.master, bg="white")
        self.button_paragraph.place(relx=0.5, rely=0.5, anchor="center")
        self.submit_button = tk.Button(self.button_paragraph, text="Submit", font=("Arial", 12),
                                        bg="light blue", command=self.edit_quote_submit)
        self.submit_button.pack(side="left", padx=10)
        self.cancel_button = tk.Button(self.button_paragraph, text="Cancel", font=("Arial", 12),
                                        bg="light blue", command=self.cancel_quote)
        self.cancel_button.pack(side="left", padx=10)


    def cancel_quote(self):
        if self.input_paragraph is not None:
            self.input_paragraph.destroy()
        if self.button_paragraph is not None:
            self.button_paragraph.destroy()
        self.isDoingSomething = False


    def add_quote_submit(self):
        # call add_quote function from backend and show success message if it returns true
        if self.add_quote(self.quote_input.get()):
            messagebox.showinfo("Success", "Quote has been added.")
            self.cancel_quote()
            self.isDoingSomething = False
            
    def edit_quote_submit(self):
        # call edit_quote function from backend and show success message if it returns true
        if self.edit_quote(self.id_input.get(), self.quote_input.get()):
            messagebox.showinfo("Success", "Quote has been edited.")
            self.cancel_quote()
            self.isDoingSomething = False

# Usage
root = tk.Tk()
app = FormQuote(root)
root.mainloop()
