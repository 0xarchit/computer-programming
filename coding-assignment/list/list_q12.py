# program to remove all occurrences of an element

lst = [int(x) for x in input("Enter elements separated by space: ").split()]
element = int(input("Enter the element to remove: "))
new_list = [num for num in lst if num != element]
print("List after removal:", new_list)