"""
Increasing Triplet Subsequence

Given an integer array `nums`, return `true` IF THERE EXISTS a triple of
indices [i, j, k] such that i < j < k and nums[i] < nums[j] < nums[k].

If no such indices exist, return `false`
"""
from typing import Optional

"""
Thinking:

This is just asking if there's a length-3 subsequence that's increasing-only, right?
i < j < k just implies "ordering, though not necessarily contiguous", to me.

The brute solution I think is straightforward:
Generate all length-3-subsequences, and check if any are increaing-only.
"""


def increasing_triplet_brute(nums: list[int]) -> bool:
    # Stage 1: Generate all length-3 subsequences
    subsequences = []

    def helper(idx: int = 0, built: Optional[list[int]] = None):
        if not built:
            built = []
        if len(built) == 3:
            subsequences.append(built)
            return
        if idx >= len(nums):
            # Exhausted nums without building a length-3 subsequence
            return

        # Either include or don't include the current num
        num = nums[idx]

        helper(idx + 1, [*built, num])
        helper(idx + 1, built)

    helper()

    def is_increasing(ss: list[int]):
        # Given a length-3 subsequence, is it STRICTLY increasing?
        for i in range(len(ss) - 1):
            if not (ss[i] < ss[i + 1]):
                return False
        return True

    return any(
        is_increasing(ss)
        for ss in subsequences
    )


"""
How can we do better than 2^N?

We could do N^3, which is better?
For each i in N, we could do a double-loop behind i, looking for two 
increasing numbers under nums[i].
"""


def increasing_triplet_n3(nums: list[int]) -> bool:
    for left in range(0, len(nums)):
        for middle in range(left + 1, len(nums)):
            for right in range(middle + 1, len(nums)):
                if nums[left] < nums[middle] < nums[right]:
                    return True
    return False


"""
THIS ACTUALLY DOESNT WORK!
"""
def increasing_triplet(nums):
    low, res = float('inf'), [float('inf'), float('inf')]
    for i in range(len(nums)):
        if nums[i] > res[-1]: return True
        if nums[i] > low: res = [low, nums[i]]
        low = min(low, nums[i])
    return False


"""
THIS ACTUALLY DOESNT WORK!
"""
def increasingTriplet(nums):
    # This fails on [4,5,1,6], thinking that it's true while it should be false
    first, second = float('inf'), float('inf')
    for n in nums:
        if n <= first:
            first = n
            second = float('inf')
        elif n <= second:
            second = n
        else:
            print("TRUE: ", first, second, n)
            return True

    print("FALSE: ", first, second)
    return False


def test(fn):
    assert fn([1, 2, 3, 4, 5]) == True
    assert fn([5, 4, 3, 2, 1]) == False
    assert fn([2, 1, 5, 0, 4, 6]) == True  # (3, 4, 5), for instance
    assert fn([4, 5, 1, 2, 3]) == True
    assert fn([4, 5, 1, 6]) == False
    assert fn([4, 5, 3, 6, 7]) == True
    assert fn([3, 6, 4, 6]) == True
    assert fn([3, 3, 4]) == False
    assert fn([3, 3, 4, 0, 1, 2]) == True
    assert fn([4,2,5,3,0]) == False
    assert fn([1,2,0,3])


# test(increasing_triplet_brute)  # Works :) 2^N
# test(increasing_triplet_n3)  # Works :) N^3
# test(increasingTriplet)
test(increasing_triplet)