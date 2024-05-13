"""
Longest Palindromic Substring
Category: String

Given a string `s`, return the LONGEST palindromic substring in s!
"""


def longest_palindromic_substring_brute(s: str) -> str:
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

    substrings = [ss for ss in substrings if is_palindrome(ss)]

    # Select longest palindromic substrings
    return max(substrings, key=len)


"""
How can we do better than the N^3 above?
Can we do N^2 by expanding a window at each character?
We can expand the window if we know that we have a {palindrome} and we 
know that the left-neighbor and right-neighbor both equal eachotehr.

O(N^2), O(N) 
"""


def longest_palindromic_substring(s: str) -> str:
    if not s:
        return 0

    longest_length = 1
    longest_substring = s[0]

    # For odd-lengthed palindromic substrings (starting with length-1)
    for idx in range(len(s)):
        length = 1
        l, r = idx - 1, idx + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            length += 2
            if length > longest_length:
                longest_length = length
                longest_substring = s[l:r + 1]
            l -= 1
            r += 1

    # For even-lengthed palindromic substrings (starting with length-2)
    for idx in range(0, len(s) - 1):
        if not s[idx] == s[idx+ 1]:
            continue
        length = 0
        l, r = idx, idx + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            length += 2
            if length > longest_length:
                longest_length = length
                longest_substring = s[l:r + 1]

            l -= 1
            r += 1

    print(longest_length, longest_substring)
    return longest_substring


# -- Test --
def test(fn):
    assert fn("babad") == "bab"
    assert fn("cbbd") == "bb"


test(longest_palindromic_substring_brute)
test(longest_palindromic_substring)
