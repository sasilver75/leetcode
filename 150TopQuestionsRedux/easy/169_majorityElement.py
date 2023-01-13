"""
Majority Element

Given an array `nums` of size `n`, return the majority element.
The majority element is the element that appears more than floor(n/2) times

You may assume that the majority element ALWAYS exists in the array.
"""
import collections
import math


def majority_element_naive(nums: list[int]) -> int:
    limit = len(nums) // 2
    counts = collections.defaultdict(int)
    for num in nums:
        counts[num] += 1
        if counts[num] > limit:
            return num

    print("Uh Oh!")

"""
Can we do it in constant space?
Because the previous solution was O(N), O(N)

There's an O(N)/O(1) algorithm called the Boyer-Moore majority vote algorithm
GIVEN that there IS some majority element, this will find it in O(N)/O(1) time

The algo maintains in its local variables:
    - A sequence element
    - A counter
It processes the elements of the sequence, one at a time.
When processing an element x, 
    if the counter is zero: 
        the algorithm  stores x as its remembered sequence element and sets the counter to one.
    else:
        compares x to the stored element, and either incremenets the counter (if they're equal) or decrements the counter (otherwise)

At the end of hte program, the sequence has a majority -- it's the element stored by the algorithm!

"""
def majority_element(nums: list[int]) -> int:
    majority_element = nums[0]
    count = 1
    for i in range(1, len(nums)):
        num = nums[i]
        if count == 0:
            majority_element = num
        elif num == majority_element:
            count += 1
        else:
            count -= 1
    return majority_element


def test(fn):
    assert fn([3,2,3]) == 3
    assert fn([2,2,1,1,1,2,2]) == 2
    assert fn([3,3,3,2,2,1,3]) == 3

test(majority_element_naive)
test(majority_element)