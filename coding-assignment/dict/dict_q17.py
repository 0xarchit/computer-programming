# Increment all values in a dictionary by 1 if they are greater than 5

dictionary = {'a': 6, 'b': 3, 'c': 8}
updated_dict = {k: (v + 1 if v > 5 else v) for k, v in dictionary.items()}
print(updated_dict)