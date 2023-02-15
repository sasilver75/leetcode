"""
Longest Palindromic Substring

Given a string s, return the LONGEST PALINDROMIC SUBSTRING in s
"""

def lps_naive(s: str) -> str:
    longest_ss = None

    def is_palindrome(s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    # Generate all substrings
    for start_index in range(len(s)):
        for end_index in range(start_index, len(s)):
            ss = s[start_index:end_index+1]
            if is_palindrome(ss):
                if longest_ss is None or len(ss) > len(longest_ss):
                    longest_ss = ss

    # print(longest_ss)
    return longest_ss


"""
How can we do better?

Think: What is the definition of a palindrome?
Symmetrical around the center
So a string of length 1 is a palindrome
And we can extend that palindrome if the charactrs on the outside of the palindrome
match

b{validPalindrome}b = {largerValidPalindrome}
c{validPalindrome}d = Not a larger palindrome

So we could start with a window of length 1 at all of the characters
and then we could expand it outwards as much as possible, updating lps

but that would only give us the odd-length palindromes!
So we need to do another pass starting with windows of length-two where
applicable, to capture palindromes like abba or cddc.

It might make sense to have a single expand_window function that, given a valid
palindromic window, expands the window while possible.
"""
def lps(s: str) -> str:
    longest_palindromic_substring = ""

    def expand_window(l: int, r: int) -> str:
        """
        Given a window of s[l:r+1] specifying a confirmed, palindromic substring
        expand that window into larger palindromic substrings while possible.
        Return the largest palindromic substring
        """
        # Base Case: We have no remaining space to further expand the palindrome window
        # Alternatively/or we DO have the space, but the expanded window would not be palindromic
        if l == 0 or r ==   len(s) - 1 or s[l-1] != s[r+1]:
            return s[l:r+1]

        # Expand the window if it would be a valid palindrome
        return expand_window(l-1, r+1)

    # Assess Odd-Lenghted Palindromic Substrings
    for idx, char in enumerate(s):
        palindromic_substring = expand_window(idx, idx)
        if len(palindromic_substring) > len(longest_palindromic_substring):
            longest_palindromic_substring = palindromic_substring

    # Assess Even-Lengthed Palindromic Substrings
    for idx in range(len(s) - 1):
        if s[idx] == s[idx+1]:
            palindromic_substring = expand_window(idx, idx+1)
        if len(palindromic_substring) > len(longest_palindromic_substring):
            longest_palindromic_substring = palindromic_substring

    return longest_palindromic_substring







def test(fn):
    assert fn("babad") in ["bab", "aba"]
    assert fn("cbbd") == "bb"

test(lps_naive)
test(lps)