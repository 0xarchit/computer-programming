# program to check if a list contains any negative numbers

lst = [int(x) for x in input("Enter elements separated by space: ").split()]
contains_negative = False
for num in lst:
    if num < 0:
        contains_negative = True
        break
print("Does the list contain negative numbers?", contains_negative)