# program to split a tuple into two halves
t = tuple(input("Enter elements: ").split())
mid = len(t) // 2
print(t[:mid], t[mid:])