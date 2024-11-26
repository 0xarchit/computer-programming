# program to check if a string starts with a given substring

s = input("Enter a string: ")
sub = input("Enter a substring: ")
if s.startswith(sub):
    print(f"String starts with '{sub}'")
else:
    print(f"String does not start with '{sub}'")