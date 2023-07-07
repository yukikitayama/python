import tkinter as tk


def click(*args):
    global size, grows
    if grows:
        size += 50
        if size >= 500:
            grows = False
    else:
        size -= 50
        if size <= 100:
            grows = True
    window.geometry(f"{size}x{size}")


size = 100
grows = True

window = tk.Tk()
window.geometry(f"{size}x{size}")
window.bind("<Button-1>", click)

window.mainloop()
