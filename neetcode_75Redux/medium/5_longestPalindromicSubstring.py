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
    pass



def test(fn):
    assert fn("babad") in ["bab", "aba"]
    assert fn("cbbd") == "bb"

test(lps_naive)
# test(lps)