# program to check if two strings are anagrams

s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")
if sorted(s1) == sorted(s2):
    print("Anagrams")
else:
    print("Not anagrams")