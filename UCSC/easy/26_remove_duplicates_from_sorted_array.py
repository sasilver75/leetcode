"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
 The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially.
 The remaining elements of nums are not important as well as the size of nums.

 Return k.
"""

from os import remove


def removeDuplicates(nums: list[int]) -> int:
    """
    It's easiest if we just use some additional memory to keep track of the elements
    Because rmoving an element frmo the middle of a list is an o(N) operation, we'd rather append it (O(1) to some new ordered collection
    Because we want to be able to keep track of membership of this new collection, we use a hashset
    """
    seen = set()
    without_duplicates = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            without_duplicates.append(num)
    return without_duplicates


assert removeDuplicates([1,1,2]) == [1,2]
assert removeDuplicates([0,0,1,1,1,2,2,3,3,4]) == [0,1,2,3,4]
