from tkinter import *
from tkinter import ttk
from tkinter import filedialog
parent = Tk()

parent.title("Tensor Flow Models")
frame = ttk.Frame(parent, borderwidth=5)

def filesearch():
    parent.filename = filedialog.askopenfilename(initialdir="/", title="Select file", filetype(("all files", "*.*"))
    

Unlabeled_Button = ttk.Button(parent, text="Unlabled Data", command=lambda: filesearch())
Labeled_Button = ttk.Button(parent, text"Labeled Data", command=lambda: filesearch())

Unlabeled_Button.place(x=10, y=15)
Labeled_Button.place(x=80, y=15)

parent.geometry("400x400")

parent.mainloop()
