"""
Maximum Subarray Sum
Category: Array

Given an integer array `nums`, find the subarray which
has the largest sum and return its sum!
"""


def maximum_subarray_naive(nums: list[int]) -> int:
    # Generate all subarrays
    subarrays = []
    for start in range(len(nums)):
        for end in range(start, len(nums)):
            subarrays.append(nums[start:end+1])

    # get max subarray sum
    return max(
        sum(sa) for sa in subarrays
    )

"""
How can we do better than O(N^2) time?
Can we do it in O(N) possibly?

Could we do it 1-D DP?
Or is there a greedy solution?

Insight: 
Subarrays are CONTIGUOUS.
Given an index, we can either:
    * Continue the last subarray
    * Begin a new subarray
    
When would we want to continue the previous subarray? When it's better than
the alternative, which is starting a new sum (subarray) at the current num!
"""

def maximum_subarray(nums: list[int]) -> int:
    max_sum = -float('inf')
    sum = 0
    for num in nums:
        sum = min(sum + num, num)
        max_sum = max(max_sum, sum)
    return max_sum



def test(fn):
    assert fn([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert fn([1]) == 1
    assert fn([5, 4, -1, 7, 8]) == 23

test(maximum_subarray_naive)