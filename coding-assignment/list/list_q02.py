# program to find maximum in a list

lst = [int(x) for x in input("Enter elements separated by space: ").split()]
maximum = lst[0]
for num in lst:
    if num > maximum:
        maximum = num
print("Maximum:", maximum)