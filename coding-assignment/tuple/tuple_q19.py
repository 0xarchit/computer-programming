# program to find the second most frequent element in a tuple.
t = tuple(input("Enter elements: ").split())
frequency = sorted(((x, t.count(x)) for x in set(t)), key=lambda p: p[1], reverse=True)