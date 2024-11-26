# program to remove the first occurrence of an element

lst = [int(x) for x in input("Enter elements separated by space: ").split()]
element = int(input("Enter the element to remove: "))
if element in lst:
    lst.remove(element)
print("List after removal:", lst)