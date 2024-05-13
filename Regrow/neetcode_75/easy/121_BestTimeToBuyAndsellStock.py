"""
Best Time to Buy and Sell Stock
Category: Array

You are given an array `prices` where `prices[i]` is the price
of a given stock on the `ith` day.

You want to maximize your profit by choosing a single day to buy
one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.
"""

"""
Insight:
Q: What determines the profit that you receive in a given trade?
A: The SELL PRICE - BUY PRICE = PROFIT

Q: Generally, how do you maximize profit in stock-trading?
A: Buy Low, Sell High!

Q: So given that you're going to sell a given day, what's the best profit? 
A: The maximum profit of selling on a given day is buying at {the best price in the past}
and then selling on that day. The "best price" is the lowest price, for buying.

Q: And the max profit overall?
A: Given that we can only BUY/SELL A SINGLE STOCK, the max profit overall
is not the (maxProfit - minPrice), but instead the maximum of the 
"what if I sold today, having bought at the best past price" for each day?
"""
def max_profit(prices: list[int]) -> int:
    max_profit = 0
    lowest_past_price = prices[1]
    for i in range(1, len(prices)):
        current_price = prices[i]
        # What if I sold today, after having bought @ lowest_past_price
        potential_profit = current_price - lowest_past_price
        max_profit = max(max_profit, potential_profit)

        # Update lowest_past_price
        lowest_past_price = min(lowest_past_price, current_price)

    return max_profit

assert max_profit([7, 1, 5, 3, 6, 4]) == 5
assert max_profit([7, 6, 4, 3, 1]) == 0
