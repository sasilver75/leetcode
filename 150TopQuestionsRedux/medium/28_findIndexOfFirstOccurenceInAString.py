"""
Find the Index of the First Occurrence in a String

Given two strings `needle` and `haystack`, return the
INDEX of the first occurrence of `needle` in `haystack`, or -1 if `needle`
is not part of haystack.
"""


"""
Here's an O(N^2) Solution (really O(N*M) where M is needle length) -- 
Just for every starting index, consider
the span from starting_index forward, using needle length
"""
def search_naive(haystack: str, needle: str) -> int:
    needle_length = len(needle)
    for starting_index in range(len(haystack)):
        needle_candidate = haystack[starting_index:starting_index+needle_length]
        if needle_candidate == needle:
            return starting_index
    return -1

"""
Can we be smarter?
Could we possibly do this in one O(N) pass, using additional memory 
and some sort of sliding window strategy?

An initial idea would be to use something like a set to keep track of the 
characters in the window, a dict to keep track of the counts of the characters
that are in the sliding window of length needle_length.

But if "abc" were the needle and the window currently contained "cba",
we don't want to accidentally return True. So the concepts of character-count-satisfying
as well as character-ordering are both important...

Ans: This uses the Knuth Morris Pratt (KMP) algorithm for O(N)

KMP spends a little time precomputing a table (on the order of the size of the needle),
and then uses that table to do an efficient search of the string in O(N) time.
KMP makes use of previous match information that the naive version does not.
"""
def search(haystack: str, needle: str) -> int:
    pass


def test(fn):
    assert fn("sadbutsad", "sad") == 0
    assert fn("leetcode", "leeto") == -1

test(search_naive)