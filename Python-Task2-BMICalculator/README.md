# BMI Calculator

## Oasis Infobyte Internship — Task 2

### Developed By
Muhammad Adeem Raja

### Track
Python Programming

### Task
Task 2 — BMI Calculator




## Project Overview

This project is a Python-based BMI Calculator developed as part of the Oasis Infobyte Python Programming Internship.

The application provides a graphical user interface where users can enter their name, weight, and height. It calculates BMI, displays the BMI category, and saves the result in an SQLite database.




## Features

- User-friendly graphical interface using Tkinter
- Input fields for name, weight, and height
- BMI calculation using the standard formula
- BMI displayed up to two decimal places
- BMI category classification
- Input validation for invalid and negative values
- Multiple user BMI records
- SQLite database for storing BMI records
- View previously saved BMI records
- Date and time stored with each record
- Database error handling
- Clear error and success messages




## BMI Formula

BMI is calculated using the following formula:

BMI = Weight (kg) / Height² (m)

The program classifies the calculated BMI into the following categories:

- Underweight: BMI below 18.5
- Normal: BMI 18.5–24.9
- Overweight: BMI 25–29.9
- Obese: BMI 30 or above

These categories are implemented according to the internship task requirements and are intended for this programming exercise.




## Technologies Used

- Python 3.13
- Tkinter
- SQLite3
- Datetime




## Installation

Python 3.13 or a compatible Python version is required.

Tkinter and SQLite3 are included with standard Python installations.

No additional external libraries are required for the current version.




## How to Run

Open the project folder in VS Code and run:

`bash
python bmi_calculator.py
`

Alternatively, click the **Run Python File** button in VS Code.


## How to Use

1. Open the BMI Calculator.
2. Enter the user's name.
3. Enter weight in kilograms.
4. Enter height in meters.
5. Click **Calculate BMI**.
6. The BMI value and category will be displayed.
7. The record will automatically be saved in the SQLite database.
8. Click **View Saved Records** to view previous records.




## Database

The application uses SQLite to store BMI records.

The database stores:

 User name
 Weight
 Height
 BMI
 BMI category
 Date and time

The database file is automatically created when the application runs.




## Error Handling

The application validates user input and displays helpful error messages when:

 Name is missing
 Weight or height is not numeric
 Weight or height is zero or negative
 Database operations fail


## Privacy

The application stores BMI records locally in an SQLite database file created within the project.

No personal information is intentionally sent to an external service by this application.




## Future Improvements

Possible future improvements include:

 BMI trend visualization using Matplotlib
 Colour-coded BMI results
 Delete and update BMI records
 Improved graphical design
 Export records to CSV
 Additional data visualization features




## Internship

This project was developed as part of the **Oasis Infobyte Python Programming Internship**.

Task: Task 2 — BMI Calculator


