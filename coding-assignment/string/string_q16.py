# program to find the shortest word in a string

s = input("Enter a string: ")
words = s.split()
shortest_word = min(words, key=len)
print("Shortest word:", shortest_word)