# program to rearrange tuple elements in alternating even and odd order.
t = tuple(map(int, input("Enter numbers: ").split()))
evens = tuple(x for x in t if x % 2 == 0)
odds = tuple(x for x in t if x % 2 != 0)
print(tuple(even if i % 2 == 0 else odd for i, (even, odd) in enumerate(zip(evens, odds))))