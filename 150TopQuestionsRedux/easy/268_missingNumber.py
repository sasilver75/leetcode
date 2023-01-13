"""
Missing Number

Given an array `nums` containing `n` distinct numbers in the range `[0, n]`
Return the only number in the range that's missing from the array.
"""


def missing_number(nums: list[int]) -> int:
    # n = len(nums) # There's a number in the range [0...9] that isn't in nums: Find it!
    # O(N)/O(N) Solution
    nums = set(nums)
    possible_nums = set([n for n in range(0, len(nums) + 1)])
    ans = (possible_nums - nums).pop()
    print(ans)
    return ans



assert missing_number([3, 0, 1]) == 2
assert missing_number([0, 1]) == 2
assert missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
