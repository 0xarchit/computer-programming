# program to find the second largest word in a string

s = input("Enter a string: ")
words = s.split()
sorted_words = sorted(words, key=len, reverse=True)
second_largest = sorted_words[1] if len(sorted_words) > 1 else None
print("Second largest word:", second_largest)