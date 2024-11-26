# program to remove all whitespace from a string

s = input("Enter a string: ")
s_without_space = "".join(s.split())
print("String without spaces:", s_without_space)