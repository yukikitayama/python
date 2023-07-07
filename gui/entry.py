import tkinter as tk


def digits_only(*args):
    global last_string
    string = text.get()
    # Valid case
    if string == "" or string.isdigit():
        last_string = string
    else:
        text.set(last_string)


window = tk.Tk()

last_string = ""

text = tk.StringVar()
text.set(last_string)
text.trace("w", digits_only)

entry = tk.Entry(window, textvariable=text)
entry.pack()
entry.focus_set()

window.mainloop()
