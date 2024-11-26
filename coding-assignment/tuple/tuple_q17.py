# program to group tuple elements based on their parity (odd/even).
t = tuple(map(int, input("Enter numbers: ").split()))
print((tuple(x for x in t if x % 2 == 0), tuple(x for x in t if x % 2 != 0)))