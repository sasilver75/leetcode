"""
Partition Equal Subset Sum

Given a non-empty array `nums` containing ONLY POSITIVE INTEGERS, find if
the array can be PARTITIONED into TWO SUBSETS such that the sum of
elements in both subsets is equal.

Question: Do partitions need to be contiguous? No, they do not.
"""
from typing import Callable, Optional

"""
Insight: This question is pretty much the same as saying:
Can you construct SOME SINGLE SUBSEQUENCE that has a sum that's exactly HALF 
of the sum of the ENTIRE subsequence!
We can brute force that, I think.

Note that we know that all of the numbers will be positive, so we can stop
when our current sum is > half. 
"""


"""
            
[1, 5, 11, 5] --> Target: 11
            
                0
        1               0
    6       1       5       0
  17 6    12  1   16 5    [11] 0
  
Since every level of our tree has two choices (include or not), and we have
to make a decision for every element in the list, we'll have a 2^N complexity
if we do this brute force method.
"""

def partition_equal_subset_sum_brute(nums: list[int]) -> bool:
    numsum = sum(nums)
    if numsum // 2 == 1: # An odd number can't be evenly divided between two subsets sums of positive integers
        return False

    target = numsum / 2

    def helper(sum: int = 0, idx: int = 0):
        if sum == target:
            return True
        if sum > target or idx == len(nums):
            return False

        # Either include or don't include the current number. 2^N
        return helper(sum+nums[idx], idx + 1) or helper(sum, idx + 1)

    return helper()

"""
Okay, but can we do any better than O(2^N) time complexity?

nums=[1, 5, 11, 5] --> Target: 11
            
                0
        1               0
    6       1       5       0
  17 6    12  1   16 5    [11] 0

Is there any repeated work being done here?
Say we're at i=0 in the list of nums, and we choose to include 1.

Now, we're at i=1, with a Target of 10! (and we're looking at the [1...end] subarray
If we were to cache this, our new subproblem would be i=1,Target=10
Or if we hadn't taken 1 at i=0., our new subproblem would be i=1, Target=11

What are the dimensions of our cache going to be? n * (Sum(nums)/2)
This is basically going to be our Big O time complexity: O(N * Sum(nums))

This is usually going to be better than 2^N performance.

Decision Tree --> Look for Repeated Work --> Introduce Caching --> Think DP
"""

"""
DP SOlution

[1, 5, 11, 5] Target=11

Let's say we were starting at the i=0 value, and we knew all of hte possible
sums that any given subset of the remainder of the array ([5, 11, 5]) would make.
For every single one of those sums, we could add our current number (1) to it,
and check whether (subarraysum + num) == Target.

This is basically the way htat we're going to do it for the bottom-up solution.
Starting at the back:

[1, 5, 11, 5]
           ^
Starting at the end, the sums we can create are 0 or 5.
We'll store these in a set.
Set = {0, 5}
Next, we'll go to 11:
[1, 5, 11, 5]
        ^
And iterate through every single one of the items in Set, and ask:
* Candidate = 11 + {setElement}
* Candidate == Target?"
* Add Candidate to Set

And continue iterating backwards.
"""

def dp_solution(nums: list[int]) -> bool:
    sums = set([0])
    target = sum(nums) / 2
    if target // 2 == 1:
        return False

    for i in range(len(nums) - 1, -1, -1):
        num = nums[i]
        for past_sum in sums.copy(): # We can't change the size of a set as we iterate over it. Making a copy helps!
            candidate = past_sum + num
            if candidate == target:
                return True
            sums.add(candidate)

    return False


# -- Test Zone --
def test(fn: Callable):
    assert fn([1, 5, 11, 5])
    assert fn([1, 2, 3, 5]) == False


test(partition_equal_subset_sum_brute)
test(dp_solution)
