"""
Valid Anagram
Category: String

Given two strings `s` and `t`, return `true` if `t` is an ANAGRAM OF `s`,
and `false` otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different
word or phrase, typically using all of the original letters exactly once.
"""

def is_anagram(t: str, s: str):
    counts = {}
    for char in t:
        if char not in counts:
            counts[char] = 0
        counts[char] += 1

    for char in s:
        if char not in counts:
            return False
        counts[char] -= 1
        if counts[char] < 0:
            return False

    for char in counts:
        if counts[char] != 0:
            return False

def test(fn):
    assert fn("anagram", "nagaram") == True
    assert fn("rat", "car") == False
