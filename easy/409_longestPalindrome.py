"""
Given a string s which cosnsists of lowercase or uppercase letters, return the
length of the LONGEST PALINDROME that can be built with those letters.

Note that letters are CASE SENSITIVE -- for example, "Aa" is not considered
a palindrome, here.
"""

def longest_palindrome(s: str) -> str:
    char_counts = {}
    for char in s:
        if not char in char_counts:
            char_counts[char] = 0
        char_counts[char] += 1

    pal_length = 0

    # Count off pairs... 7 -> 6 characters to be used in palindrome
    for char in char_counts:
        count = char_counts[char]
        pal_length += count - (count % 2)

    # We've counted off all the pairs... But there can still be a center char: OXO or OOO
    # If there's at least one odd number
    if any(char_counts[char] % 2 == 1 for char in char_counts):
        pal_length += 1

    return pal_length

assert longest_palindrome("abccccdd") == 7
assert longest_palindrome("abbddccc") == 7