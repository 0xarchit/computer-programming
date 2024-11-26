# program to check if a string contains any special characters

import string
s = input("Enter a string: ")
special_chars = string.punctuation
if any(char in special_chars for char in s):
    print("Contains special characters")
else:
    print("No special characters")