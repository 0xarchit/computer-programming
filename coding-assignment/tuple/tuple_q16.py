# program to find all pairs of elements from a tuple whose sum equals a given number.
t = tuple(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target sum: "))
print([(x, y) for x in t for y in t if x + y == target and x <= y])
