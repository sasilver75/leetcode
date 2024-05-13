"""
Power of Three

Given an integer n, return TRUE if it is a power of Three
Otherwise, return False.

An integer n is a power of three -- if there exists an integer x such taht
n == 3**x
"""

def is_power_of_three(n: int) -> bool:
    pow = 0
    while 3 ** pow < n:
        pow += 1

    return 3 ** pow == n

assert is_power_of_three(27) == True
assert is_power_of_three(28) == False
assert is_power_of_three(0) == False
assert is_power_of_three(-1) == False