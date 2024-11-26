# program to count the number of vowels in a string

s = input("Enter a string: ")
vowels = "aeiou"
count = 0
for char in s:
    if char.lower() in vowels:
        count += 1
print("Number of vowels:", count)