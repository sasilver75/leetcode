"""
Coin Change

You are given an integer array `coins` representing coins of
different denominations and an integer `amount` representing a
total amoutn of money.

Return the FEWEST NUMBER OF COINS that you need to make up that amount!
If that amount of money CANNOT be made up by any combo, return -1

You may assume that you have an INFINITE NUMBER of each kind of coin
"""

"""
1,2,1 and 2,1,1
"""


def fewest_coins_brute(coins: list[int], target: int) -> int:
    def helper(coins_used: int = 0, remaining: int = target) -> int:
        if remaining == 0:
            return coins_used

        options = [helper(coins_used + 1, remaining - coin)
                   for coin in coins
                   if remaining - coin >= 0]
        return min(
            options
        ) if options else -1

    ans = helper()
    print(ans)
    return ans


def fewest_coins(coins: list[int], target: int) -> int:
    dp = [None] * (target+1)
    dp[0] = 0

    for i in range(1, len(dp)):
        options = [
            dp[i-coin] + 1
            for coin in coins
            if i - coin >= 0 and dp[i-coin] is not None # If coin is spendable and gets us to a visited spot
        ]

        if options:
            dp[i] = min(options)

    return dp[target] if dp[target] is not None else -1


def test(fn):
    assert fn([1, 2, 5], 11) == 3  # (5+5+1)
    assert fn([2], 3) == -1  # Cannot make
    assert fn([1], 0) == 0  # 0


test(fewest_coins_brute)
test(fewest_coins)