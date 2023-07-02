import tkinter as tk

window = tk.Tk()

b1 = tk.Button(window, text="Button 1")
b1.pack()
b1["anchor"] = "e"
b1["width"] = 40

b2 = tk.Button(window, text="Button 2")
b2.pack()
b2["anchor"] = "sw"
b2["width"] = 40
b2["height"] = 3

window.mainloop()
