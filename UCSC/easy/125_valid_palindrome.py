"""
A phrase is a palindrome if, after converting
all uppercase letters into lowercase letters and
removing all non-alphanumeric characters, it 
reads the same forward and backwards. 

Alphanumeric characters include letters and numbers
"""

import string


def valid_palindrome(s: str) -> bool:
    # Clena it
    cleaned = "".join(char.lower() for char in s if char in [*string.ascii_letters, *string.digits])

    # Now walk a pointer from each side
    left, right = 0, len(cleaned)-1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
        
    return True



assert valid_palindrome("A man, a plan, a canal: Panama")
assert not valid_palindrome("race a car")