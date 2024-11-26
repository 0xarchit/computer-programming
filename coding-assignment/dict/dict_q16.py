# Group strings from a list based on their length

words = ['cat', 'dog', 'apple', 'bat', 'banana']
grouped = {}
for word in words:
    grouped.setdefault(len(word), []).append(word)
print(grouped)
