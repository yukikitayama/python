import tkinter as tk


def on_off():
    global accessible
    if accessible == tk.DISABLED:
        accessible = tk.ACTIVE
    else:
        accessible = tk.DISABLED
    # 1 means the second item in the submenu
    sub_menu.entryconfig(1, state=accessible)


window = tk.Tk()

accessible = tk.DISABLED

menu = tk.Menu(window)
window.config(menu=menu)

sub_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Menu", menu=sub_menu)
sub_menu.add_command(label="On/Off", command=on_off)
sub_menu.add_command(label="Switch", state=tk.DISABLED)

window.mainloop()