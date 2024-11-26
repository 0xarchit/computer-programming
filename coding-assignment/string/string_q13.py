# program to remove punctuation from a string

import string
s = input("Enter a string: ")
s_no_punctuation = s.translate(str.maketrans('', '', string.punctuation))
print("String without punctuation:", s_no_punctuation)