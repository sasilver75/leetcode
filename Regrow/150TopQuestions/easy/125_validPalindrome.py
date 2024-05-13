"""
Valid Palindrome

A phrase is a palindrome if, after:
    1) converting all uppercase letters into lowercase letters
    2) and removing all non-alphanumeric characters,
it reads the same forward and backward.

Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.


"""
import string


def is_valid_palindrome(s: str) -> bool:
    alphanumeric = string.ascii_letters + string.digits  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
    s = "".join([char for char in s if char in alphanumeric]).lower()
    l = 0
    r = len(s) - 1
    while l < r:
        if not s[l] == s[r]:
            return False
        l += 1
        r -= 1
    return True


assert is_valid_palindrome("A man, a plan, a canal: Panama") == True
assert is_valid_palindrome("race a car") == False
assert is_valid_palindrome(" ") == True
