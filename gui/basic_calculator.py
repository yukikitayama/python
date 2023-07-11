from tkinter import *
from tkinter import messagebox


def get_number(en):
    s = en.get()
    try:
        v = float(s)
    except ValueError:
        return None
    return v


def doeval():
    v1 = get_number(e1)
    if v1 is None:
        messagebox.showerror("Error", "Invalid argument in the first field")
        e1.focus_set()
        return
    v2 = get_number(e2)
    if v2 is None:
        messagebox.showerror("Error", "Invalid argument in the second field")
        e2.focus_set()
        return
    o = op.get()
    if o == 3 and v2 == 0:
        messagebox.showerror("Error", "Cannot divide by zero")
        e2.focus_set()
        return
    if o == 0:
        r = v1 + v2
    elif o == 1:
        r = v1 - v2
    elif o == 2:
        r = v1 * v2
    else:
        r = v1 / v2
    messagebox.showinfo("Result", str(r))

wnd = Tk()
wnd.title("Calculator")
e1 = Entry(wnd)
op = IntVar()
opa = Radiobutton(wnd, text="+", var=op, val=0)
ops = Radiobutton(wnd, text="-", var=op, val=1)
opm = Radiobutton(wnd, text="*", var=op, val=2)
opd = Radiobutton(wnd, text="/", var=op, val=3)
e2 = Entry(wnd)
bt = Button(wnd, text="Evaluate", command=doeval)
e1.grid(row=0, rowspan=4, column=0)
e1.focus_set()
opa.grid(row=0, column=1)
ops.grid(row=1, column=1)
opm.grid(row=2, column=1)
opd.grid(row=3, column=1)
e2.grid(row=0, rowspan=4, column=2)
bt.grid(row=4, columnspan=3)
wnd.mainloop()
