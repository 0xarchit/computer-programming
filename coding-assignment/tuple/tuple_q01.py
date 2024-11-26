# program to find the second largest element in a tuple
t = tuple(map(int, input("Enter numbers separated by spaces: ").split()))
print(sorted(set(t))[-2])