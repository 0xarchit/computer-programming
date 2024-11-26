# program to sort a list in ascending order

lst = [int(x) for x in input("Enter elements separated by space: ").split()]
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]
print("Sorted list:", lst)