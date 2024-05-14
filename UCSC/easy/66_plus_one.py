"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
 

Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.
"""

def plus_one(nums: list[int]) -> list[int]:
    """
    Note that the digits here are ordered from most significant to least significant, just like our usual numbers

    So it's all about adding to the rightmost number and letting that cascade (iteratively or recurrently) along to the right
    If there's still a carry at the end, we don't have to do this in-place, so we can just plop our resulting list into a [1].extend(nums)
    """

    carry = 0
    idx = len(nums) - 1
    nums[idx] += 1

    while idx >= 0:
        nums[idx] += carry
        if nums[idx] >= 10:
            carry = 1
            nums[idx] -= 10
        else:
            carry = 0
        idx -= 1
        
    if carry:
        return [1, *nums]
    return nums

        
assert plus_one([1,2,3]) == [1,2,4]
assert plus_one([4,3,2,1]) == [4,3,2,2]
assert plus_one([9]) == [1,0]
