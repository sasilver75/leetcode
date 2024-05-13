"""
Best Time to Buy and Sell STock (Easy)

Given an array `prices` where `prices[i]` is the PRICE of a given stock on the `ith` day...
We want to MAXIMIZE OUR PROFIT by choosing a SINGLE DAY to buy one stock and choosing a DIFFERENT DAY in the future to sell that stock
    - You can only buy/sell one stock
    - You can't buy and sell a stock on the same day

Return the MAXIMUM PROFIT that you can achieve from this transaction;
if you cannot achieve any profit, return 0!
"""

def max_profit_naive(prices: list[int]) -> int:
    max_profit = -float('inf')
    for buying_index in range(len(prices)):
        for selling_index in range(buying_index+1, len(prices)):
            # Trade Profit = Sell Price - Buy Price
            candidate_profit = prices[selling_index] - prices[buying_index]
            max_profit = max(max_profit, candidate_profit)

    # If you cannot achieve any profit, return 0!
    return max(max_profit, 0)


"""
Instead of doing N^2 comparisons, what we can do is consider, for each day: 
    "What if I sold today, having bought at the best price in the past? What would my profit be?"
"""
def max_profit(prices: list[int]) -> int:
    max_profit = - float('inf')
    lowest_past_buy_price = prices[0]
    for idx in range(1, len(prices)):
        price = prices[idx]

        # What if we sold here?
        candidate_profit = price - lowest_past_buy_price
        max_profit = max(max_profit, candidate_profit)

        # Update LPBP
        lowest_past_buy_price = min(lowest_past_buy_price, price)

    # If we cannot make any profit, return 0
    return max(max_profit, 0)





def test(fn):
    assert fn([7,1,5,3,6,4]) == 5
    assert fn([7,6,4,3,1]) == 0

test(max_profit_naive)
test(max_profit)