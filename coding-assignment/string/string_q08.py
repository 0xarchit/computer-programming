# program to find the index of the first occurrence of a substring

s = input("Enter a string: ")
sub = input("Enter a substring: ")
index = s.find(sub)
if index != -1:
    print("Index of first occurrence:", index)
else:
    print("Substring not found")