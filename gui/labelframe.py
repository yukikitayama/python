import tkinter as tk


window = tk.Tk()

label_frame_1 = tk.LabelFrame(
    window,
    text="Frame 1",
    width=200,
    height=100,
    bg="white"
)
label_frame_1.pack()

label_frame_2 = tk.LabelFrame(
    window,
    text="Frame 2",
    labelanchor="se",
    width=200,
    height=100,
    bg="yellow"
)
label_frame_2.pack()

button_1_1 = tk.Button(label_frame_1, text="B1 in F1")
button_1_1.place(x=10, y=10)
button_1_2 = tk.Button(label_frame_1, text="B2 in F1")
button_1_2.place(x=10, y=50)
button_2_1 = tk.Button(label_frame_2, text="B1 in F2")
button_2_1.grid(column=0, row=0)
button_2_2 = tk.Button(label_frame_2, text="B2 in F2")
button_2_2.grid(column=1, row=1)

window.mainloop()
