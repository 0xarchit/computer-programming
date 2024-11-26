# program to check if a tuple is a subset of another
t1 = tuple(input("Enter elements of first tuple: ").split())
t2 = tuple(input("Enter elements of second tuple: ").split())
print(set(t1).issubset(t2))