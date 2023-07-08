# tkinter

## Observable variable

Works like a regular variable but also any change of the variable's state can be **observed** by external agents.

An object of the container class, explicitly created and initialized.

Observable variable is typed, so we have to know what type of value to be stored, cannot change during the variable's life.

Create after the main window initialization.

- `BooleanVar` with `False` initialization
- `DoubleVar` with `0.0`
- `IntVar` with `0`
- `StringVar` with `""`

```python
s = StringVar()

s.set("Something")

s.get()
```

## Widget

**Master widget** is typically the main window.

All widgets fall into 2 categories; clickable and non-clickable

`widget = Widget(master, option, ...)`

## Non-clickable widget

Don't have a `command` property

You can use `bind()` to simulate command behavior

## messagebox

`messagebox` module has the predefined functions to announce something or ask questions to users

- `askyesno()` has question mark
- `askokcancel()` has question mark
- `askretrycancel()` has a warning sign
- `askquestion()` has a question mark icon
- `showerror()` has a red warning icon, only OK button to respond, return `OK` string
- `showwarning()` a warning icon, only OK button, return `OK` string
