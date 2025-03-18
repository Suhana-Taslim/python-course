from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("500x700")

def msg():
    messagebox.showwarning("Alert", "Stop! Virus found")

    button = Button(x=40, y=80)

root.mainloop()