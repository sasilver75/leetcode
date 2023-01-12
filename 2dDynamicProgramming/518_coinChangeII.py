"""
Coin Change II

You are given an integer array `coins` representing coins of different
denominations, and an integer `amount` representing a total amount of money.

Return the NUMBER OF COMBINATIONS to make up that amount!
If that amount of money cannot be made up by any combination of the coins,
return 0.

You may assume that you have an infinite number of each type of coin.

The answer is guaranteed to fit into a signed 32-bit integer


NOTE: We're asking here for the number of COMBINATIONS, where a combination
is actually order-independent. So we don't can about 211 vs 121 vs 112 --
they're all the same thing.
"""


def n_ways_change_naive(amount: int, coins: list[int]) -> int:
    ways = set()

    def helper(remaining: int, used_count=list[int]) -> None:
        if remaining == 0:
            ways.add(tuple(used_count))

        for idx, coin in enumerate(coins):
            if remaining - coin >= 0:
                new_used_count = [*used_count]
                new_used_count[idx] += 1
                helper(remaining - coin, new_used_count)

    helper(amount, [0] * len(coins))

    return len(ways)


"""
Can we do better?

I think we can with some caching... Imagine we had a caching key of 

(remaining, used_counts) would perhaps be the key used.

Let's try it out 
"""

"""
Neetcode:
Better to think of it like this:

               Amounts Remaining
            5   4   3   2   1   0
        1   _   _   _   _   _   _   
        2   _   _   _   _   _   _
Coin    5   _   _   _   _   _   _


Where DP[coins][amountRemaining]
We can initialize all of the "0" column to 1.

               Amounts Remaining
             5   4   3   2   1   0
          _________________________
        1|   _   _   _   _   _   1   
        2|   _   _  {_}   _   _   (1)
Coin    5|   _   _   _   _   _   [1]

What's the formula for DP[coins][amount]

What does the bottom-right position mean? That I'm highlighting with the [] 
"If we could only choose from the single coin 5, and we have 0 coins remaining, how many ways could we sum up to 0?"
The answer is 1 different way.

What about the position above that, marked with the ()?
"If we could choose from either 2 or 5, and we have 0 coins remaining, how many ways could we sum to 0?"

And so on and so on.
For an arbitrary position like  the one highlighted with {},
it's asking:
"How many ways can we sum up to 3, using only coins [2,5]?"

So what order would it make sense to compute these values?
Probably "bottom-up". since "using only coins [5]" is a subproblem of "using only coins [2,5]"

So let's do it column by column from the right to the left, populating the
column from bottom to top.

dp[coin][amount] = dp[coin][amount-coin] + dp[coin-1][amount]
    - The choice is like... Okay, given that I'm now in the case
    wehre I can use any of [1,2,5], I can either "use 1" (the first term in equation),
    or I can "not used 1, and use the other coins" (the second term in the equation)
    - In the DP table, this means looking to our right by coin cost, and looking 
    directly below us.
"""


def n_ways_change(amount: int, coins: list[int]) -> int:
    coins.sort()

    # Set up DP
    dp = [
        [0] * (amount + 1)
        for _ in range(len(coins))
    ]
    last_row = len(dp)-1
    last_col = len(dp[0])-1

    # Populate the rightmost column with ones
    for row in range(len(dp)):
        dp[row][-1] = 1

    # Populate the columns right to left, bottom to top rows for each
    for col in range(last_col - 1, -1, -1): # Col
        for row in range(last_row, -1, -1): # Row
            coin_value = coins[row]

            right = dp[row][col + coin_value] if col + coin_value <= last_col else 0  # What if we used the current coin? That would put us at amount-coin remaining, which confusingly in this table is actually amount+coin in terms of indices
            down = dp[row + 1][col] if row + 1 <= last_row else 0  # What if we chose not to use the current coin?

            dp[row][col] = right + down

    return dp[0][0]  # Meaning "Using all coins, at the highest amount"


def test(fn):
    assert fn(5, [1, 2, 5]) == 4  # 5, 221, 2111, 11111
    assert fn(3, [2]) == 0  # Cannot be made
    assert fn(10, [10]) == 1  # 10


test(n_ways_change_naive)
test(n_ways_change)
