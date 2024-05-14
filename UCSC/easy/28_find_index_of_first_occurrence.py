"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.


"""

def find_needle_naive(haystack: str, needle: str) -> int:
    """
    Return the index of the first occurrence of the needle in haystack
    For each position in the 
    Runs in NK time (haystack being length k, needle being length n)
    """
    # at every position
    for start_idx in range(len(haystack)):
        # Take a needle-sized bite and compare it to our needle; is it the same?
        bite = haystack[start_idx:start_idx+len(needle)]
        if bite == needle:
            print("Found ", needle, f" at {start_idx}")
            return start_idx
    print("Not found: ", needle)
    return -1


def find_needle(haystack: str, needle: str) -> int:
    """
    Return the index of the first occurrence of the needle in haystack
    The idea is that we use some sort of extra memory to avoid having to do a linear scan over the elngth of the needle.
    Like if the haystack is 10,0000 long, and the needle is 2,000, then that's a lot of length-2000 scans
    But we care about the specific string being present, not a permutation of it
        -  So we need to keep track of both ORDER _and_ the count of characters
        This seems hard

    ANSWER: This is actually an instance where people use the Knuth Morris Pratt algorithm to search for a string in a sequence
    this isn't worth learning

    """
    ...


for fn in [
    find_needle_naive,
    find_needle
]:
    assert fn("sadbutsad", "sad") == 0, f"{fn.__name__} 1"
    assert fn("leetcode", "leeto") == -1, f"{fn.__name__} 2" # not present