"""
Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false
otherwise
"""


def valid_anagram(s, t):
    """
    Returns true if t is an anagram of s, and false otherwise

    Insight:
    Two words are anagrams for eachother if their per-character "balance" is 0
    (adding 1 for word A and subbing 1 for word B when char X is observed)
    """
    counts = {}
    for char in s:
        if char not in counts:
            counts[char] = 0
        counts[char] += 1

    for char in t:
        if char not in counts:
            return False
        counts[char] -= 1

    return all([val == 0 for val in counts.values()])


assert valid_anagram("anagram", "nagaram") == True
assert valid_anagram("rat", "car") == False
