"""
Contains Duplicate

Given an integer array nums, return true if any value appears at lease TWICE
in teh array, and return FALSE if every element is distinct.
"""

"""
Thinking: 

O(N) time and O(N) space
An easy solution would be to use a hashset to keep track of seen values --
 when we come across a value that's already been seen, we return True.

O(NlogN) time and O(1) space
If we wanted to use O(1) space, we could do an in-place, mutative sort of the input
numbers, and then do a linear scan, looking at adjacent values to see if there are
any repeats (duplicates), returning True if so.

O(N) time and O(1) space
This is where it's like "how could we possibly do this?"
Which is when we need to think about tricky bit manipulation stuff.
Let's look at an example of four numbers:

101
111
101
001

There's probably some bitwise shit we could do here, right
"""


def contains_duplicate(nums: list[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


assert contains_duplicate([1, 2, 3, 1]) == True
assert contains_duplicate([1, 2, 3, 4]) == False
assert contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True
