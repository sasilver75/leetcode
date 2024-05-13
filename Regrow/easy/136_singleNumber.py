"""
Given NON-EMPTY array of INTEGERS nums, every element appears TWICE
except for one. Find that single one.

You must implement a solution with O(N) time and O(1) space complexity.
"""

"""
Thinking:
Okay the easy way would be have a onceSeen and a twiceSeen set, or something, and do a lienar scan, then
do the disjoint of the two sets. But this takes O(N) space

Or you could sort in place and scan across -- the one with only different numbers on both sides
would be the one we're looking for. But this takes O(nlong) time.

What sort of information can we keep track of as we scan across?
Do we need to do more than one scan?
Is the fact that other numbers appear TWICE (rather than "more than once") of any interest?
"""

"""
Cheating:
The "trick" to this "crackhead" problem is XOR. It requires bit manipulation

[4, 1, 2, 1, 2]

4 ---> ...100
1 ---> ...001
2 ---> ...010
1 ---> ...001
2 ---> ...010

See above: Only the left column (4) has one bit in a column! The other two colums have an event number (matching) 1-bits 

XOR
1 ^ 0 == 1
0 ^ 1 == 1
1 ^ 1 == 0
0 ^ 0 == 0
So only if they're different -- exclusive or

What we really do here is to take the XOR of each of these
The order that you do the XOR operation in is not important

"XOR of any two numbers gives the difference of bit as 1 and the same bit as 0
Thus, 1 ^ 1 == 0 because the same numbers have the same bits.
So we will always get the single unique element because lal the same ones will evaluate to 0 and 0 ^ single = single
The order doesn't matter. In other words, the XOR operation is commutative."
"""

def single_number(nums: list[int]) -> int:
    result = 0
    for n in nums:
        result = n ^ result
    return result


# Case 1
assert single_number([2, 2, 1]) == 1
assert single_number([4, 1, 2, 1, 2]) == 4
assert single_number([1]) == 1
