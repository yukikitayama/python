import tkinter as tk


def to_string(x):
    return f"Couter: {str(x)}"


def plus():
    global counter
    counter += 1
    text.set(to_string(counter))


window = tk.Tk()

counter = 0

text = tk.StringVar()

button = tk.Button(window, text="Go on!", command=plus)
button.pack()

label = tk.Label(window, textvariable=text, height=4)
text.set(to_string(counter))
label.pack()

window.mainloop()
