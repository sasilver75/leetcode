"""
Find the index of the first occurrence in a string

Given two strings `needle` and `haystack`, return the INDEX of the FIRST
occurrence of `needle` in haystack, or -1 if `needle` is not part of `haystack`
"""
from typing import Callable, Any


def with_print(fn: Callable) -> Any:
    def wrapper(*args, **kwargs):
        ans = fn(*args, **kwargs)
        print(f"Returning {ans}")
        return ans
    return wrapper

# @with_print
def first_occurrence_brute(needle: str, haystack: str) -> int:
    """
    This is going to run in O(N*M) time where N/M are the length of needle/haystack
    """
    for i in range(0, len(haystack) - len(needle)):
        match = True
        for j in range(0, len(needle)):
            if haystack[i+j] != needle[j]:
                match = False
                break
        if match:
            return i

    return -1

"""
Knuth Morris Pratt *KMP* Algorithm for O(N) Time String Searching
https://zerobone.net/blog/cs/knuth-morris-pratt/

The main idea is to cut out repeated work by doing some preprocessing.
In the previous example, we had a (say, length 4 needle), and we would, for each
character in the ...

TBH this is a pretty complex search algorithm -- I don't think that this would
be a good test of someone's ability -- to be able to to independently, under pressure,
in 30 minutes, reinvent a search algorithm invented by Knuth. I'm going to skip this,
I think... for now...

"""


def first_occurrence(needle: str, haystack: str) -> int:
    pass


# /!\ -- Test Zone -- /!\
def test(fn: Callable):
    assert fn("sad", "sadbutsad") == 0
    assert fn("leetcode", "leeto") == -1
    assert fn("sam", "abasabasamab") == 7


test(first_occurrence_brute)
test(first_occurrence)
