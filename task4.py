#Develop an advanced password generator with a graphical user interface (GUI) using Tkinter or PyQt.
#Enhance it by including options for password complexity, adherence to security rules, and clipboard integration for easy copying.
import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    length = int(entry_length.get())
    include_upper = var_upper.get()
    include_numbers = var_numbers.get()
    include_symbols = var_symbols.get()

    characters = string.ascii_lowercase  # start with lowercase letters

    if include_upper:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    # Ensure the length of the password is valid
    if length < 1:
        messagebox.showerror("Error", "Password length must be at least 1.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    entry_password.delete(0, tk.END)
    entry_password.insert(0, password)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(entry_password.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Initialize the GUI application
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("400x300")

# Label and entry for password length
label_length = tk.Label(root, text="Password Length:")
label_length.pack(pady=10)
entry_length = tk.Entry(root)
entry_length.pack(pady=5)

# Checkboxes for password complexity
var_upper = tk.BooleanVar()
var_numbers = tk.BooleanVar()
var_symbols = tk.BooleanVar()

check_upper = tk.Checkbutton(root, text="Include Uppercase Letters", variable=var_upper)
check_upper.pack(pady=5)
check_numbers = tk.Checkbutton(root, text="Include Numbers", variable=var_numbers)
check_numbers.pack(pady=5)
check_symbols = tk.Checkbutton(root, text="Include Symbols", variable=var_symbols)
check_symbols.pack(pady=5)

# Entry to display the generated password
entry_password = tk.Entry(root, width=40)
entry_password.pack(pady=10)

# Buttons to generate the password and copy it to the clipboard
button_generate = tk.Button(root, text="Generate Password", command=generate_password)
button_generate.pack(pady=10)

button_copy = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
button_copy.pack(pady=5)

# Run the GUI loop
root.mainloop()