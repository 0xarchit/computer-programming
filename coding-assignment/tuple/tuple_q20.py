# program to split a tuple into chunks of size `n`.
t = tuple(input("Enter elements: ").split())
n = int(input("Enter chunk size: "))
print([t[i:i + n] for i in range(0, len(t), n)])