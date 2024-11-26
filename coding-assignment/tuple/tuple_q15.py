# program to check if any element in a tuple starts with a specific character
t37 = tuple(input("Enter words: ").split())
ch = input("Enter starting character: ")
print(any(word.startswith(ch) for word in t37))