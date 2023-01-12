"""
Coin Change

You are given coins of different denominations and total amount of money `amount`

Write a function to compute the FEWEST NUMBER OF COINS that you need to make
up that amount.

If that amount of money CANNOT be made up by any combination
of the coins, RETURN -1.

You may assume that you have an INFINITE NUMBER of each kind of coin.
"""
from typing import Callable, Optional


def coin_change_brute(coins: list[int], amount: int) -> int:

    def helper(coins: list[int], remaining: int, used: int = 0) -> Optional[int]:
        # Base Case: We're reached target
        if remaining == 0:
            # print("Remaining 0 -- used: ", used)
            return used

        # Base Case: We can't reach target using (coins, remaining)
        if not any(remaining - coin >= 0 for coin in coins):
            return None  # "Magic None" -- Fix?

        # Recurse into all available coin options. This is a list of Union[int, None] values
        paths = [helper(coins, remaining - coin, used + 1) for coin in coins if remaining - coin >= 0]

        # Return min coins used. It's possible that Some/All of these elements are None.
        return min(path for path in paths if path is not None) if any(val is not None for val in paths) else None

    res = helper(coins, amount)
    return res or -1


"""
How can we be more intelligent, though? I'm sure that we're solving recurring subproblems
in the recursive brute force solution above.
Would it be better to attempt to do a bottom-up dynamic programming type solution?
Where the ith element in a dp table is the minimum number of coins that it would take to get there?
And we just build UP to our target number?
"""

def coin_change_dp(coins: list[int], amount: int) -> int:
    dp = [None] * (amount + 1) # Where the ith index is the MINIMUM COINCOUNT to get to i
    dp[0] = 0

    for i in range(1, amount + 1):
        options = [dp[i-coin] for coin in coins if i - coin >= 0 and dp[i-coin] is not None]
        if not options:
            dp[i] = None # Using "None" to mark "Cannot get to finish line from here"... I realize that I also intialized the list to be all Nones too.
        else:
            dp[i] = min(options) + 1

    return dp[amount] or -1



# --- Test Zone ---
def test(fn: Callable) -> None:
    assert fn([1, 2, 5], 11) == 3
    assert fn([2], 3) == -1

test(coin_change_brute)
test(coin_change_dp)