"""
Maximum Product Subarray (Medium)

Given an integer array nums, find a subarray that has the largest product, and return the product
"""

"""
Ways to approach this:
1. Generate all subarrays, and find the one with the largest product
2. The problem with a smarter solution to this one is that a negative times a negative is a positive, but a negative times a positive is a negative.
So given that you have some negative number that you're considering, should you "extend" the previous subarray by making it (perhaps negative), without
knowing if there's some future negative that will make it positive again?

[2, 3, -4, 6, -3]
Given the above, -4 doesn't "know" that -3 is coming up. It either has to pick -4 and -24 .
Given a previous number of -24, 6 has to choose whether to become -144 or to become 6

I think it's important here to realize that there are two things: Magnitude and Direction (pos/neg)
What we want at the end is the highest POSITIVE magnitude

Along the way, we don't know which Direction our current magnitude will go...
I think what I'm suggesting is that we keep at every element the [lowest, highest] number that we could create, using a combination
of { currentNumber and [prevLowest, preHighest] }

So it'd be like

prevLowest, prevHighest = running
candidates = [currentNumber * prevLowest, currentNumber * prevHighest, currentNumber?] Does currentNumber belong here? 
running = [min(candidates), max(candidates)]

And then at the end, returning prevHighest (or the max in running)
"""


def max_product_naive(nums: list[int]) -> int:
    max_product = -float('inf')
    for starting_index in range(len(nums)):
        product = 1
        for current_index in range(starting_index, len(nums)):
            product *= nums[current_index]
            max_product = max(max_product, product)
    return max_product


def max_product(nums: list[int]) -> int:
    max_profit = -float('inf')
    running = [1, 1]  # lowest, highest

    for num in nums:
        lowest, highest = running
        candidates = [lowest * num, highest * num, num]  # Consider the case nums=[-2,6]; we need this here
        max_profit = max(max_profit, max(candidates))
        running = [min(candidates), max(candidates)]

    print(max_profit)
    return max_profit


def test(fn):
    assert fn([-2, 6]) == 6
    assert fn([2, 3, -2, 4]) == 6  # 2, 3
    assert fn([-2, 0, -1]) == 0


for fn in [
    # max_product_naive,
    max_product
]:
    test(fn)
