import tkinter as tk
from tkinter import messagebox

def add(a, b):
    answer = a + b
    result_label.config(text=f"{a} + {b} = {answer}")

def sub(a, b):
    answer = a - b
    result_label.config(text=f"{a} - {b} = {answer}")

def mul(a, b):
    answer = a * b
    result_label.config(text=f"{a} * {b} = {answer}")

def div(a, b):
    if b != 0:
        answer = a / b
        result_label.config(text=f"{a} / {b} = {answer}")
    else:
        messagebox.showerror("Error", "Division by zero is not allowed.")

def calculate():
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())
        if operation_var.get() == 1:
            add(a, b)
        elif operation_var.get() == 2:
            sub(a, b)
        elif operation_var.get() == 3:
            mul(a, b)
        elif operation_var.get() == 4:
            div(a, b)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

def on_exit():
    root.destroy()

root = tk.Tk()
root.title("Simple Calculator")

operation_var = tk.IntVar()

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

tk.Label(frame, text="Select Operation:").grid(row=0, column=0, columnspan=2)

tk.Radiobutton(frame, text="Addition", variable=operation_var, value=1).grid(row=1, column=0)
tk.Radiobutton(frame, text="Subtraction", variable=operation_var, value=2).grid(row=1, column=1)
tk.Radiobutton(frame, text="Multiplication", variable=operation_var, value=3).grid(row=2, column=0)
tk.Radiobutton(frame, text="Division", variable=operation_var, value=4).grid(row=2, column=1)

tk.Label(frame, text="First Number:").grid(row=3, column=0)
entry_a = tk.Entry(frame)
entry_a.grid(row=3, column=1)

tk.Label(frame, text="Second Number:").grid(row=4, column=0)
entry_b = tk.Entry(frame)
entry_b.grid(row=4, column=1)

result_label = tk.Label(frame, text="")
result_label.grid(row=5, column=0, columnspan=2)

calculate_button = tk.Button(frame, text="Calculate", command=calculate)
calculate_button.grid(row=6, column=0, columnspan=2, pady=10)

exit_button = tk.Button(frame, text="Exit", command=on_exit)
exit_button.grid(row=7, column=0, columnspan=2)

root.mainloop()
