import tkinter as tk
from tkinter import messagebox


def error():
    ans = messagebox.showerror("Error", "Problem!")
    print(ans)


window = tk.Tk()

button = tk.Button(window, text="Cause problem", command=error)
button.pack()

window.mainloop()
