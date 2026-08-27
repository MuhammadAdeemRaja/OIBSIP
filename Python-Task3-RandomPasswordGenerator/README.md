# Random Password Generator

## 📌 Project Overview

This project is a **Random Password Generator** developed using Python and Tkinter. It allows users to generate secure and customizable passwords by selecting the desired password length and character types.

The application provides a simple graphical user interface (GUI) and uses Python's `secrets` module for secure random password generation.

## 🎯 Objective

The main objective of this project is to create a secure, customizable, and user-friendly password generator that can generate strong random passwords quickly.

## ✨ Features

* Generate secure random passwords
* Select password length from 8 to 100 characters
* Uppercase letters (A-Z)
* Lowercase letters (a-z)
* Numbers (0-9)
* Special symbols
* Exclude ambiguous characters
* Copy password to clipboard
* Password strength indicator
* Clear generated password
* Last 5 generated passwords history
* Input validation
* Error handling
* User-friendly Tkinter GUI

## 🛠️ Technologies Used

* **Python 3**
* **Tkinter**
* **Secrets**
* **String**
* **Pyperclip**

## 📦 Installation

Make sure Python 3 is installed on your computer.

Install the required external library:

```bash
pip install pyperclip
```

Tkinter, `secrets`, and `string` are included with standard Python installations.

## ▶️ How to Run

Open the project folder in VS Code or Command Prompt.

Run the following command:

```bash
python password_generator.py
```

The Random Password Generator window will open.

## 📝 How to Use

1. Select the desired password length.
2. Select at least two character types.
3. Choose whether to exclude ambiguous characters.
4. Click **Generate Password**.
5. The generated password will appear in the password field.
6. Click **Copy to Clipboard** to copy the password.
7. Check the password strength indicator.
8. Click **Clear** to remove the current password.

## 🔐 Security

This project uses Python's `secrets` module for password generation.

The `secrets` module is designed to generate cryptographically strong random values and is more suitable for security-sensitive applications such as password generation.

The application also ensures that at least one character is selected from every chosen character type.

## 💪 Password Strength

The application provides a basic password strength indicator based on password length and the number of selected character types.

* **Weak** – Shorter passwords with fewer character types
* **Medium** – Longer passwords using multiple character types
* **Strong** – Passwords of at least 16 characters using 3 or more character types

This is a basic strength indicator and should not be considered a complete security assessment.

## 📂 Project Structure

```text
Python-Task3-RandomPasswordGenerator/
│
├── password_generator.py
├── README.md
└── screenshot.png
```

## 🖼️ Screenshot

Add a screenshot of the running application to this repository as:

```text
screenshot.png
```

The screenshot demonstrates the graphical interface of the Random Password Generator.

## 🎓 Internship Information

**Internship:** Oasis Infobyte Internship Program (OIB-SIP)

**Track:** Python Programming

**Task:** Random Password Generator

**Developer:** Muhammad Adeem Raja

## 🚀 Future Improvements

* Improve the graphical user interface
* Add show/hide password functionality
* Add an advanced password strength meter
* Add customizable password requirements
* Improve password history privacy
* Add additional security features

## 📄 Conclusion

The Random Password Generator is a Python-based GUI application developed as part of the Oasis Infobyte Python Programming Internship. The project demonstrates Python programming, GUI development with Tkinter, secure random password generation, clipboard functionality, input validation, and password strength evaluation.
