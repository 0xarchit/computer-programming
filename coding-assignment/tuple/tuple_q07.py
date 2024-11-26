# program to extract elements greater than a given number
t = tuple(map(int, input("Enter numbers separated by spaces: ").split()))
n = int(input("Enter the threshold number: "))
print(tuple(x for x in t if x > n))