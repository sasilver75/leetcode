"""
Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s!
"""

def with_return_value(fn):
    def wraps(*args, **kwargs):
        ans = fn(*args, **kwargs)
        print(f"{args, kwargs, ans}")
        return ans
    return wraps


def lpss_naive(s: str) -> str:
    """
    Naive solution
        1. Generate all substrings
        2. Filter to palindromic
        3. Select the longest one
    """
    # @with_return_value
    def is_palindrome(s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    longest = ""
    for start in range(len(s)):
        for end in range(start, len(s)):
            ss = s[start:end+1]
            if is_palindrome(ss):
                longest = ss if len(ss) > len(longest) else longest

    print(longest)
    return longest


def lpss(s: str) -> str:
    """
    How can we do better than N^3?
    We can use a (pair of) sliding window strategies with the knowledge that a{palindrome}a == {largerPalindrome}
    """
    longest_palindrome = ""

    # Odd-Lengthed Palindromes
    for idx in range(len(s)):
        l, r = idx, idx
        # While we CAN expand in both directions AND expanding results in
        while (
            l-1 >= 0 and
            r + 1 < len(s) and
            s[l-1] == s[r+1]
        ):
            l -= 1
            r += 1

        # We cannot expand our palindromic substring any wider
        palindrome = s[l:r+1]
        longest_palindrome = palindrome if len(palindrome) > len(longest_palindrome) else longest_palindrome


    # Even-Lengthed Palindromes
    for idx in range(len(s) - 1):
        if s[idx] == s[idx+1]:
            l, r = idx, idx+1

        while (
                l - 1 >= 0 and
                r + 1 < len(s) and
                s[l - 1] == s[r + 1]
        ):
            l -= 1
            r += 1

        # We cannot expand our palindromic substring any wider
        palindrome = s[l:r+1]
        longest_palindrome = palindrome if len(palindrome) > len(longest_palindrome) else longest_palindrome

    return longest_palindrome


def test(fn):
    assert fn("abc") == "a"
    assert fn("babad") == "bab"
    assert fn("cbbd") == "bb"

# test(lpss_naive)
test(lpss)