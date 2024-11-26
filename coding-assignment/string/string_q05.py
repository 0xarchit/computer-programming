# program to find the longest word in a string

s = input("Enter a string: ")
words = s.split()
longest_word = max(words, key=len)
print("Longest word:", longest_word)