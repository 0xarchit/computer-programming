# program to check if a string has any repeating characters

s = input("Enter a string: ")
if len(s) != len(set(s)):
    print("Has repeating characters")
else:
    print("No repeating characters")