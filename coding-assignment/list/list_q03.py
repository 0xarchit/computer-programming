# program to find the calculate the average of a list

lst = [int(x) for x in input("Enter elements separated by space: ").split()]
total = 0
for num in lst:
    total += num
average = total / len(lst)
print("Average:", average)