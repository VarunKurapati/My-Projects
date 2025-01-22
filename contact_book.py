import tkinter as tk
from tkinter import messagebox

contact = {}

def display_contact_gui():
    if not contact:
        result_text.set("Empty contact book")
    else:
        result = "Name\t\tPhone\t\tEmail\t\tAddress\n"
        for name, info in contact.items():
            result += f"{name}\t\t{info['phone']}\t\t{info['email']}\t\t{info['address']}\n"
        result_text.set(result)

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    
    if name == "" or phone == "" or email == "" or address == "":
        messagebox.showerror("Error", "Please fill in all fields.")
        return
    
    contact[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }
    display_contact_gui()

def search_contact():
    search_name = search_entry.get()
    
    if search_name in contact:
        info = contact[search_name]
        result_text.set(f"Phone: {info['phone']}\nEmail: {info['email']}\nAddress: {info['address']}")
    else:
        result_text.set("Contact not found.")

def edit_contact():
    edit_name = edit_entry.get()
    
    if edit_name in contact:
        phone = edit_phone_entry.get()
        email = edit_email_entry.get()
        address = edit_address_entry.get()
        
        contact[edit_name]["phone"] = phone
        contact[edit_name]["email"] = email
        contact[edit_name]["address"] = address
        
        display_contact_gui()
    else:
        result_text.set("Contact not found.")

def delete_contact():
    delete_name = delete_entry.get()
    
    if delete_name in contact:
        del contact[delete_name]
        display_contact_gui()
    else:
        result_text.set("Contact not found.")

root = tk.Tk()
root.title("Contact Book")

tk.Label(root, text="Name:").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Phone:").grid(row=1, column=0)
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1)

tk.Label(root, text="Email:").grid(row=2, column=0)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1)

tk.Label(root, text="Address:").grid(row=3, column=0)
address_entry = tk.Entry(root)
address_entry.grid(row=3, column=1)

add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.grid(row=4, column=0, columnspan=2, pady=10)

tk.Label(root, text="Search Name:").grid(row=5, column=0)
search_entry = tk.Entry(root)
search_entry.grid(row=5, column=1)

search_button = tk.Button(root, text="Search Contact", command=search_contact)
search_button.grid(row=6, column=0, columnspan=2, pady=10)

tk.Label(root, text="Edit Name:").grid(row=7, column=0)
edit_entry = tk.Entry(root)
edit_entry.grid(row=7, column=1)

tk.Label(root, text="New Phone:").grid(row=8, column=0)
edit_phone_entry = tk.Entry(root)
edit_phone_entry.grid(row=8, column=1)

tk.Label(root, text="New Email:").grid(row=9, column=0)
edit_email_entry = tk.Entry(root)
edit_email_entry.grid(row=9, column=1)

tk.Label(root, text="New Address:").grid(row=10, column=0)
edit_address_entry = tk.Entry(root)
edit_address_entry.grid(row=10, column=1)

edit_button = tk.Button(root, text="Edit Contact", command=edit_contact)
edit_button.grid(row=11, column=0, columnspan=2, pady=10)

tk.Label(root, text="Delete Name:").grid(row=12, column=0)
delete_entry = tk.Entry(root)
delete_entry.grid(row=12, column=1)

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.grid(row=13, column=0, columnspan=2, pady=10)

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify=tk.LEFT)
result_label.grid(row=14, column=0, columnspan=2, pady=10)

display_contact_gui()

root.mainloop()
