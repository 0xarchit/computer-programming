# program to merge two tuples into a dictionary
keys = tuple(input("Enter keys separated by spaces: ").split())
values = tuple(input("Enter values separated by spaces: ").split())
print(dict(zip(keys, values)))