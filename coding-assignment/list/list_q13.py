# program to find the second smallest element

lst = [int(x) for x in input("Enter elements separated by space: ").split()]
first_smallest = second_smallest = float('inf')
for num in lst:
    if num < first_smallest:
        second_smallest = first_smallest
        first_smallest = num
    elif num < second_smallest and num != first_smallest:
        second_smallest = num
print("Second smallest element:", second_smallest)