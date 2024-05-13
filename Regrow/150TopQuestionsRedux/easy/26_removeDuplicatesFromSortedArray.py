"""
26 Remove Duplicates from Sorted Array

Given an integer array `nums` sorted in non-decreasing order, remove the duplicates IN PLACE such that each unique element appears only once.
The relative order of elements should be kept the same.

"""


"""
I think the idea is to maintain two pointers, where there's a slow "base" pointer and a "seek" pointer that's faster.

At every iteration, seek moves forward.
We check whether the number @ seek is in our set of numbers that we've already observed.
    If it isn't, we swap (or just overwrite, really) the value @ base with teh value @ seek
    Whenever we swap, we move base forward one.
    
So base is always at the next insertion location, and seek is out front looking for the next unique value to insert @ the seek location.

Let's use an example of [1,1,2]
    
    b               {}
    1   1   2
    s
    
    SWAP - Advance Base and Seek
    
        b               {1}
    1   1   2
        s
    
    No swap needed - Advance Seek
    
        b               {1}
    1   1   2
            s
            
    SWAP - Advance Base And Seek
    
            b               {1, 2}
    1   2   2
                 s
    
    Terminate from Seek == len(nums)
    

"""
def remove_duplicates(nums: list[int]) -> int:
    seek, base = 0, 0
    seen = set()

    while seek < len(nums):
        if nums[seek] not in seen:
            nums[base] = nums[seek]
            base += 1

        seen.add(nums[seek])

        seek += 1

    return base




nums = [1,1,2]
assert remove_duplicates(nums) == 2
assert nums[:2] == [1,2]

nums = [0,0,1,1,1,2,2,3,3,4]
assert remove_duplicates(nums) == 5
assert nums[:5] == [0,1,2,3,4]
