"""
Given an non-empty array of integers `nums`, every element appears TWICE expect for one.
Find that single one.

You must implement a solution with linear runtime complexity and only use CONSTANT extra space.
"""

def singleNumberNaive(nums: list[int]) -> int:
    """
    Well this would be really easy if we just relax the constant extra space thing, right?
    """
    once = set()
    twice = set()
    for num in nums:
        if num in once:
            twice.add(num)
        else:
            once.add(num)
    
    return (once-twice).pop()

def singleNumber(nums: list[int]) -> int:
    """
    Now we have to do this without using extra space.... How could we possibly do this?
    Would sorting help? Imagine you had 11224 ; would that make things easier? Yeah! Then we can just scan across and compare neighbors.
    But wait, we can only do LINEAR runtime complexity and only use CONSTANT extra space...
    The only sorting algorithm that runs in linear that I KNOW is something like counting sort, which takes linear space.

    What can we do in linear time?
    - We can add up all the numbers 41212 -> 10, but I'm not sure that this helps us.
    
    Cheating:
    The "trick" to this "crackhead" problem is XOR. It requires bit manipulation

    [4, 1, 2, 1, 2]

    4 ---> ...100
    1 ---> ...001
    2 ---> ...010
    1 ---> ...001
    2 ---> ...010

    See above that only the leftmost column has an odd number of 1s
    So when we XOR them all together, we'll just get back 100, which happens to be the answer.
    """
    acc = nums[0]
    for num in nums[1:]:
        acc = acc ^ num
    return acc


for fn in (singleNumberNaive, singleNumber):
    assert fn([2,2,1]) == 1, f"{fn}: 221"
    assert fn([4,1,2,1,2]), f"{fn}: 41212"
