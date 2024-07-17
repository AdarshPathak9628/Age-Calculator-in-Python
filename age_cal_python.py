##  program to enter a dob and calculate its age.

import datetime

# Get the current date
dob = datetime.datetime.now()
cy = dob.year
cm = dob.month
cd = dob.day

# Get the user's date of birth
DOB = input("Enter your DOB (dd/mm/yyyy): ").split("/")
d = int(DOB[0])
m = int(DOB[1])
y = int(DOB[2])

print(type(cd), type(d))

# Calculate the difference in days
if cd < d:
    if cm in [1, 3, 5, 7, 8, 10, 12]:
        cd=cd+31
    elif cm in [4, 6, 9, 11]:
        cd = cd+30
    else:
        # Check for leap year in February
        if (cy % 4 == 0 and cy % 100 != 0) or (cy % 400 == 0):
            cd = cd+29
        else:
            cd = cd+28
    cm = cm-1

rd = cd - d

# Calculate the difference in months
if cm < m:
    cm = cm+12
    cy = cy-1

rm = cm - m
ry = cy - y

print(f"{ry} years, {rm} months, {rd} days")

