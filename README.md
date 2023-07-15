# Credential Generator

The Credential Generator is a Python GUI application that generates credentials (username and password) based on user inputs such as first name, last name, date of birth, and email ID.

## Features

- Validates the date of birth (DOB) to ensure it is in the correct format (YYYY-MM-DD).
- Validates the email ID using a regular expression pattern.
- Generates a username by concatenating the first name, last name, and the first four characters of the DOB.
- Generates a password using your name and some random characters.

## Requirements

- Python 3.x
- tkinter (a built-in Python library for creating GUI applications)

## Usage

1. Install Python from the official Python website (https://www.python.org) if you don't have it installed already.
2. Install the required `tkinter` library by executing the following command:
   pip install tk
4. Clone this repository or download the source code.
5. Open a terminal or command prompt and navigate to the directory containing the source code files.
6. Run the application by executing the following command:
   python credential_generator.py
6. The GUI window will appear, prompting you to enter your first name, last name, date of birth (in the format YYYY-MM-DD), and email ID.
7. Click the "Generate Credentials" button to generate the username and password based on the provided information.
8. The generated credentials will be displayed in a message box.
9. Click the "Reset" button to clear all the input fields and start over.
