"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

def two_sum_naive(nums: list[int], target: int) -> list[int]:
    """
    Here's the dumbest way of doing it by doing N^2 iterations through nums, comparing to see if numbers add to target
    If they do, we stop our iteration by returning the indices at which we found a match.
    Sucecssive iterations don't benefit from eachother in any way, in this method.
    On the plus side, this doesn't require using any additional memory.
    """
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
    raise Exception(f"Naive: No pair found in {nums} targeting {target}")


def two_sum(nums: list[int], target: int) -> list[int]:
    """
    We can use a little moore memory O(N) by having a lookup of the numbers that we've accumulated.
    We can either store the complement of past nubmers or the past numbers themselves, it's just moving the math around.
    What's important is that we're storing {something to compare to} and {the past index with the interseting number}
    So whether it's {complement needed: index} or {number: index}, it doesn't matter

    Something to clarify: Should ([1,1,3],4) be [1,2] or should it be [0,2]? Unclear from the instructions, maybe it's clear from the 
    examples, but it's a good thing to ask. I'm going with [1,2] (the latest occurrence of matching numbers)
    """
    past = {}
    for idx, num in enumerate(nums):
        # What would this number's complement b, with respect to target?
        # This is number + x = target, so we find this by doing target - number
        complement = target - num
        
        # check for complement
        if complement in past:
            return [past[complement], idx]
        
        # otherwise log this number in past; if it already exists, we just update it to have the latest index of this number, which is fine, I think
        past[num] = idx

    raise Exception("Nope")
        



# -----
tests = (
    ([2,7,11,15], 9, [0,1]),
    ([3,2,4], 6, [1,2]),
    ([3,3], 6, [0,1])
)

for fns in two_sum_naive, two_sum:
    for nums, target, output in tests:
        assert two_sum(nums, target) == output
        print(f"{fns.__name__} Passed")


