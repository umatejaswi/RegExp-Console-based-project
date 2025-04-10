import re

# Name
x = True
while x:
    pattern = re.compile(r'^[A-Za-z ]+$')
    text = input("Enter Your Name: ")
    res = pattern.fullmatch(text)
    if res is not None:
        name = res.group()
        break
    else:
        print("Enter Name in Correct Format!")

# Date of Birth
while True:
    pattern = re.compile(r'\d{2}-\d{2}-\d{4}')
    text = input("Enter Date of Birth (dd-mm-yyyy): ")
    res = pattern.fullmatch(text)
    if res is not None:
        dob = res.group()
        break
    else:
        print("Enter DOB in Correct Format!")

# Email ID
while True:
    pattern = re.compile(r'[a-z0-9]+@gmail.com\Z')
    text = input("Enter Email ID: ")
    res = pattern.fullmatch(text)
    if res is not None:
        mailid = res.group()
        break
    else:
        print("Enter Mail ID in correct format!")

# Mobile Number
while True:
    pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
    text = input("Enter Mobile Number (xxx-xxx-xxxx): ")
    res = pattern.fullmatch(text)
    if res is not None:
        mobile = res.group()
        break
    else:
        print("Enter Mobile Number in correct Format!")

# Convert mobile to continuous digits
x = ''
for i in mobile:
    if i.isdigit():
        x += i
mobile = x  # Update the mobile number

# Convert DOB to 'dd-mon-yyyy'
month_map = {
    '01': 'jan', '02': 'feb', '03': 'mar', '04': 'apr',
    '05': 'may', '06': 'jun', '07': 'jul', '08': 'aug',
    '09': 'sep', '10': 'oct', '11': 'nov', '12': 'dec'
}
dob = dob[:3] + month_map[dob[3:5]] + dob[5:]

# Final Output
print(f"Name : {name}")
print(f"Date of Birth: {dob}")
print(f"Mail ID: {mailid}")
print(f"Mobile : {mobile}")
