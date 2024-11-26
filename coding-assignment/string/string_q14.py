# program to check if a string is a valid email

email = input("Enter your email: ")
if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")