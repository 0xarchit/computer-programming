# program to reverse a List

lst = [int(x) for x in input("Enter elements separated by space: ").split()]
reversed_list = []
for i in range(len(lst) - 1, -1, -1):
    reversed_list.append(lst[i])
print("Reversed list:", reversed_list)