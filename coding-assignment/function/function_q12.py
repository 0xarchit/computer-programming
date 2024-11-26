# functon to Check if a string is an anagram of another
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)