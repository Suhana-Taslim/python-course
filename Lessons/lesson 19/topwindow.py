from tkinter import *

root = Tk()
root.geometry("400*300")
root.title("main")

def topwin():
    top = Toplevel()
    top.geometry("180*100")
    top.title("toplevel")
    l2 = Label(top, text = "This is toplevel window")
    l2.pack()

    top.mainloop()

l = Label(root, text = "this is root window")