"""
Best time to buy and sell stock

Given an array PRICES where PRICES[I] is the price of a given
stocko n the i'th day

We want to maximize profit by choosing a SINGLE DAY to buy one stock
and a SINGLE DIFFERENT DAY to sell one stock in the future.

Return the maximum profit that you can achieve from this transaction.
If you can't achieve any profit, return 0.
"""

def max_profit_naive(prices: list[int]) -> int:
    # O(N^2) Brute solution
    max_profit = 0
    for idx, buy_price in enumerate(prices):
        for sell_price in prices[idx+1:]:
            potential_profit = sell_price - buy_price
            max_profit = max(max_profit, potential_profit)
    return max_profit

"""
Instead of brute forcing it, can we keep track of the minimum past price,
so that we know "what's hte best past time that I could have bought at?"
"""
def max_profit(prices: list[int]) -> int:
    max_profit = 0
    min_past_price = prices[0]
    idx = 1
    while idx < len(prices):
        price = prices[idx]
        potential_profit = price - min_past_price
        max_profit = max(max_profit, potential_profit)
        min_past_price = min(min_past_price, price)
        idx += 1

    return max_profit

def test(fn):
    assert fn([7,1,5,3,6,4]) == 5
    assert fn([7,6,4,3,1,]) == 0

test(max_profit_naive)
test(max_profit)
