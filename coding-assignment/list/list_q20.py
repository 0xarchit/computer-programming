# program to find the index of the last occurrence of an element

lst = [int(x) for x in input("Enter elements separated by space: ").split()]
element = int(input("Enter the element to find the last occurrence: "))
last_index = -1
for i in range(len(lst) - 1, -1, -1):
    if lst[i] == element:
        last_index = i
        break
print("Last index of", element, ":", last_index)