"""
Find Duplicate Number

Given an array of integers `nums` containing n+1 integers where each
integer is the range [1, n] inclusive

There is only ONE REPEATED NUMBER in nums -- return this repeated number!

You must solve this proble without modifying the array nums, and using only
constant extra space (O(1))

Note: All of the integers in nums appear only once, except for precisely one
integer, which appears two or more times.
"""


def find_duplicate_naive(nums: list[int]) -> int:
    # Simple O(N^2) search for duplicate number
    for source_idx in range(len(nums)):
        for check_idx in range(source_idx + 1, len(nums)):
            if nums[source_idx] == nums[check_idx]:
                return nums[source_idx]
    # Should never hit here

"""
How can we do better?
There's something that we can do in O(N)/O(1), as long as we can modify the input.
We pretty much "reuse" the space that we're already given.

TLDR:
When we encounter nums[i] = 2, we set nums[2] = -nums[2]
So we flip the sign at the index of of "seen" numbers. This takes advantage
of the fact that all of the numbers are in the range 1..n,and the array size is n+1,
meaning that all of the numbers start as positives. 

[1, 3, 4, 2, 2]

"""
def find_duplicate(nums: list[int]) -> int:
    answer = None
    for idx, num in enumerate(nums):
        # Determine the index we should look at, given the value in nums @ idx
        target_index = abs(num)

        # Have we already seen this number?
        if nums[target_index] < 0:
            print("TI: ", target_index)
            answer = target_index # We could return here, but we wont, because we want to clean up the mutated data.
            break

        # Otherwise, set it to negative
        nums[target_index ] *= -1

    # At the end, we can "fix" the array, if we wanted to
    for idx in range(len(nums)):
        nums[idx] = abs(nums[idx])

    print(answer)
    return answer

def test(fn):
    assert fn([1, 3, 4, 2, 2]) == 2
    assert fn([3, 1, 3, 4, 2]) == 3


# test(find_duplicate_naive)
test(find_duplicate)
