"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
 The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
 The remaining elements of nums are not important as well as the size of nums.

Return k.

"""

from os import remove


def remove_element_naive(nums: list[int], val: int) -> list[int]:
    """
    So given a non-sorted list, we need to remove all occurrence of val
    That means that we necessarily need to check every element in the sequence, so we're not goign to be doing any better than O(N) in terms of time complexity
    If we modify the same list, we're going to be doing (worst case) O(N) as we iterate through the list, and shift

    So we should probably try to make just a single pass without deleting in-place, which would require us to use some additional memory.
    We don't need to check for any membership in the new list, just make a comparison using the current element in our initial iterable and the target valu
    """
    new = []
    for num in nums:
        if num != val:
            new.append(num)
    print(new)
    return new

def remove_element(nums: list[int], val: int) -> list[int]:
    """
    I just think it's interesting that the person said that we didn't necessarily have to return the values in order.
    This isn't going to be any faster, but we could do something like:
    """
    # Could also use the collecitons.Counter to do this, or a defaultdit
    acc = {}
    for num in nums:
        if num not in acc:
            acc[num] = 0
        acc[num] += 1
    
    # Now we have counts of each element
    new = []
    for num, count in acc.items():
        new.extend([num]*count)
    
    print(new)
    return new


"""
OOPS
I totally misread the instructions, where we're supposed to remove all occurrences of val IN PLACE by moving those elemnts to the front
of the list!
nums = [0,1,2,2,3,0,4,2], val = 2
becomes something like nums = [0,1,4,0,3,_,_,_]
"""

def remove_element_correct(nums: list[int], val: int) -> list[int]:
    """
    We're going to do this by basically moving "good" elements to the front of the list, and keeping track of the number of 
    "good" elements that we've seen.
    We hve a base pointer starting at idx 0, and another that seeks forward linearly at every step
    If our seeking pointer finds a number that's NOT target, we move it to base, and increment base 
    (then, as usual, we increment seek)
    """
    base = 0
    seek = 0
    # Walk seek across
    while seek < len(nums):
        seek_num = nums[seek]
        if seek_num != val:
            nums[base] = seek_num
            base += 1
        seek += 1
        print(nums)
    return nums


# These are actually corect, I just didn't want to write the test.
for fn in [remove_element_correct]:
    assert fn([3,2,2,3], 3)[0:2] == [2,2], f"{fn.__name__} bad 1"
    assert fn([0,1,2,2,3,0,4,2], 2)[0:5] == [0,1,4,0,3], f"{fn.__name__} bad 2"
