# program to find the second largest element

lst = [int(x) for x in input("Enter elements separated by space: ").split()]
largest = second_largest = float('-inf')
for num in lst:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num
print("Second largest:", second_largest)