import tkinter
from tkinter import messagebox


def clicked():
    messagebox.showinfo("info", "Some\ninfo")


window = tkinter.Tk()

button1 = tkinter.Button(window, text="Show info", command=clicked)
button1.pack()

button2 = tkinter.Button(window, text="Quit", command=window.destroy)
button2.pack()

window.mainloop()

