"""
Plus One

You are given a LARGE INTEGER represented as an integer array digits,
where each digits[i] is the ith digit of the integer.

The integers are ordered from most significant to least significant in
left-to-right order.
The large integer does not contain any leading 0s.

Increment the large integer by one and return th resulting array of digits!
"""


def increment_by_one(nums: list[int]) -> list[int]:
    acc = []  # You really could just update nums in place if you wanted to, but I'd rather be pure
    nums = nums[::-1]
    carry = 0
    nums[0] += 1  # Add one!
    for dig in nums:
        dig_sum = dig + carry
        carry = dig_sum // 10
        acc.append(dig_sum % 10)
    if carry:
        acc.append(carry)

    return acc[::-1]


assert increment_by_one([1, 2, 3]) == [1, 2, 4]
assert increment_by_one([4, 3, 2, 1]) == [4, 3, 2, 2]
