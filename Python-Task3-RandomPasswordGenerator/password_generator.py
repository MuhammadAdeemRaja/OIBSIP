import tkinter as tk
from tkinter import messagebox
import secrets
import string
import pyperclip


# Character sets
UPPERCASE = string.ascii_uppercase
LOWERCASE = string.ascii_lowercase
NUMBERS = string.digits
SYMBOLS = string.punctuation

AMBIGUOUS = "0Ol1I"


# Store last 5 passwords
password_history = []


# Generate secure password
def generate_password():
    try:
        length = int(length_var.get())
    except ValueError:
        messagebox.showerror(
            "Invalid Length",
            "Please enter a valid password length."
        )
        return

    if length < 8:
        messagebox.showerror(
            "Invalid Length",
            "Password length must be at least 8 characters."
        )
        return

    selected_sets = []

    if uppercase_var.get():
        selected_sets.append(UPPERCASE)

    if lowercase_var.get():
        selected_sets.append(LOWERCASE)

    if numbers_var.get():
        selected_sets.append(NUMBERS)

    if symbols_var.get():
        selected_sets.append(SYMBOLS)

    # At least two character types
    if len(selected_sets) < 2:
        messagebox.showerror(
            "Invalid Selection",
            "Please select at least two character types."
        )
        return

    # Remove ambiguous characters if selected
    if ambiguous_var.get():
        selected_sets = [
            "".join(
                char for char in charset
                if char not in AMBIGUOUS
            )
            for charset in selected_sets
        ]

    # Make sure selected sets are not empty
    selected_sets = [
        charset for charset in selected_sets
        if charset
    ]

    if len(selected_sets) < 2:
        messagebox.showerror(
            "Invalid Selection",
            "The selected character types contain no usable characters."
        )
        return

    # Guarantee one character from every selected type
    password_characters = [
        secrets.choice(charset)
        for charset in selected_sets
    ]

    # Combined character pool
    all_characters = "".join(selected_sets)

    # Fill remaining length
    for _ in range(length - len(password_characters)):
        password_characters.append(
            secrets.choice(all_characters)
        )

    # Securely shuffle password
    for i in range(len(password_characters) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        password_characters[i], password_characters[j] = (
            password_characters[j],
            password_characters[i]
        )

    password = "".join(password_characters)

    # Display password
    password_var.set(password)

    # Copy automatically
    try:
        pyperclip.copy(password)
        clipboard_label.config(
            text="Password copied to clipboard!"
        )
    except Exception:
        clipboard_label.config(
            text="Password generated."
        )

    # Add to history
    password_history.insert(0, password)

    # Keep only last 5
    if len(password_history) > 5:
        password_history.pop()

    update_history()
    update_strength(length, len(selected_sets))


# Copy password manually
def copy_password():
    password = password_var.get()

    if not password:
        messagebox.showwarning(
            "No Password",
            "Please generate a password first."
        )
        return

    try:
        pyperclip.copy(password)
        clipboard_label.config(
            text="Password copied to clipboard!"
        )
    except Exception:
        messagebox.showerror(
            "Clipboard Error",
            "Could not copy the password."
        )


# Update password strength
def update_strength(length, character_types):
    if length >= 16 and character_types >= 3:
        strength = "Strong"
    elif length >= 12 and character_types >= 2:
        strength = "Medium"
    else:
        strength = "Weak"

    strength_var.set(f"Strength: {strength}")


# Update history list
def update_history():
    history_listbox.delete(0, tk.END)

    for index, password in enumerate(password_history, start=1):
        history_listbox.insert(
            tk.END,
            f"{index}. {password}"
        )


# Clear password
def clear_password():
    password_var.set("")
    strength_var.set("Strength: --")
    clipboard_label.config(text="")


# Main window
root = tk.Tk()

root.title("Random Password Generator")

root.geometry("600x700")

root.resizable(False, False)


# Title
title_label = tk.Label(
    root,
    text="Random Password Generator",
    font=("Arial", 22, "bold")
)

title_label.pack(pady=15)


# Password length
tk.Label(
    root,
    text="Password Length",
    font=("Arial", 12, "bold")
).pack()

length_var = tk.IntVar(value=16)

length_spinbox = tk.Spinbox(
    root,
    from_=8,
    to=100,
    textvariable=length_var,
    width=10,
    font=("Arial", 12)
)

length_spinbox.pack(pady=8)


# Character type section
tk.Label(
    root,
    text="Character Types",
    font=("Arial", 12, "bold")
).pack(pady=(10, 5))


uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)


tk.Checkbutton(
    root,
    text="Uppercase Letters (A-Z)",
    variable=uppercase_var,
    font=("Arial", 11)
).pack(anchor="w", padx=180)


tk.Checkbutton(
    root,
    text="Lowercase Letters (a-z)",
    variable=lowercase_var,
    font=("Arial", 11)
).pack(anchor="w", padx=180)


tk.Checkbutton(
    root,
    text="Numbers (0-9)",
    variable=numbers_var,
    font=("Arial", 11)
).pack(anchor="w", padx=180)


tk.Checkbutton(
    root,
    text="Symbols (!@#$...)",
    variable=symbols_var,
    font=("Arial", 11)
).pack(anchor="w", padx=180)


# Ambiguous characters option
ambiguous_var = tk.BooleanVar(value=False)

tk.Checkbutton(
    root,
    text="Exclude ambiguous characters (0, O, l, 1)",
    variable=ambiguous_var,
    font=("Arial", 11)
).pack(pady=12)


# Generate button
generate_button = tk.Button(
    root,
    text="Generate Password",
    font=("Arial", 12, "bold"),
    command=generate_password,
    width=25
)

generate_button.pack(pady=10)


# Password display
password_var = tk.StringVar()

password_entry = tk.Entry(
    root,
    textvariable=password_var,
    font=("Consolas", 13),
    width=45,
    justify="center"
)

password_entry.pack(pady=8)


# Copy button
copy_button = tk.Button(
    root,
    text="Copy to Clipboard",
    font=("Arial", 11),
    command=copy_password,
    width=20
)

copy_button.pack(pady=5)


# Clipboard status
clipboard_label = tk.Label(
    root,
    text="",
    font=("Arial", 10)
)

clipboard_label.pack()


# Strength
strength_var = tk.StringVar(
    value="Strength: --"
)

strength_label = tk.Label(
    root,
    textvariable=strength_var,
    font=("Arial", 14, "bold")
)

strength_label.pack(pady=10)


# Clear button
clear_button = tk.Button(
    root,
    text="Clear",
    font=("Arial", 10),
    command=clear_password,
    width=15
)

clear_button.pack(pady=5)


# History
tk.Label(
    root,
    text="Last 5 Generated Passwords",
    font=("Arial", 12, "bold")
).pack(pady=(15, 5))


history_listbox = tk.Listbox(
    root,
    width=55,
    height=6,
    font=("Consolas", 10)
)

history_listbox.pack(pady=5)


# Start application
root.mainloop()