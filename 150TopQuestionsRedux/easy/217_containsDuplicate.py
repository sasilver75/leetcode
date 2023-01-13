"""
Given an integer array nums, return TRUE if any values appears AT LEAST TWICE
in the array, and return FALSE if every element is distinct.
"""

"""
Possible ways we could do this:
    - Linear Scan with Hashtable for seen elements, O(N)/O(N)
    - Sort in Place and linear scan, looking for identical neighbors O(NLogN)/O(1)
    - O(N)/O(1) solution?...
"""
def contains_duplicate_naive(nums: list[int]) -> None:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

def test(fn):
    assert fn([1,2,3,1])
    assert fn([1,2,3,4]) == False
    assert fn([1,1,1,3,3,4,3,2,4,2]) == True