# program to find the frequency of each element

lst = [int(x) for x in input("Enter elements separated by space: ").split()]
frequency = {}
for num in lst:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
print("Frequencies:")
for key in frequency:
    print(key, ":", frequency[key])