"""
Palindromic Substrings
Category: String

Given a string s, return the NUMBER of palindromic substrings in it!
A string is a palindrome when it reads the same backwards as forwards.

A substring is a contiguous sequence of characters in the string.
"""


def count_palindromic_substrings_naive(s: str) -> int:
    """ O(N)^3 time and O(N)^2 memory using brute generation+filter"""
    # Generate all substrings
    substrings = []
    for start in range(len(s)):
        for end in range(start, len(s)):
            substrings.append(s[start:end + 1])

    # Filter to palindromic substrings
    def is_palindrome(s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    palindromic_substrings = [ss for ss in substrings if is_palindrome(ss)]
    print(palindromic_substrings)

    # Return Count
    return len(palindromic_substrings)


def count_palindromic_substrings(s: str) -> int:
    """O(N^2) time and O(N) memory using expanding/contracting window"""
    n_palindromes = 0

    # Count the Odd-Lengthed Palindromic Substrings
    for idx in range(len(s)):
        l, r = idx, idx
        while l >= 0 and r < len(s) and s[l] == s[r]:
            n_palindromes += 1
            l -= 1
            r += 1

    # Count the Even-Lengthed Palindromic Substrings
    for idx in range(len(s)-1):
        l, r = idx, idx + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            n_palindromes += 1
            l -= 1
            r += 1

    return n_palindromes


def test(fn):
    assert fn("abc") == 3  # ['a', 'b', 'c']
    assert fn("aaa") == 6  # ['a', 'aa', 'aaa', 'a', 'aa', 'a']
    assert fn("abba") == 6  # ['a', 'abba', 'b', 'bb', 'b', 'a']


test(count_palindromic_substrings_naive)
test(count_palindromic_substrings)
