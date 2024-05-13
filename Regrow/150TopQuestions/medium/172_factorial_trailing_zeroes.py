"""
Factorial Trailing Zeroes

Given an integer `n`, return the number of trailing zores in `n!`!

Note that `n!` = n * n-1 * n-2 * ... * 3 * 2 * 1
"""

"""
Okay, what if we just evaluated the factorial of n and then looked
at the number of zeroes, instead of doing something clever off the bat?
"""

def factorial_trailing_zeroes(n: int) -> int:
    fac = 1 # Representing 0! = 1
    for i in range(1, n+1):
        fac = fac * i

    fac_str = str(fac)
    z_count = 0
    idx = len(fac_str)-1
    while fac_str[idx] == "0" and idx >= 0:
        z_count += 1
        idx -= 1

    return z_count



"""
Follow up: Can we get a solution that works in logarithmic time complexity?
My dear I'm not sure that I care to!
"""

assert factorial_trailing_zeroes(3) == 0 # 6 has no trailing zeroes
assert factorial_trailing_zeroes(5) == 1 # 120 has one trailing zero
assert factorial_trailing_zeroes(0) == 0 # 1 has no trailing zeroes
