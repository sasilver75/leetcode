"""
You're climbing a staircase that takes n steps to reach the top.

Eahc time, you can climb 1 or 2 steps. How many distinct ways can you climb to the top?
"""

def with_print(f):
    def _with_print(n):
        ans = f(n)
        print(ans)
        return ans
    return _with_print

@with_print
def count_ways(n: int) -> int:
    if n < 0:
        return 0
    if n == 0:
        return 1

    return count_ways(n-1) + count_ways(n-2)


assert count_ways(2) == 2
assert count_ways(3) == 3
assert count_ways(4) == 5
assert count_ways(6) == 10

# 222
# 2211
# 2112
# 1122
# 21111
# 12111
# 11211
# 11121
# 11112
# 111111