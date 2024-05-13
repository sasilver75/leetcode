"""
Maximum Product Subarray

Given an integer array `nums`, find a subarray that has the largest product,
and return the product.

The test cases are generated such that the answer will fit in a 32-bit integer
"""


"""
Let's just generate all of the subarrays, and then take the maximum product
of each.

Recall that a subarray is an ordered, contiguous "part" of the list
"""
def max_product_subarray_naive(nums: list[int]) -> int:
    subarrays = []
    for starting_index in range(len(nums)):
        for ending_index in range(starting_index, len(nums)):
            subarrays.append(nums[starting_index: ending_index+1])

    def product(nums: list[int]) -> int:
        acc = 1
        for num in nums:
            acc *= num
        return acc

    max_product = max(product(subarray) for subarray in subarrays)
    return max_product



"""
How can we be a little more smart about this, rather than doing O(N^2)?

Does knowing subproblems help us out with this?
What if we had a 1-dimensional dynammic programming table where

dp[i] = maximum product subarrray starting at idx i in nums
"""
def max_product_subarray(nums: list[int]) -> int:
    dp = [0]*len(nums)
    for idx in range(len(dp)-1, -1, -1):
        dp[idx] = max([
            nums[idx],
            nums[idx] * dp[idx+1]
        ]) if idx+1 < len(nums) else nums[idx]

    return max(dp)



def test(fn):
    assert fn([2, 3, -2, 4]) == 6
    assert fn([-2, 0, -1]) == 0

test(max_product_subarray_naive)
test(max_product_subarray)
