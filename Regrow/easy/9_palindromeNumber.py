import math


# Have a pointer at each end of the palindrome.
def is_palindrome(num: int):
    if num < 0:
        return False
    num = str(num).lower() # This doesn't mutate the num object passed to the function -- only rebinds the name num locally to a new object
    i = 0
    j = len(num) - 1
    while i < j:
        if num[i] != num[j]:
            return False
        i += 1
        j -= 1
    return True

def test(fn):
    cases = [
        (121, True),
        (-121, False),
        (10, False),
    ]

    for inp, soln in cases:
        ans = fn(inp)
        print(
            f"""
Testing: {inp}
Answer: {ans}
Correct: {ans == soln}
"""
        )

test(is_palindrome)