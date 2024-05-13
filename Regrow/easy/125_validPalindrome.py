"""
A phrase is a palindrome if, after lowercasing and removing
all non-alphanumeric characters, it reads the same forward and backwards.

Alphanumeric characters contain both letters and numbers
"""
import string

ALPHANUMERICS = set(string.ascii_letters + string.digits)

def is_valid_palindrome(s: str) -> bool:
    # Preprocess String
    s_clean = "".join([char for char in s.lower() if char in ALPHANUMERICS])

    # Two Pointers, walk towards center, compare values
    l = 0
    r = len(s_clean)-1
    while l < r:
        if s_clean[l] != s_clean[r]:
            return False
        l += 1
        r -= 1
    return True


assert is_valid_palindrome("A man, a plan, a canal: Panama") == True
assert is_valid_palindrome("Tacocat") == True
assert is_valid_palindrome("race a car") == False
assert is_valid_palindrome(" ") == True