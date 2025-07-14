import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip  # For clipboard copy

# Password Generator Logic
def generate_password():
    try:
        length = int(entry_length.get())
        if length <= 0:
            messagebox.showerror("Invalid Input", "Password length must be a positive number.")
            return

        char_set = ""
        if var_letters.get():
            char_set += string.ascii_letters
        if var_numbers.get():
            char_set += string.digits
        if var_symbols.get():
            char_set += string.punctuation

        if not char_set:
            messagebox.showerror("Selection Error", "Please select at least one character set.")
            return

        password = "".join(random.choice(char_set) for _ in range(length))
        entry_result.delete(0, tk.END)
        entry_result.insert(0, password)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for password length.")

# Copy to Clipboard
def copy_to_clipboard():
    password = entry_result.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Empty", "No password to copy.")

# GUI Setup
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x350")
root.resizable(False, False)

# Widgets
tk.Label(root, text="Password Length:", font=("Arial", 10)).pack(pady=5)
entry_length = tk.Entry(root)
entry_length.pack()

var_letters = tk.BooleanVar(value=True)
var_numbers = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Letters (A-Z, a-z)", variable=var_letters).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Include Numbers (0-9)", variable=var_numbers).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Include Symbols (!, @, #, etc.)", variable=var_symbols).pack(anchor="w", padx=20)

tk.Button(root, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white").pack(pady=10)

entry_result = tk.Entry(root, width=35, font=("Arial", 12))
entry_result.pack(pady=5)

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg="#2196F3", fg="white").pack(pady=5)

tk.Label(root, text="Developed by Varun", font=("Arial", 8)).pack(side="bottom", pady=10)

# Run the GUI
root.mainloop()
