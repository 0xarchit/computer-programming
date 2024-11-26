# swapping of key and value of dictionary

def swap_key_value(d):
    return {v: k for k, v in d.items()}

data = eval(input("Enter a dictionary (e.g., {'a': 1, 'b': 2}): "))
print(swap_key_value(data))