# Convert a nested dictionary into a single-level dictionary

nested_dict = {'a': {'b': 1}, 'c': 2}
flat_dict = {}
for key, value in nested_dict.items():
    if isinstance(value, dict):
        for sub_key, sub_value in value.items():
            flat_dict[f"{key}.{sub_key}"] = sub_value
    else:
        flat_dict[key] = value
print(flat_dict)
