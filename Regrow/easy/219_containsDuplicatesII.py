"""
Given an integer array NUMS and an integer K, return TRUE if there are
two DISTINCT indices i and j in the array such that nums[i] == nums[j]
and abs(i-j) <= k

Sam: In other words, two equal elements in nums that are at most k distance
from eachother.
"""

"""
Thinking:

The dumbeest thing we could do would be to, for each element in nums, which
let's say is length n, look at the next k elements (if possible) for a matching
number. This would require looking at ~nk elements, which would be O(n^2) in the 
case where k >= n. 


Okay, so the idea of "k" distance from eachother makes 
me think of a span of a list, moving a cross the list. I think another
way of putting that would be a sliding window of length/size k.

We keep track of the elements that are currently in the window.
We want to be able:
    1) Remove the "oldest" element from the window
    2) Add the "newest" element to the window
    3) Efficiently determine if the just-added-to-window number is already seen in the window.
    
1 and 2 feel like a doubly linked list to me
3 feels like a set to me
I could definitely maintain both of them... But do I really 
need to maintain a whole linked list? It's more like just two 
pointers that I need to keep track of, a lead and a back pointer.
"""


def contains_duplicates(nums: list[int], k: int) -> int:
    if not nums:
        return False

    # Phase 1: Expand Window, growing window_set and checking
    seen = set()
    for num in nums[0:k + 1]: # Safe even if k > len(
        if num in seen:
            return True
        seen.add(num)

    # If we didn't see
    if k > len(nums):
        return False

    # Establish Indexes
    left = 0
    right = k  # Check: Should this be k? k - 1?

    # Phase 2: Slide/Inchworm da Window, shrinking/growwing window_set and checking
    while right < len(nums) - 1:
        seen.remove(nums[left])
        left += 1
        right += 1
        to_add = nums[right]
        if to_add in seen:
            return True
        seen.add(to_add)

    return False


assert contains_duplicates([1, 2, 3, 1], 3) == True
assert contains_duplicates([1, 0, 1, 1], 1) == True
assert contains_duplicates([1, 2, 3, 1, 2, 3], 2) == False
