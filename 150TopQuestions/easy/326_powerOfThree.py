"""
Power of Three

Given an integer n, return TRUE if it is a power of three! Else, return false.

An integer is a power of three if there exists an integer x such that n == 3 ** x
"""

def is_power_of_three(n: int) -> bool:
    # Assuming only natural numbers (positive integers) for powers
    if n < 1:
        return False
    power = 0
    current = 3 ** power
    while current < n:
        power += 1
        current = 3 ** power

    return current == n




assert is_power_of_three(27) == True
assert is_power_of_three(0) == False
assert is_power_of_three(-1) == False