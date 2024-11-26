# remove duplicate code from dictionary

dictionary = {'a': 1, 'b': 2, 'c': 1}
unique_dict = {}
for key, value in dictionary.items():
    if value not in unique_dict.values():
        unique_dict[key] = value
print(unique_dict)
