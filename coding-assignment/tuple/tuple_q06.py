# program to find the Cartesian product of two tuples
t1 = tuple(input("Enter first tuple elements: ").split())
t2 = tuple(input("Enter second tuple elements: ").split())
print(tuple((a, b) for a in t1 for b in t2))