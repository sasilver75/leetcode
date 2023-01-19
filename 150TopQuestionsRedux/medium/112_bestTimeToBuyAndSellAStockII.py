"""
Best Time to Buy and Sell a Stock II

Given an integer array `prices` where `prices[i]` is the rice of a
given stock on the `ith` day.

On each day, you may decide to buy and/or sell the stock.
You can only hold at most one share of the stock at any time.

However, you can buy it and then immediately sell it on the next day.
Find and return the MAX PROFIT that you can achieve.
"""

"""            /\
          /\  /  \
         /  \/    \
        /          \  /
                    \/
        
        b s b  s    b  s
                    
An omnipotent trader who gets max profit would buy at ever local minima
and sell at every local maxima.

last_min = prices[0]
last_max = None

for price in prices[1:]:
    if not last_min:
        last_min = price 
        continue
    
"""
def max_profit(prices: list[int]) -> int:
    """
    TODO: What if there is a "plateau"?
        - Only the last flat price should be considered a local maxima
        - Only the last flat price should be considered a local minima

    What about
            /
       - - /
     /
    /
    """
    profit = 0
    bought_price = None # TODO: prices[0]?
    for i in range(len(prices)): # TODO: 1, len(prices)?
        price = prices[i]

        # Is price a local minima? Buy!
        if (prices[i-1] if i - 1 >= 0 else float('inf')) >= price < (prices[i+1] if i + 1 < len(prices) else float('inf')):
            bought_price = price

        # Is price a local maxima? Sell (assuming we have a bought stock)
        if bought_price is not None and (prices[i-1] if i - 1 >= 0 else -float('inf')) <= price > (prices[i+1] if i + 1 < len(prices) else -float('inf')):
            profit += (price - bought_price)

    return profit


assert max_profit([7, 1, 5, 3, 6, 4]) == 7 # Buy day 2, sell day 3, buy day 4, sell day 5
assert max_profit([1, 2, 3, 4, 5]) == 4 # Buy on day 1 and sell on day 5
assert max_profit([7, 6, 4, 3, 1]) == 0 # No way to make a positive profit
