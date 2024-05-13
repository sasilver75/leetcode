"""
Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s.

(You may assume that the maximum length of s is 1000)
"""


def longest_palindromic_substring_brute(s: str) -> str:
    # Brute: Let's generate all possible substrings and then determine which is the longest of them all
    def is_palindrome(s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if not s[l] == s[r]:
                return False
            l += 1
            r -= 1
        return True

    # O(N^2) loop to generate all possible substrings
    substrings = set()
    for i in range(0, len(s)):
        for j in range(i, len(s)):
            substrings.add(s[i: j + 1])

    # O(N) for each O(N^2) substrings = O(N^3) total
    max_substring = ""
    for substring in substrings:
        if is_palindrome(substring) and len(substring) > len(max_substring):
            max_substring = substring

    print(max_substring)
    return max_substring


assert longest_palindromic_substring_brute("babad") in ["bab", "aba"]  # "aba" is also valid
assert longest_palindromic_substring_brute("cbbd") == "bb"


# ----

"""
Let's be smarter! :) 
We can do this in O(N^2) time.
The insight is that if you have a palindrome like "BB", and you want to expand that palindrome, you could do so by
sandwiching the {valid palindrome} with two identical characters -- like C{BB}C. As long as the two characters that we're
adding are identical and we're making a valid palindrome sandwich, we can just consider it as C{ValidPalindrome}C 

So we can slide across the input string, and from each character, begin a process of growing a window from what we KNOW is a valid
palindrome (a single character).
"""

def longest_palindromic_substring(s: str) -> str:
    longest_palindrome = ""
    for idx, char in enumerate(s):
        i, j = idx, idx
        # We need to first expand the window as long as it can while having identical characters
        while j < len(s) - 1 and s[j+1] == s[i]: # While we can move j to the right (in terms of length and s[j] == s[i])
            j += 1
        while i >= 0 and j < len(s) and s[i] == s[j]:
            ss = s[i: j+1]
            if len(ss) > len(longest_palindrome):
                longest_palindrome = ss
            i -= 1
            j += 1

    print(longest_palindrome)
    return longest_palindrome



assert longest_palindromic_substring("babad") in ["bab", "aba"]  # "aba" is also valid
assert longest_palindromic_substring("cbbd") == "bb" # This provides a unique challenge -- we can't start with a length-1 window! Before we start our usual


def neetcode_solution(s: str) -> str:
    res = ""
    resLen = 0
    for i in range(len(s)):
        # Odd Length
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r-l+1) > resLen:
                res = s[l:r+1]
                resLen = r - l + 1
            l -= 1
            r += 1

        # Even Length
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l  + 1) > resLen:
                res = s[l:r+1]
                resLen = r - l + 1
            l -= 1
            r += 1

    return res


assert neetcode_solution("babad") in ["bab", "aba"]  # "aba" is also valid
assert neetcode_solution("cbbd") == "bb" # This provides a unique challenge -- we can't start with a length-1 window! Before we start our usual

