# prgram to find key with the maximum value in a dictionary
data = {'a': 10, 'b': 25, 'c': 17}
max_value_key = None
max_value = 0
for key, value in data.items():
    if value > max_value:
        max_value = value
        max_value_key = key
print(max_value_key)