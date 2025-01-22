import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password

def generate_password_gui():
    def generate():
        try:
            length = int(length_entry.get())
            if length <= 0:
                messagebox.showerror("Error", "The length must be a positive integer.")
                return
            password = generate_password(length)
            password_var.set(password)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")
            
    root = tk.Tk()
    root.title("Password Generator")

    length_label = tk.Label(root, text="Desired Password Length:")
    length_label.pack(pady=10)

    length_entry = tk.Entry(root, width=30)
    length_entry.pack()

    generate_button = tk.Button(root, text="Generate Password", command=generate)
    generate_button.pack(pady=10)

    password_var = tk.StringVar()
    password_label = tk.Label(root, text="Generated Password:")
    password_label.pack()

    password_entry = tk.Entry(root, textvariable=password_var, width=50, state='readonly')
    password_entry.pack()

    root.mainloop()

def main():
    generate_password_gui()

if __name__ == "__main__":
    main()
