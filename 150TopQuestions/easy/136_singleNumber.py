"""
Single Number

Given a non-empty array of integers nums, every element appears TWICE
except for one! Find that single one.

You must implement a solution with a LINEAR O(N) runtime complexity,
and only use CONSTANT O(1) extra space!
"""

"""
Thinking:

The easy way of doing this would be to keep something like a dic of counts
of each letter, and then scan through the dict at the end and choose the one 
with a count of 1. But we can't do that, since that'd be O(N) memory.

If we're going to maintain a linear runtime complexity, we won't be able to 
sort the items.

So what data do we need to keep track of? Data that doesn't grow as n does...

Alternatively... What other O(N) options are there?
Two pointers scanning from each side? I don't see how that would help.

What's the TRICK here? Let's look at some numbers...

4   1   2   1   2

Yeah, it doesn't see like there's an obvious one.
Which is when we should start thinking ways of tricky/devilish ways.

That makes me think of bit manipulation
Let's look at the bit versions of the numbers above

100
001
010
001
010

If we XOR these numbers together, we should get 100 back!
"""


def single_number(nums: list[int]) -> int:
    acc = nums[0]
    for num in nums[1:]:
        acc = acc ^ num
    return acc


assert single_number([2, 2, 1]) == 1
assert single_number([4, 1, 2, 1, 2]) == 4
assert single_number([1]) == 1
