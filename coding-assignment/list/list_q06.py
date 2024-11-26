# program to remove duplicates from a list

lst = [int(x) for x in input("Enter elements separated by space: ").split()]
unique_list = []
for num in lst:
    if num not in unique_list:
        unique_list.append(num)
print("List without duplicates:", unique_list)