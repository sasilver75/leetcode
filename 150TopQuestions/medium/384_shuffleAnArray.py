"""
Shuffle an Array

Given an integer array `nums`, design an algorithm to randomly shuffle the array!

All permutations of the array should be EQUALLY LIKELY as a result of the shuffling.
Implement the `Solution` class:

Solution(int[] nums) Initializes the object w the integer array `nums`
int[] reset() Resets the array to its original configuration and returns it
int[] shuffle() Returns a random shuffling of the array
"""
import random

"""
(Modernized) Fisher-Yates Shuffle
https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle

An alogrithm for generating a random permutation of a finite sequence.
Effectively puts all elements into a hat, and continually determines the next
element by randomly drawing an element from the hat until no elements remain.

This returns an UNBIASED Permutation -- every permutation is equally likely!
"""


class Solution:
    def __init__(self, nums: list[int]):
        # Be sure here to always copy the input list by value so that subequent mutations don't fuck you up.
        # also bakcup and nums need to refer to different lists by reference, if you're going to be changing nums
        self.backup = [*nums]
        self.nums = [*nums]

    def shuffle(self) -> list[int]:
        # Shuffle self.nums!
        for i in range(len(self.nums)):
            # Select a random element from indices [i...end] to be in position i
            swap_idx = random.randint(i, len(self.nums) - 1)
            self.nums[i], self.nums[swap_idx] = self.nums[swap_idx], self.nums[i]

        return self.nums

    def reset(self) -> list[int]:
        self.nums = self.backup
        return self.nums


# -- Test Zone --
def test():
    s = Solution([1, 2, 3])
    print(s.shuffle())
    print(s.reset())
    print(s.shuffle())


test()
