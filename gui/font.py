import tkinter as tk

window = tk.Tk()

l1 = tk.Label(window, text="Label 1")
l1.grid(column=0, row=0)

l2 = tk.Label(window, text="Label 2", font=("Times", "12"))
l2.grid(column=0, row=1)

l3 = tk.Label(window, text="Label 3", font=("Arial", "24", "bold"))
l3.grid(column=0, row=2)

window.mainloop()
