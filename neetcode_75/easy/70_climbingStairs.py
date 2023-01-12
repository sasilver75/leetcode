"""
Climbing Stairs
Category: DP

You are climbing a staircase. It takes n steps
to reach the top. Each time, you can climb either 1
or 2 steps. In how many distinct ways can you climb to
the top?
"""


def climb_stairs(n: int) -> int:
    if n <= 2:
        return n

    dp = [0] * (n + 1)
    dp[0] = 0  # 1?
    dp[1] = 1
    dp[2] = 2

    for i in range(3, len(dp)):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


def climb_stairs_constant_memory(n: int) -> int:
    if n <= 2:
        return max(n, 0)

    n_minus_2 = 1
    n_minus_1 = 2

    for i in range(3, n + 1):  # Check iteration boundary
        ans = n_minus_1 + n_minus_2
        n_minus_2 = n_minus_1
        n_minus_1 = ans

    return ans


def test(fn):
    assert fn(2) == 2  # (2), (1)
    assert fn(3) == 3  # (111), (21), (12)
    assert fn(4) == 5  # (11111), (112), (121), (211), (22)
    assert fn(5) == 8  # (11111), (1112), (1121), (1211), (2111), (122), (212), (221)


test(climb_stairs)
test(climb_stairs_constant_memory)
