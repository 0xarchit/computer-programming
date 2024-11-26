# program to find unique elements in a tuple
t = tuple(input("Enter elements separated by spaces: ").split())
print(tuple(set(t)))