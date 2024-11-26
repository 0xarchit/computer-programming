# program to count occurrences of an element

lst = [int(x) for x in input("Enter elements separated by space: ").split()]
element = int(input("Enter the element to count: "))
count = 0
for num in lst:
    if num == element:
        count += 1
print("Count of", element, ":", count)