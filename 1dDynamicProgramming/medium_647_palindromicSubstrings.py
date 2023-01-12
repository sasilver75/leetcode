"""
647 Palindromic Substrings

Given a string s, return the NUMBER of palindromic substring in it!
A string is a palindrome when it reads the same backwards and forwards.
A substring is a contiguous sequence of characters within the string
"""
from typing import Callable


def check_sol(fn: Callable) -> bool:
    # assert fn("abc") == 3
    # assert fn("aaa") == 6
    assert fn("aaaa") == 10 # Aaaa, aAaa, aaAa, aaaA, AAaa, aAAa, aaAA, AAAa, aAAA, AAAA


def is_palindrome(s: str) -> bool:
    l = 0
    r = len(s) - 1
    while l < r:
        if not s[l] == s[r]:
            return False
        l += 1
        r -= 1
    return True

# assert is_palindrome("aba") == True
# assert is_palindrome("abba") == True
# assert is_palindrome("abbac") == False


# -----------

def palindromic_substring_brute(s: str) -> int:
    # GEnerate all substirngs
    substrings = []
    for i in range(0, len(s)):
        for j in range(i, len(s)):
            substrings.append(s[i:j+1])

    n_palindromes = 0
    for substring in substrings:
        if is_palindrome(substring):
            print(substring)
            n_palindromes += 1

    print(n_palindromes)
    return n_palindromes

check_sol(palindromic_substring_brute)

# -----------

def palindromic_substring(s: str) -> int:
    n_palindromes = 0

    for idx in range(len(s)):
        l, r = idx, idx
        # Expand rightward as much as possible (identical characters), counting each palindrome
        while r < len(s) and s[r] == s[l]:
            n_palindromes += 1
            r += 1

        # Expand window in both directions while it makes sense
        while l >= 0 and r < len(s) and s[l] == s[r]:
            n_palindromes += 1
            l -= 1  # Expand window outwards
            r += 1
    print(f"{s} has {n_palindromes} palindromes")
    return n_palindromes



check_sol(palindromic_substring) # This isn't captugin "AAa" or "aAA" currently.

# -----------

def neetcode_solution(s: str) -> int:
    res = 0

    for i in range(len(s)):
        l = r = i

        # Accounting for Odd-length Palindromes (a, aaa, aaaaa)
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1

        # Accounting for Even-length Palindromes : Notice that we don't be double-counting! (aa, aaaa, aaaaaa)
        l = i
        r = i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
    return res


check_sol(neetcode_solution)