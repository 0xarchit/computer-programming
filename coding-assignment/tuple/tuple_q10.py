# program to find the symmetric difference between two tuples
t24 = tuple(input("Enter first tuple: ").split())
t25 = tuple(input("Enter second tuple: ").split())
print(tuple(set(t24) ^ set(t25)))