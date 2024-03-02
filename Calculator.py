import tkinter.messagebox
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Калькулятор")

btn_style = ttk.Style().configure('My.TButton', font=('Copperplate Gothic Light', 16), width=4, height=2,
                                  background='indigo', foreground='fuchsia')

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, END)
        entry.insert(END, str(result))
    except ZeroDivisionError:
        tkinter.messagebox.showerror('Ха-ха-ха', 'Навіть першокласники знають, що на нуль ділити не можна')
    except NameError or SyntaxError:
        tkinter.messagebox.showerror('Гей!', 'Можна вводити тільки те, що відображенно в інтерфейсі')


def clear():
    entry.delete(0, END)


def display(value):
    entry.insert(END, value)


def exit():
    root.quit()


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

entry = ttk.Entry(root, width=40, justify='right', background='indigo')
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('.', 4, 0), ('0', 4, 1), ('+', 4, 3)
]

for (text, row, col) in buttons:
    btn = ttk.Button(root, text=text, style='My.TButton', command=lambda value=text: display(value))
    btn.grid(row=row, column=col)

result_btn = ttk.Button(root, text='=', style='My.TButton', command=calculate)
result_btn.grid(row=4, column=2)

clear_btn = ttk.Button(root, text='C', style='My.TButton', width=9, command=clear)
clear_btn.grid(row=5, column=0, columnspan=2)

end_btn = ttk.Button(root, text='Exit', style='My.TButton', width=9, command=exit)
end_btn.grid(row=5, column=2, columnspan=2)

root.resizable(False, False)
root.mainloop()
