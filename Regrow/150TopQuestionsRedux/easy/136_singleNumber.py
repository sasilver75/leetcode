"""
Single Number

Given a non-empty array of integers `nums`, every element appears TWICE except for one.
Find that single one.

You must implement a solution that has LINEAR runtime complexity, using
only constant extra space.
"""

"""
You should see this and consider that it seems to pretty pretty difficult to
do, which should be a tip-off that it's probably a bitwise operation.

Say that a list included the numbers 3, 5, 3
In binary, these would be

0011   <- 3
0101   <- 5
0011   <- 3

If use use Bitwise XOR (^), reducing across the list of numbers, what would we get?

3 ^ 5
  0011
  0101
= 0110

And that that {result} ^ 3 again
  0110
  0011
= 0101  <--- Hey, that's our 5 again!

So we just do a reduce/fold across the numbers, using bitwise or as the operation
"""


def single_number(nums: list[int]):
    acc = nums[0]
    i = 1
    while i < len(nums):
        acc = acc ^ nums[i]
    return acc


assert single_number([2, 2, 1]) == 1
assert single_number([4, 1, 2, 1, 2]) == 4
assert single_number([1]) == 1
