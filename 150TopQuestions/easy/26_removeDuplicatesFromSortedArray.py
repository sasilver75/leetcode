"""
Remove Duplicates from Sorted Array

Give an integer array nums sorted in NON-DECERASING ORDER,
remove the duplicates in-place such that each unique element appears only once!
The relative order of the elements should be kept the same.

Since it's impossible to change the length of the array in some languages,
you must instead have teh result be placed in the FIRST PART of the array.

If you have k elements after removing the duplicates, then the first k elements
of nums should hold the final result. It doesn't matter what you leave beyond
the first k elements.

Return k after placing the final result in the first k slots of nums.
"""

"""
            2   i
    0   1   1   1   2
                    j
                    
                    
The idea is that you have two pointers -- a slow one, and fast one.

The slow one will be at the location where you will be shuffling the next
unique element to. 
The fast one will be ahead, tracking each candidate element up for consideration as a
unique element.

Since the list is sorted, what characterizes a unique element?
Well all of the numbers BEHIND i are both sorted and unique. So the candidate
number is unique if it's GREATER than the i-1'th element.
"""

def remove_duplicates(nums: list[int]) -> tuple[int, list[int]]:
    slow = 1
    fast = 1
    while fast < len(nums):
        if nums[fast] > nums[slow - 1]:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1

    return nums, slow



lst, idx = remove_duplicates([1, 1, 2])
assert lst[:idx] == [1, 2]

lst, idx = remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
assert lst[:idx] == [0, 1, 2, 3, 4]
