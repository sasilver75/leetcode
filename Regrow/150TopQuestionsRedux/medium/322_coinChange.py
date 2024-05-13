"""
Coin Change

Given an integer array coins if nums[idx] < nums[comparison_idx] coins of different denominations,
and an integer amount representing a total amount of money

Return the FEWEST NUMBER OF COINS that you need to make up that amount
If the amount of money cannot be made up by any combination of the coins,
return -1

You may assume that you have an infinite number of each kind of coin
"""
from collections import deque

"""
Let's just generate EVERY way to make amount using coins, and remember
the shortest one
"""


def coin_change_naive_dfs(coins: list[int], amount: int) -> int:
    fewest_coins_used = float('inf')

    def dfs(current_amount: int, coins_used: int):
        nonlocal fewest_coins_used

        if current_amount > amount:
            return
        if current_amount == amount:
            fewest_coins_used = min(fewest_coins_used, coins_used)

        for coin in coins:
            dfs(current_amount + coin, coins_used + 1)

    dfs(0, 0)

    return fewest_coins_used if fewest_coins_used < float('inf') else -1


"""
I suppose we're really looking for the shortest path through the recursive tree
in order to get to our answer, which would mean a breadth first search
would be a better option.
"""
def coin_change_naive_bfs(coins: list[int], amount: int) -> int:

    node_queue = deque()
    node_queue.appendleft((0, 0))
    while node_queue:
        running_total, coins_used = node_queue.pop()

        if running_total == amount:
            return coins_used

        for coin in coins:
            if running_total + coin <= amount:
                node_queue.appendleft((running_total+coin, coins_used+1))

    return -1



""""
Is there a DP option? 1-d DP table

DP of length amount+1
dp[i] = Fewest # of coins to make i, using `coins`
dp[i] = min(
            dp[i-coin]
        ) for coin in coins
          if i - coin >= 0 and dp[i - coin] is not 0
"""
def coin_change_dp(coins: list[int], amount: int) -> int:
    dp = [None] * (amount+1)
    dp[0] = 0

    for i in range(len(dp)):
        # Reachable amounts
        paths = [
            dp[i-coin]
            for coin in coins
            if i-coin >= 0 and dp[i-coin] is not None
        ]

        if paths:
            dp[i] = min(paths) + 1

    return dp[amount] if dp[amount] is not None else -1

    
        



def test(fn):
    assert fn([1, 2, 5], 11) == 3
    assert fn([2], 3) == -1
    assert fn([1], 0) == 0


# test(coin_change_naive_dfs)
# test(coin_change_naive_bfs)
test(coin_change_dp)
