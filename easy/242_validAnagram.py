"""
Given two strings, s and t, return TRUE if t
is an ANAGRAM of s, and false otherwise.

An ANAGRAM is a word or phrase formed by rearranging
the letters of a different word or phrase, typically
using all of the original letters exactly once.
"""


def is_anagram(s: str, t: str) -> bool:
    """
    Insight:
    Two anagrams have the same characters in them
    So if we count the characters in each, we should have
    the same number of characters
    """
    char_counts = {}
    for char in s:
        if not char in char_counts:
            char_counts[char] = 0
        char_counts[char] += 1

    for char in t:
        if char not in char_counts:
            return False
        char_counts[char] -= 1
        if char_counts[char] == 0:
            del char_counts[char]

    # If char_counts is empty, then return True; else false
    return False if char_counts else True

assert is_anagram("anagram", "nagaram") == True
assert is_anagram("rat", "car") == False