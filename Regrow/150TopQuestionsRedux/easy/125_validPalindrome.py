"""
Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase
letters, and removing all non-alphanumeric characters, it reads the same forward
and backward. Alphanumeric characters include letters are numbers.

Given a string s, return True if it's a palindrome or false otherwise
"""
import string


def valid_palindrome(s: str) -> int:
    allowed = set(string.digits + string.ascii_lowercase)
    s = "".join([char for char in s.lower() if char in allowed])
    l, r = 0, len(s) - 1

    while l <= r:
        if s[l] != s[r]:
            return False
        r -= 1
        l += 1

    return True

assert valid_palindrome("A man, a plan, a canal: Panama") == True
assert valid_palindrome("race a car") == False
assert valid_palindrome(" ") == True
