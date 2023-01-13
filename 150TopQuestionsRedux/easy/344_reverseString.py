"""
Write a function that reverses a string.
The input string is given as an array of characters.

You must do this by modifying the input array IN-PLACE with
only O(1) of extra memory.
"""


def reverse_string(s: list[str]) -> list[str]:
    l, r = 0, len(s) - 1
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
    return s


assert reverse_string(["h", "e", "l", "l", "o"]) == ["o", "l", "l", "e", "h"]
assert reverse_string(["H", "a", "n", "n", "a", "h"]) == ["h", "a", "n", "n", "a", "H"]
