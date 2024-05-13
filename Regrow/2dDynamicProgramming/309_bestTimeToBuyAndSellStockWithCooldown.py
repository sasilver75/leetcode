"""
Best Time to Buy and Sell Stock with Cooldown
Difficulty: Medium

You are given an array `prices` where prices[i] is the price of
a given stock on the ith day.

Find the maximum profit you can achieve.
You may complete as many transactions as you'd like.
(i.e. buy one and sell one share of the stock multiple times)

Catch:
* After you sell your stock, you CANNOT BUY STOCK THE NEXT DAY)
    - i.e. there is a cooldown of one day

Note:
    you may not engage in multiple transactions simultaneously (i.e. you must sell
    the stock before you buy again).
"""

"""
Thinking: This is interesting to me, because this isn't obviously a 
2-D dynamic programming problem at first glance, is it? Feels like a one
dimensional one?...

We can either buy or we can sell, but we can only sell if we've bought
the stock before.

At the beginning of the array, are we buying or selling?
[1,2,3,0,2]
At the beginning, index=0, are we buying or selling?
    - Of course, we can only buy
                      0
                    Start
            Buy             Cooldown
            -1                  0
            
    On the left path what can we do? We can either:
    Sell or Cooldown
    
                      0
                    Start
            Buy             Cooldown
            -1                  0
    Sell        Cooldown
    1           -1
    
We can see that at each index, we have the opportunity to either COOLDOWN,
or (BUY or SELL)... so far. But what about exploring after the Sell decision?


                      0
                    Start
            Buy             Cooldown
            -1                  0
    Sell        Cooldown
    1           -1
    
    Cooldown
    1
    
    Our only option after a sell is to COOLDOWN -- it's like we "skipped" a day!
    
    The next day, we can either do a Buy/Cooldown again.
    
    The height of this tree will be N, the number of days, and the
    number of decisions at each level increases by 2, so this would be O(2^N).
    
    With caching, we can reduce this this to O(N)!
    The two cache keys that we'll be using are the:
    (day_index: int, can_buy: bool)
    
    How big will this cache space be?
    day_index has N values, and can_buy has two values.
    So there are 2N possible cache values, which reduces to O(N).
        
"""


def max_profit(prices: list[int]) -> int:
    dp = {}  # (idx, can_buy): max_profit

    def dfs(idx: int, can_buy: bool) -> int:
        # Base Case 1: We're "out of days"
        if idx >= len(prices):
            return 0

        # Base Case 2: Answer is already in dp cache
        if (idx, can_buy) in dp:
            return dp[(idx, can_buy)]


        if can_buy:
            # We're in the buying state. Our two options are to buy or to cooldown
            buy = dfs(idx + 1, False) - prices[idx]   # Max profit of the "remaining" array, starting at the enxt state, minus the cost of buying this stock
            cooldown = dfs(idx+1, True)

            # We're curious which one created the maximum profit
            dp[(idx, can_buy)] = max(buy, cooldown)

        else:
            # We're in the selling state. Our two options are to sell or cooldown. If we sell, we MUST cooldown next turn.
            # We skip a day when we sell, to cooldown
            sell = dfs(idx+2, True) + prices[idx] # Max profit of "remaining" time after selling today
            cooldown = dfs(idx+1, False)

            # We're curious which one created the maximum profit
            dp[(idx, can_buy)] = max(sell, cooldown)

        return dp[(idx, can_buy)]

    dfs(0, True)
    return dp[(0, True)] # Necessarily the maximum of the DP.values() will be at dp[(0, True)]






def test(fn):
    assert fn([1, 2, 3, 0, 2]) == 3  # buy, sell, cooldown, buy, sell
    assert fn([1]) == 0


test(max_profit)
