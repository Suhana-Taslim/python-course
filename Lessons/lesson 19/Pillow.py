from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('image')
root.geometry('500x500')

upload = Image.open("img.jpg")

image = ImageTk.PhotoImage(upload)

label = Label(root, image=image, height=300, width=300)
label.place(x=50, y=0)
label2 = Label(root, text="This is how you add image in Tkinter Window")
label2.place(x=40, y=360)

root.mainloop()