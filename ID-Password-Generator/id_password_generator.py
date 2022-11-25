import random as rd
x = input("First Name : ")
y = input("Last Name : ")
z = input("DOB[DD/MM/YYYY] : ")
a = ["!","@","#","$","%","^","&","*","~"]
username = (x+y).lower() + z[0:2] + z[3:5] + z[8] + z[9]
password = x[0].upper() + x[1:].lower() + a[rd.randint(0,8)] + str(rd.randint(1,9)) + str(rd.randint(1,9)) + str(rd.randint(1,9)) + str(rd.randint(1,9))
print("Username : ",username)
print("Password : ",password)