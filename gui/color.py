import tkinter as tk


window = tk.Tk()

button = tk.Button(
    window,
    text="Button #1",
    bg="red",
    fg="yellow"
)
button.pack()

b2 = tk.Button(window, text="Button 2")
b2.pack()
b2.config(bg="#000000")
b2.config(fg="yellow")
b2.config(activeforeground="#FF0000")
b2.config(activebackground="green")

window.mainloop()
