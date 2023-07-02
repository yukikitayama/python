import tkinter as tk

window = tk.Tk()

b1 = tk.Button(window, text="Button 1")
b1.pack()

b2 = tk.Button(window, text="Button 2")
b2.pack()
b2["borderwidth"] = 10
b2["highlightthickness"] = 20
b2["padx"] = 10
b2["pady"] = 20
b2["underline"] = 2

window.mainloop()
