"""
Coin Change

Given an integer array `coins` representing coins of different denominations, and an
integer amount representing a total amount of money.

Return the FEWEST NUMBER OF COINS that you need to make up that amount.

If that mount of money CANNOT be made up by any combination of the coins, return -1

You may assume that you have an INFINITE NUMBER OF COINS for each type of coin.
"""
from typing import Optional


def coin_change(coins: list[int], amount: int) -> int:
    minimum_coins_used = float('inf')

    def dfs(remaining: int, coins_used: int) -> int:
        """Given a remaining amount of coins, return the minimum number of spent coins to get remaining to 0"""
        nonlocal minimum_coins_used

        if remaining < 0:
            return

        if remaining == 0:
            minimum_coins_used = min(minimum_coins_used, coins_used)

        for coin in coins:
            dfs(remaining - coin, coins_used + 1)

    dfs(amount, 0)
    return minimum_coins_used if minimum_coins_used != float('inf') else -1


def coin_change_better(coins: list[int], amount: int) -> int:
    def dfs(remaining: int, coins_used: int) -> Optional[int]:
        if remaining < 0:
            return
        if remaining == 0:
            return coins_used

        # What options could we take, from where we are?
        best_option = float('inf')
        for coin in coins:
            if remaining - coin >= 0:
                choice_result = dfs(remaining - coin, coins_used + 1)
                if choice_result is not None:
                    best_option = min(best_option, choice_result)

        return best_option if best_option != float('inf') else -1

    res = dfs(amount, 0)
    return res


"""
The above searches could be pruned as well, if we wanted to.
We could solve this in a dynamimic programming fashion, however.

DP is of length amount+1
dp[0] = 0
dp[1...] = None

dp[x] = minimum number of coins you can use to spend x
dp[x] = None indicates that you can't (as far as we know) spend from here down to zer.

"""


def coin_change_dp(coins: list[int], amount: int) -> int:
    dp = [None] * (amount + 1)
    dp[0] = 0
    for remaining in range(1, len(dp)):
        for coin in coins:
            # If we can spend the coin, even -- and if the coin gets us to somewhere that can get us to 0,
            if remaining - coin >= 0 and dp[remaining - coin] is not None:
                # Check whether that's our best solution so far, for `remaining`
                dp[remaining] = min(dp[remaining], dp[remaining - coin] + 1) if dp[remaining] is not None else dp[remaining - coin] + 1
    print(dp)
    return dp[amount] if dp[amount] is not None else -1


def test(fn):
    assert fn([1, 2, 5], 11) == 3  # 5+5+1
    assert fn([2], 3) == -1
    assert fn([1], 0) == 0


test(coin_change)
test(coin_change_better)
test(coin_change_dp)
