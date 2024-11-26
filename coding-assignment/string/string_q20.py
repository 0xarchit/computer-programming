# program to convert a string to its ASCII equivalent

s = input("Enter a string: ")
ascii_values = [ord(char) for char in s]
print("ASCII values:", ascii_values)