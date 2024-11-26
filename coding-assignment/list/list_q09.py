# program to find intersection of two lists

lst1 = [int(x) for x in input("Enter elements of first list separated by space: ").split()]
lst2 = [int(x) for x in input("Enter elements of second list separated by space: ").split()]
intersection = []
for num in lst1:
    if num in lst2 and num not in intersection:
        intersection.append(num)
print("Intersection:", intersection)