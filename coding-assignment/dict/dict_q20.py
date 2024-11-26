# Create a dictionary with cumulative sums as values

dictionary = {'a': 10, 'b': 20, 'c': 30}
cumulative_sum = 0
cumulative_dict = {}
for key, value in dictionary.items():
    cumulative_sum += value
    cumulative_dict[key] = cumulative_sum
print(cumulative_dict)
