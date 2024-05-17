"""
Given an array of prices where prices[i] is the price ofa given stock on the ith day

You want to maximize your profit by choosing a SINGLE day to buy one stock, and choose a DIFFERENT day
in the future to sell THAT stock.

Return the MAXIMUM PROFIT you can achieve from this transaction. If you can't achieve any profit, return 0
"""

def maxProfit(prices: list[int]) -> int:
    """
    The trick to this quesiton is ask yourself what it means to maximize profit
    You sell high, and buy low.

    One way of determining what the maximum profit of a sequence would be is taking the max of 
    the maximum profit that you could have earned if you made the "best sale possible" at every specific
    timestep.
    Meaning, at a given timestamp, consider: What if we bought at the lowest past price and sold at the
    current price? What would that profit be? Would it be better than the best profit we've seen so far?
    """
    maxProfit = 0
    lowestPrice = prices[0]
    for price in prices[1:]:
        # What if we sold at the lowest price?
        potentialProfit = price - lowestPrice

        # Update MaxProfit?
        prev = maxProfit
        maxProfit = max(maxProfit, potentialProfit)
        print(f"At {price} updated maxprofit from {prev} -> {maxProfit}")

        # Update lowestPrice?
        lowestPrice = min(lowestPrice, price)

    print(maxProfit)
    return maxProfit

assert maxProfit([7,1,5,3,6,4]) == 5
assert maxProfit([7,6,4,3,1]) == 0
