import tkinter as tk


window = tk.Tk()

label = tk.Label(window, text="Little label:")
label.pack()

frame = tk.Frame(
    window,
    height=30,
    width=100,
    bg="#000099"
)
frame.pack()

button = tk.Button(window, text="Button")
button.pack(fill=tk.X)

switch = tk.IntVar()
switch.set(1)

checkbutton = tk

window.mainloop()
