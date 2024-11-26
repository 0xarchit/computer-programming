# program to count the number of uppercase characters in a string

s = input("Enter a string: ")
count = sum(1 for char in s if char.isupper())
print("Number of uppercase letters:", count)