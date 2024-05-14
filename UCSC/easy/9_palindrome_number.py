"""
Given an integer x, return true if x is a 
palindrome, and false otherwise.
"""

import itertools


def palindrome_naive(num: int) -> bool:
    """
    I suppose the naivest thing we could do is think about how we'd solve this if it were 
    a string. We can use two pointers, and walk them from each opposing side twoards the 
    center. If something is violated, we return False early, else return True

    The one thing to consider is what to do when numbers are negative numbers
    eg is -22 a palindrome? Not clear to me. Let's assuming that it is and just abs it
    EDIT: Oh, nevermind, it's NOT.
    """
    if num < 0:
        return False
    num_s = str(num)
    i,j = 0, len(num_s)-1
    while i < j: # It's fine when i == j, because a palidnrome of length 1
        if num_s[i] != num_s[j]:
            return False
        i += 1
        j -= 1
    return True

def palindrome_recursive(num: int) -> bool:
    """
    I don't think that there's a smarter way to really do this, but just
    showing that we could do this in a recursive manner too, if that's at all interesting.
    """
    if num < 0:
        return False
    num_s = str(num)
    def _recurse(num: int) -> bool:
        if len(num) <= 1:
            return True
        if num[0] != num[len(num) - 1]:
            return False
        return _recurse(num[1:len(num)-1])

    return _recurse(num_s)

# ----

fns = (palindrome_naive, palindrome_recursive)

cases = (
    (121, True),
    (-121, False),
    (10, False)
)

for fn, (inp, output) in itertools.product(fns, cases):
    assert fn(inp) == output
    print(f"{fn.__name__} passed")