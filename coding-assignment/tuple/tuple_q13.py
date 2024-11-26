# program to check if a tuple is a palindrome
t = tuple(input("Enter elements: ").split())
print(t == t[::-1])