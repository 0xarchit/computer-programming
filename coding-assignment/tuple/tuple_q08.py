# program to find the union of two tuples
t1 = tuple(input("Enter first tuple: ").split())
t2 = tuple(input("Enter second tuple: ").split())
print(tuple(set(t1) | set(t2)))