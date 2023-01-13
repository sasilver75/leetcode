"""
First Unique Character in String

Given a string `s`, find the first non-repeating character in ti
and return its index. If it doesn't exist, return -1
"""
import collections


def first_uniq_char(s: str) -> int:
    # O(N)/O(N) solution
    once_seen = set()
    multi_seen = set()
    for char in s:
        if char not in once_seen:
            once_seen.add(char)
        elif char not in multi_seen:
            multi_seen.add(char)

    for idx, char in enumerate(s):
        if char not in multi_seen:
            return idx
    return -1


"""
We can't (easily?) sort the input, because it's possible that there
are multiple "seen once" characters in s, and we need to return the FIRST
of those characters -- so the relative ordering being preserved is important.
"""

"""
We can take advantage of dictionaries remembering their insert-order in 
recent versions of Python (3.6+). So we can just use a counter.
"""


def first_uniq_char_trick(s: str) -> int:
    char_counts = collections.Counter(s)
    for char in char_counts:
        if char_counts[char] == 1:
            return s.index(char)  # Return the index of first occurrence of char

    return -1

def test(fn):
    assert fn("leetcode") == 0
    assert fn("loveleetcode") == 2
    assert fn("aabb") == -1

# test(first_uniq_char)
test(first_uniq_char_trick)