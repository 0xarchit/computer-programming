# program to multiply each element by a constant

lst = [int(x) for x in input("Enter elements separated by space: ").split()]
constant = int(input("Enter the constant to multiply each element by: "))
result = [num * constant for num in lst]
print("List after multiplication:", result)