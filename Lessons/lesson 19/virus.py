from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("200*200")

def msg():
    messagebox.showwarning("Alert", "Stop! Virus found")

    button = Button(x=40, y=80)

root.mainloop()