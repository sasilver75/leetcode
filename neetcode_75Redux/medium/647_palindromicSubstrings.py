"""
Palindromic Substrings

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome if it reads teh same forwards as  backwards
A substring is an ordered and contiguous sequence of characters within the string
"""

"""
Thinking:
Again, the idea that you can get valid palindromes by expanding outwards
from a valid palindrome.
We want to count the number of expansions of that window that we can do.
Recall that there are odd-lengthed palindromes and even-length palindromes.

We're going to be doing this process of iterating a cross a list of items and
expanding a window, and we want to be incrementing a counter somewhere in there
of the number of valid palindromes. 
We could be doing this incrementation as we do the expansions, or do all of the incrementations
when we get to the maximum length palindrome centered around a root index.
For example, if the longest palindrome that we could get is of length 5, then w
this counts as ceil(5/2)=3 different odd-lengthed palindromes. Alternatively, we could 
have been incrementing the number of palindromes as we go.

"""

def n_palindromic_substrings(s: str) -> int:
    n_palindromes = 0

    def expand_window(l: int, r: int) -> None:
        """
        Called on a valid palindromic window.
        Increment the count of palindromes, and expand the window if:
            1. We have room remaining to expand the window
            2. Expanding the window would result in a valid palindrome
        """
        nonlocal n_palindromes

        n_palindromes += 1

        if l == 0 or r == len(s) - 1 or s[l-1] != s[r+1]:
            return

        expand_window(l-1, r+1)


    for idx in range(len(s)):
        expand_window(idx, idx)

    print("After odds: ", n_palindromes)

    for idx in range(len(s)-1):
        if s[idx] == s[idx+1]:
            expand_window(idx, idx+1)

    print("After evens: ", n_palindromes)


    return n_palindromes


def test(fn):
    assert fn("abc") == 3
    assert fn("aaa") == 6

test(n_palindromic_substrings)