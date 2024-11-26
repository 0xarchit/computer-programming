# program to replace all occurrences of a value in a tuple
t35 = tuple(input("Enter elements: ").split())
old = input("Enter value to replace: ")
new = input("Enter new value: ")
print(tuple(new if x == old else x for x in t35))