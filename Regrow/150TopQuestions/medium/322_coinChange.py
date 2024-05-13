"""
Coin Change

You are given an integer array `coins` representing coins of different
denominations and an integer `amount` representing a total amount of money.

Return the FEWEST number of coins that you need to make that amount!

If that amount of money CANNOT be made up by any combination of the coins,
return -1

You may assume that you have an infinite number of each kind of coin.

"""


def coinChangeBrute(coins: list[int], amount: int) -> int:
    if amount == 0:
        return 0

    def helper(coins_used: int = 0, remaining: int = amount):
        if remaining == 0:
            return coins_used

        paths = [
            helper(coins_used + 1, remaining - coin)
            for coin in coins
            if remaining - coin >= 0
        ]

        return min(paths) if paths else float('inf')

    minWays = helper()
    return minWays if minWays != float('inf') else -1


"""
Can we do better?

This could be a dynamic programming question, 1-D.

dp[i] = 
"""

def coinChange(coins: list[int], amount: int) -> int:
    if amount == 0:
        return 0

    dp = [None] * (amount+1)
    dp[0] = 0

    for i in range(len(dp)):
        paths = [
            dp[i - coin]
            for coin in coins
            if i - coin >= 0
            and dp[i-coin] is not None
        ]

        if paths:
            dp[i] = min(paths) + 1

    return dp[amount] or -1


def test(fn):
    assert fn([1, 2, 5], 11) == 3 # 5+5+1
    assert fn([2], 3) == -1
    assert fn([1], 0) == 0

# test(coinChangeBrute)
test(coinChange)