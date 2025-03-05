from tkinter import *

window = Tk()
window.title('Tkinter Sample Window')
window.geometry('500*500')

greeting = Label(text="Hello User", fg='black', bg='white')
button = Button(text="Click Me", bg='black', fg='white')
entry = Entry(fg="yellow", bg="green", width=50)

greeting.pack()
button.pack()
entry.pack()

frame = Frame(master=window, relief=RAISED, borderwidth=10)
frame.pack()
label = Label(master=frame, text='Simple Frame')
label.pack()

textbox = Text(fg='pink', bg='blue')
textbox.pack()