# program to generate all subsets of a tuple
t = tuple(input("Enter elements: ").split())
print([tuple(t[i:j]) for i in range(len(t)) for j in range(i+1, len(t)+1)])