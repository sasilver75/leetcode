"""
Given an array prices where prices[i] is the
price of a given stock on the ith day...

You want to maximize your profit by choosing a
SINGLE day to buy one stock and choosing a DIFFERENT DAY
in the future to SELL that stock.

Return the maximum profit you can achieve from this
transaction.

If you can't achieve any profit, return 0
"""

# To maximize stock price, you want to buy low and sell high.
def max_profit_dumb(prices: list[int]) -> int:
    # The dumb way is to compare each price with the future highest price
    max_profit = 0
    for idx, buy_price in enumerate(prices):
        if idx < len(prices) - 1: #
            max_future_price = max([f_price for f_price in prices[idx+1:]])
            current_max_profit = max_future_price-buy_price
            max_profit = max(max_profit, current_max_profit)
    return max_profit


# Smarter way: What if we kept track of the past lowest price we've seen at every point, and asked ourselves: "What if I sold now?"
def max_profit(prices: list[int]) -> int:
    max_profit = 0
    if len(prices) <= 1:
        return 0
    lowest_price = prices[0]
    for current_price in prices[1:]:
        # What if I sold now? What would I stand to make?
        current_profit = current_price - lowest_price
        # Is that the bets profit I've seen so far?
        max_profit = max(max_profit, current_profit)
        # Is this the lowest price that I've seen so far? Would this be the best time to buy, so far?
        lowest_price = min(lowest_price, current_price)

    return max_profit

assert max_profit([7,1,5,3,6,4]) == 5
assert max_profit([7,6,4,3,1]) == 0