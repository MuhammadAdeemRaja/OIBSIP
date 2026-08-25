import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime


# Create database
def create_database():
    conn = sqlite3.connect("bmi_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bmi_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            weight REAL NOT NULL,
            height REAL NOT NULL,
            bmi REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# Calculate BMI
def calculate_bmi():
    name = name_entry.get().strip()
    weight_text = weight_entry.get().strip()
    height_text = height_entry.get().strip()

    if not name:
        messagebox.showerror("Error", "Please enter your name.")
        return

    try:
        weight = float(weight_text)
        height = float(height_text)
    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter numbers for weight and height."
        )
        return

    if weight <= 0 or height <= 0:
        messagebox.showerror(
            "Invalid Input",
            "Weight and height must be greater than zero."
        )
        return

    # BMI formula
    bmi = weight / (height ** 2)

    # Category
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    result_label.config(
        text=f"BMI: {bmi:.2f}\nCategory: {category}"
    )

    # Save record
    try:
        conn = sqlite3.connect("bmi_records.db")
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO bmi_records
            (name, weight, height, bmi, category, date)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            name,
            weight,
            height,
            bmi,
            category,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ))

        conn.commit()
        conn.close()

        messagebox.showinfo(
            "Success",
            "BMI calculated and record saved successfully."
        )

    except sqlite3.Error as error:
        messagebox.showerror(
            "Database Error",
            f"Could not save the record.\n{error}"
        )


# Show saved records
def show_records():
    try:
        conn = sqlite3.connect("bmi_records.db")
        cursor = conn.cursor()

        cursor.execute("""
            SELECT name, weight, height, bmi, category, date
            FROM bmi_records
            ORDER BY id DESC
        """)

        records = cursor.fetchall()
        conn.close()

        if not records:
            messagebox.showinfo("Records", "No BMI records found.")
            return

        records_window = tk.Toplevel(root)
        records_window.title("BMI Records")
        records_window.geometry("750x400")

        text_box = tk.Text(
            records_window,
            font=("Arial", 11),
            wrap="word"
        )
        text_box.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        for record in records:
            name, weight, height, bmi, category, date = record

            text_box.insert(
                tk.END,
                f"Name: {name}\n"
                f"Weight: {weight} kg | Height: {height} m\n"
                f"BMI: {bmi:.2f} | Category: {category}\n"
                f"Date: {date}\n"
                f"{'-' * 60}\n"
            )

        text_box.config(state="disabled")

    except sqlite3.Error as error:
        messagebox.showerror(
            "Database Error",
            f"Could not read records.\n{error}"
        )


# Create database first
create_database()


# Main window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("500x550")
root.resizable(False, False)


# Title
title_label = tk.Label(
    root,
    text="BMI Calculator",
    font=("Arial", 24, "bold")
)
title_label.pack(pady=20)


# Name
tk.Label(
    root,
    text="Name",
    font=("Arial", 12)
).pack()

name_entry = tk.Entry(
    root,
    font=("Arial", 12),
    width=30
)
name_entry.pack(pady=8)


# Weight
tk.Label(
    root,
    text="Weight (kg)",
    font=("Arial", 12)
).pack()

weight_entry = tk.Entry(
    root,
    font=("Arial", 12),
    width=30
)
weight_entry.pack(pady=8)


# Height
tk.Label(
    root,
    text="Height (meters)",
    font=("Arial", 12)
).pack()

height_entry = tk.Entry(
    root,
    font=("Arial", 12),
    width=30
)
height_entry.pack(pady=8)


# Calculate button
calculate_button = tk.Button(
    root,
    text="Calculate BMI",
    font=("Arial", 12, "bold"),
    command=calculate_bmi,
    width=20
)
calculate_button.pack(pady=15)


# Result
result_label = tk.Label(
    root,
    text="BMI: --\nCategory: --",
    font=("Arial", 16, "bold")
)
result_label.pack(pady=15)


# Records button
records_button = tk.Button(
    root,
    text="View Saved Records",
    font=("Arial", 11),
    command=show_records,
    width=20
)
records_button.pack(pady=10)


# Run application
root.mainloop()