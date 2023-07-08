import tkinter as tk
from tkinter import messagebox


def question():
    ans = messagebox.askokcancel("Coffee", "Can I make you one more coffee?")
    print(ans)


window = tk.Tk()

button = tk.Button(window, text="Coffee", command=question)
button.pack()

window.mainloop()
