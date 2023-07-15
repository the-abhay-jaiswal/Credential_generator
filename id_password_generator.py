import random as rd
import re
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

def is_valid_date(date_string, format_string):
    try:
        datetime.strptime(date_string, format_string)
        return True
    except ValueError:
        return False

def generate_credentials():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    dob = entry_dob.get()
    email = entry_email.get()

    if is_valid_date(dob, "%Y-%m-%d"):
        if re.search("^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$", email):
            username = (first_name + last_name).lower() + dob[0:4]
            password = (
                first_name[0].upper()
                + first_name[1:].lower()
                + rd.choice(["!", "@", "#", "$", "%", "^", "&", "*", "~"])
                + str(rd.randint(1, 9))
                + str(rd.randint(1, 9))
                + str(rd.randint(1, 9))
                + str(rd.randint(1, 9))
                + str(rd.randint(1, 9))
                + str(rd.randint(1, 9))
            )

            messagebox.showinfo("Credentials", f"Username: {username}\nPassword: {password}")
        else:
            messagebox.showerror("Invalid Input", "Invalid email ID")
    else:
        messagebox.showerror("Invalid Input", "Invalid date of birth")

def reset_fields():
    entry_first_name.delete(0, tk.END)
    entry_last_name.delete(0, tk.END)
    entry_dob.delete(0, tk.END)
    entry_email.delete(0, tk.END)

# Create the GUI window
window = tk.Tk()
window.title("Credential Generator")

# Create labels and entry fields
label_first_name = tk.Label(window, text="First Name:")
label_first_name.pack()
entry_first_name = tk.Entry(window)
entry_first_name.pack()

label_last_name = tk.Label(window, text="Last Name:")
label_last_name.pack()
entry_last_name = tk.Entry(window)
entry_last_name.pack()

label_dob = tk.Label(window, text="DOB [YYYY-MM-DD]:")
label_dob.pack()
entry_dob = tk.Entry(window)
entry_dob.pack()

label_email = tk.Label(window, text="Email ID:")
label_email.pack()
entry_email = tk.Entry(window)
entry_email.pack()

# Create the buttons
button_generate = tk.Button(window, text="Generate Credentials", command=generate_credentials)
button_generate.pack()

button_reset = tk.Button(window, text="Reset", command=reset_fields)
button_reset.pack()

# Start the GUI event loop
window.mainloop()





"""
------------------------------------------------------ALGORITHM----------------------------------------------------------------
import random as rd
import re
from datetime import datetime

def is_valid_date(date_string, format_string):
    try:
        datetime.strptime(date_string, format_string)
        return True
    except ValueError:
        return False

x = input("First Name : ")
y = input("Last Name : ")
z = input("DOB[YYYY-MM-DD] : ")
format = "%Y-%m-%d"
a = ["!","@","#","$","%","^","&","*","~"]
em = input("Enter your Email-ID : ")
em_cond = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
username = (x+y).lower() + z[0:4]
password = x[0].upper() + x[1:].lower() + a[rd.randint(0,8)] + str(rd.randint(1,9)) + str(rd.randint(1,9)) + str(rd.randint(1,9)) + str(rd.randint(1,9)) + str(rd.randint(1,9)) + str(rd.randint(1,9))


if is_valid_date(z, format):
    if re.search(em_cond,em):
        print("Username : ",username)
        print("Password : ",password)
    else:
        print("\nInvalid email Id")
else:
    print("Invalid date")

-----------------------------------------------------------------------------------------------------------------------------------
"""