"""
Coin Change

Given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money

Return the FEWEST NUMBER OF COINS that you need to make up that amount!
If that amount of money CANNOT be made by any combination of the coins, return -1

You may assume that you have an infinite number of each type of coin.
"""


def coin_change(coins: list[int], amount: int) -> int:
    min_coins = float('inf')

    def dfs(remaining: int, coins_used: int):
        nonlocal min_coins
        if remaining == 0:
            min_coins = min(min_coins, coins_used)
            return



    return min_coins if min_coins < float("inf") else -1



def coin_change_dp(coins: list[int], amount: int) -> int:
    pass


def test(fn):
    assert fn([1, 2, 5], 11)
    assert fn([2], 3 == -1)
    assert fn([1], 0 == 0)

test(coin_change)
# test(coin_change_dp)
