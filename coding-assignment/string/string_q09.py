# program to replace all occurrences of a substring in a string

s = input("Enter a string: ")
old_sub = input("Enter the substring to replace: ")
new_sub = input("Enter the new substring: ")
new_string = s.replace(old_sub, new_sub)
print("Modified string:", new_string)