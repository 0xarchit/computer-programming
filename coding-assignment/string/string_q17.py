# program to extract all words that start with a vowel

s = input("Enter a string: ")
words = s.split()
vowel_words = [word for word in words if word[0].lower() in 'aeiou']
print("Words starting with a vowel:", vowel_words)