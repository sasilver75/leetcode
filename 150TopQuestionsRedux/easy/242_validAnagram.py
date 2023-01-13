"""
Valid Anagram

Given two strings s and t, return True if t is an ANAGRAM for s, and false otherwise

An anagram is a word or phrase formed by rearranging the letters of a different
word or phrase, typically using all of the original letters exactly once.
"""
import collections


def is_anagram(s: str, t:str) -> bool:
    char_counts = collections.defaultdict(int)
    for char in s:
        char_counts[char] += 1
    for char in t:
        char_counts[char] -= 1
        # Early Exit here
        if char_counts[char] < 0:
            return False

    return all(v == 0 for v in char_counts.values())

assert is_anagram("anagram", "nagaram") == True
assert is_anagram("rat", "car") == False