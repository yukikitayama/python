import tkinter as tk
from tkinter import messagebox


def question():
    ans = messagebox.askyesno("!", "Eat breakfast")
    print(ans)


window = tk.Tk()

button = tk.Button(window, text="Ask", command=question)
button.pack()

window.mainloop()
