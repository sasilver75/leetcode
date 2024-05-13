"""
Best Time to Buy and Sell Stock II

You are given an integer array `prices` where `prices[i]` is the price
of a given stock on the `ith` day.

On each day, you MAY decide to buy and/or sell the stock!

You can only hold at most ONE share of the stock at any time.
However you can buy it and then immediately sell it on the same day.

Find and return the MAXIMUM profit you can achieve.

Sam: The change in this from the easy version of the question is that
you can buy and sell multiple times.
"""
from typing import Optional

"""
Thinking:
The way that we pursue the easier version of the problem is keeping track of 
the lowest past price we've seen, and then asking (at each element), "What profit
would I get if I sold that stock right now?"

So we were keeping track of the PastMinimumPrice and the CurrentPrice, to 
update the MaximumProfit.

Spitballing: What if we kept track of... pretty much TWO of those sets?
We keep track of the lowest two prices that we've seen?  And then keep track of the top two profits? Ehh
--> Oops -- It's possible that we buy and sell many times, not just twice! So we can't do a one-pass thing, I'm guessing?

How could we brute-force this?

At each index...

Assuming we don't hold stock, we could either:
1) Buy Stock
2) Not Buy Stock

Assuming we hold stock, we could either:
1) Sell Stock
2) Not Sell Stock

We can "end" the day holding stock (though it won't help us profit)
This would be 2^N
Let's try it!


"""


def max_profit_brute(prices: list[int]) -> int:
    max_profit = 0

    def helper(idx: int = 0, running_profit: int = 0, held_stock: bool = False) -> int:
        nonlocal max_profit
        if idx == len(prices):
            max_profit = max(max_profit, running_profit)
            return

        """
        Optimization Note: I don't think there needs to be specifically a "Buy or Don't Buy Stock", is there? Why would you not buy?
        Do we force a buy and then force liquidation at the last day? Is this needed anyways?
        You can buy and sell on the same day -- how does that fit in?
        """

        if held_stock:
            # Sell (at current price) or Don't Sell Stock
            helper(idx + 1, running_profit + prices[idx], False)
            helper(idx + 1, running_profit, True)
        else:
            # Buy (at current price) or Don't Buy Stock
            helper(idx + 1, running_profit - prices[idx], True)
            helper(idx + 1, running_profit, False)

    helper()

    return max_profit


"""
Neetcode Hint:

What's the algorithm to determine when we're going to buy and sell?
It's easier to see when you draw the prices as a graph.

Price
7        O
6        O               O
5        O       O       O    
4        O       O       O   O
3        O       O   O   O   O
2        O       O   O   O   O
1        O   O   O   O   O   O
    
    Days 0   1   2   3   4   5
    
We want to sell high, and buy low, right?
In other words, buy high, and sell low!

So we never sell on a "declining" price, right?
So we don't buy at 7, because it's (going to be) declining.

We BUY at local minima, and SELL at local maxima! 
A local minima is where idx-1 and idx+1 are both greater than idx
Inverse for local maxima

So we buy at 1, sell at 2 for profit of 4
We rebuy at 3, sell at 4 for a profit of 3

Really what we're doing looking at the graph is capturing every "increase"
in the stock price. That makes sense, given that we're omnipotently calculating
what the maximum profit would be for a god-tier trader!


Edge Cases:

4                    O
3        O           O
2        O   O   O   O
1        O   O   O   O
    
    Day  0   1   2   3
    
Do we buy on day 1 or day 2? It doesn't matter, but we have to pick one.
The same for the maximum choice of when to sell.

I'm going to prefer to buy the last of the flat section in each case.
"""


def max_profit(prices: list[int]) -> int:
    holding_stock = False
    profit = 0

    for idx, price in enumerate(prices):
        # Not holding stock? --> Buy Case: Buy the local minima [but don't buy the last price]
        if not holding_stock and idx < len(prices) - 1:
            # Consider sibling prices as very high if unavailable
            previous_price = prices[idx - 1] if idx - 1 >= 0 else float('inf')
            next_price = prices[idx + 1] if idx + 1 < len(prices) else float('inf')

            if previous_price >= price < next_price:  # If price is local maxima
                # print(f"Buy at {price}")
                holding_stock = True
                profit -= price

        # Holding stock? --> Sell Case: Sell the local maxima
        else:
            # Consider sibling prices as very low if unavailable
            previous_price = prices[idx - 1] if idx - 1 >= 0 else float('-inf')
            next_price = prices[idx + 1] if idx + 1 < len(prices) else float('-inf')

            if previous_price <= price > next_price:  # if price is local minima
                # print(f"Sell at {price}")
                holding_stock = False
                profit += price

    return profit


# -- Test Zone --

def test(fn):
    assert fn([7, 1, 5, 3, 6, 4]) == 7  # Buy on day2, sell on day3, THEN buy on day 4, sell on day 5
    assert fn([1, 2, 3, 4, 5]) == 4  # Buy on day 1 and sell on day 5
    assert fn([7, 6, 4, 3, 1]) == 0  # No way to make profit


# test(max_profit_brute)
test(max_profit)
