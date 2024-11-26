#  Keep only keys starting with the letter a

dictionary = {'apple': 1, 'banana': 2, 'avocado': 3}
filtered_dict = {k: v for k, v in dictionary.items() if k.startswith('a')}
print(filtered_dict)