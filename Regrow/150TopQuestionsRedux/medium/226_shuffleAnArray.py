"""
384 Shuffle an Array

Given an integer array nums, design an algorithm to randomly shuffle the array

All permutations of the array should be equally likely as a result of the shuffling

Implement the Solution class:
    - Solution(int[] nums) initializes the object with integer array nums
    - int[] reset() resets hte array ot its original configuration, and returns it
    - int[] shuffle() Returns a random shuffling of the array
"""
import random


class Shuffler:
    def __init__(self, nums: list[int]):
        self.original = nums.copy()
        self.nums = nums.copy()

    def reset(self) -> list[int]:
        self.nums = self.original.copy()
        return self.nums

    """
    Ideas of how to do this:
    My Idea: For every index, select a random swapindex from the list, and swap the elements.
        - Is this inappropriate? Does this in any way bias earlier indexes?
        - I don't think so?
        - Unfortunately, this actually isn't quite random, I don't think
        
    Algorithm: Fisher-Yates Shuffle
    - Effectively puts all elements int oa hat, and continually determines the
    next element by randomly drawing an element from the hat until no elements remain
    - This returns an unbiased permutation; every permutation is equally likely
    """

    # WARNING: NOT RANDOM
    # def shuffle(self) -> list[int]:
    #     for target_index in range(len(self.nums)):
    #         swap_index = random.randint(0, len(self.nums)-1)
    #         self.nums[target_index], self.nums[swap_index] = self.nums[swap_index], self.nums[target_index]
    #     return self.nums

    """
    Fisher Yate Algorithm:
    Effectively puts all elements int oa hat, and continually determines the
    next element by randomly drawing an element from the hat until no elements remain
    
    Given an index, the remaining "hat" elements are [index...end]
    This is why it's important to swap the elements, not just overwrite the target_idx -- we
    want to make sure that the element @ target_idx is still in the hat, if it wasn't selected
    to be the source element itself.
    """
    def shuffle(self) -> list[int]:
        for target_idx in range(len(self.nums)):
                source_index = random.randint(target_idx, len(self.nums)- 1)
                self.nums[target_idx], self.nums[source_index] = self.nums[source_index], self.nums[target_idx]
        return self.nums
