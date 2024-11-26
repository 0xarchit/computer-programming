# program to check if a list is sorted in ascending order

lst = [int(x) for x in input("Enter elements separated by space: ").split()]
is_sorted = True
for i in range(len(lst) - 1):
    if lst[i] > lst[i + 1]:
        is_sorted = False
        break
print("Is the list sorted in ascending order?", is_sorted)