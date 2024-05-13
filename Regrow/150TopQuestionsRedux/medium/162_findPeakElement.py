"""
Find Peak Element

A peak element is an element that is STRICTLY GREATER than its neighbors

Given a 0-indexed integer array nums, find a peak element, and return
its INDEX. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -INF
In other words, an element is always considered to be strictly greater than a
neighbor that's outside the array.

You must write an algorithm that runs in O(logn) time!
"""

"""
How should we do this?

Given that we're returning an index, we need to preserve the relative
ordering on the elements, so sorting I think is out of the question.

I think we're down to a binary search here... 


An element is either:
1) On an uphill  /
2) On a downhill  \
3) The beginning of a high plateau /_
4) The end of a high plateau _\
5) The beginning of a low plateau \_
6) The end of a low plateau  _/
6.5) Flat ___
7) A peak  /\
8) A valley  \/

Let's say we have 

[1, 2, 1, 3, 5, 6, 4]

We select the middle element
[1, 2, 1, (3), 5, 6, 4]

What can we say about the middle element?
Okay... this one happens to be on an uphill, and that happens to be the "right"
way to look...

But imagine we had:

[1, 9, 1, (3), 5, 6, 4]

In this case, the same logic would lead us down the wrong path.
I'm going to lightly assert that there isn't a way that we can tell
which direction the peak is by just looking locally at a single element.

But at the same time, we can't preprocess the list into any other sort of list,
because that would take O(N) time. So... we have to somehow binary search on this!

Oh fuck!

THe instructions say: "find a peak element", not find "THE" peak element

So we just need to move in the direction of "uphill", in the case of clean
uphill or downhill

There's another big in the instructions that's important as well:
nums[i] != nums[i + 1] for all valid i.
That means that there AREN'T any flat parts! Amazing!

That turns this into an easy binary search problem: Find any peak in 
a list that can't have repeating numbers (Flat parts)!
"""


def findPeakElement(nums: list[int]) -> int:
    def get_adjacents(idx: int) -> tuple[int, int, int]:
        val = nums[idx]
        left = nums[idx - 1] if idx - 1 >= 0 else -float('inf')
        right = nums[idx + 1] if idx + 1 < len(nums) else -float('inf')
        return left, val, right

    def is_peak(idx: int):
        left, mid, right = get_adjacents(idx)
        return left < mid > right

    def is_uphill(idx: int):
        left, mid, right = get_adjacents(idx)
        return left < mid < right

    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2

        if is_peak(mid):
            return mid

        if is_uphill(mid):
            l = mid + 1
        else:
            r = mid - 1

    raise ValueError("There's no peak!")


def test(fn):
    """
               O
             OOO
            OOOOO
    """
    assert fn([1, 2, 3, 1]) == 2

    """
                 O
                OO
                OOO
               OOOO
             O OOOO
            OOOOOOO
                             /\
                            /  \
                           /    \
                    /\    /    
             /\    /  \  /      
          /\/  \/\/    \/  
    """
    assert fn([1, 2, 1, 3, 5, 6, 4]) == 5


test(findPeakElement)
