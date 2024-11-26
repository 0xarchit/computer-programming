# display common key from dictionary

def find_common_keys(dict1, dict2):
    return list(dict1.keys() & dict2.keys())

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
common_keys = find_common_keys(dict1, dict2)
print(*common_keys)
