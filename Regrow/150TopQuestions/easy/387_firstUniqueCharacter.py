"""
First Unique Character in a String

Given a string s, find the first non-repeating character in it, and return
its index. If it does NOT exist, return -1!
"""

"""
Thinking of ways to do this:

The "first" non-repeating (unique) character -- so we DO care about preserving
the original order of the string -- we couldn't do somethign like sort the string
and then scan for the first nonrepeating.

What we could do is scan through the string, getting counts of each character
The nscan through it again and return the first character whose count is 1 ... else -1

This would be O(N) and O(N).
"""

def first_unique(s: str) -> int:
    # Populate character counts
    counts = {}
    for char in s:
        if char not in counts:
            counts[char] = 0
        counts[char] += 1

    # seek for first 1-counted character
    for idx, char in enumerate(s):
        if counts[char] == 1:
            return idx

    # fallback: return -1
    return -1


assert first_unique("leetcode") == 0
assert first_unique("loveleetcode") == 2
assert first_unique("aabb") == -1