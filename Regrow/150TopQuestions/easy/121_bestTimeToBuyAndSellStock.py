"""
Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a stock
on a given day.

You want to maximize your profit by choosing a single day ot buy
one stock and choosing a different day in the future to sell that stock!

Return the MAXIMUM profit that you can achieve from this transaction.
If you cannot achieve any profit, return 0.
"""


def best_time_to_buy_and_sell_dumb(nums: list[int]) -> int:
    """
    Logic: What if I looked at every price in nums and asked:
    "If I bought now, what's the best (highest) price I could sell this at
    in the future? Is the profit resulting from that better than my max profit?"
    This will be an O(N^2) time algo, since each price needs to be compared to
    all subsequent prices.
    """
    max_profit = 0
    for idx, buy_price in enumerate(nums):
        for sell_price in nums[idx + 1:]:
            profit = sell_price - buy_price
            max_profit = max(max_profit, profit)
    return max_profit


assert best_time_to_buy_and_sell_dumb([7, 1, 5, 3, 6, 4]) == 5
assert best_time_to_buy_and_sell_dumb([7, 6, 4, 3, 1]) == 0


def best_time_to_buy_and_sell(nums: list[int]) -> int:
    """
    Logic: Instead of doing it in O(N^2), can we possibly do it in one pass?
    (It wouldn't make sense otherwise to sort the numbers).
    Instead of asking "What if I bought here", what if we asked "What if I sold here?"
    If we did that, what information would we want to keep track of given that we
    want to know the maximal profit that we could attain if we sold at the current time?
    We'd want to keep track of the previous "best purchase price," which is the minimum
    price possible in the past!
    """
    lowest_buy_price = nums[1]
    max_profit = 0
    for i in range(1, len(nums)):
        # Consider: What if we sold here?
        current_price = nums[i]
        profit = current_price - lowest_buy_price

        max_profit = max(max_profit, profit)  # Update: Max Profit?
        lowest_buy_price = min(lowest_buy_price, current_price)  # Update: Min Lowest Buy Price

    return max_profit

assert best_time_to_buy_and_sell([7, 1, 5, 3, 6, 4]) == 5
assert best_time_to_buy_and_sell([7, 6, 4, 3, 1]) == 0
