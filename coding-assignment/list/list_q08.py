# program to check if a list is palindrome

lst = [int(x) for x in input("Enter elements separated by space: ").split()]
is_palindrome = True
for i in range(len(lst) // 2):
    if lst[i] != lst[len(lst) - 1 - i]:
        is_palindrome = False
        break
print("Is palindrome:", is_palindrome)