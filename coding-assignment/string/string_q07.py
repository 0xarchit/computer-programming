# program to remove duplicate characters from a string

s = input("Enter a string: ")
s_no_duplicates = "".join(sorted(set(s), key=s.index))
print("String without duplicates:", s_no_duplicates)