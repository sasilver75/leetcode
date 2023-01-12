"""
Valid Palindrome
Category: String

A phrase is a palindrome if, after converting all uppercase letters into lowercase
letters and removing all non-alphanumeric characters, it reads the same
forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.
"""
import string


def is_palindrome(s: str) -> bool:
    # Clean the string
    alphanumerics = set(string.ascii_uppercase + string.ascii_lowercase + string.digits)
    s = "".join([char for char in s if char in alphanumerics]) # s = "".join(filter(lambda char: char in alphanumerics, s))
    l, r = 0, len(s) - 1
    while l <= r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

def test(fn):
    assert fn("A man, a plan, a canal: Panama") == True
    assert fn("race a car") == False
    assert fn(" ") == True

