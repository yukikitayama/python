import tkinter as tk


window = tk.Tk()

button = tk.Button(
    window,
    text="Button #1",
    bg="red",
    fg="yellow"
)
button.pack()

window.mainloop()
