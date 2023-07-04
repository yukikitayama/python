import tkinter as tk


def blink():
    global is_white

    if is_white:
        color = "black"
    else:
        color = "white"

    is_white = not is_white

    frame.config(bg=color)
    # Need this again to make it continuously blink
    frame.after(500, blink)


is_white = True

window = tk.Tk()

frame = tk.Frame(window, width=200, height=100, bg="white")
# Invoke blink for the first time
frame.after(500, blink)
frame.pack()

window.mainloop()
