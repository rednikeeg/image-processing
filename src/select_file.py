import tkinter as tk
from tkinter import filedialog

name =""

def openFile():
    root = tk.Tk()
    root.withdraw()
    name = filedialog.askopenfilename()
    return name
