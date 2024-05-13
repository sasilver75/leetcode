"""
Given an integer array nums, return an array answer such that
answer[i] is equal to the product of all of the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer

*** You must:
 - write an algorithm that runs  in O(N) time
 - WITHOUT using division operation (/)


"""


def productOfArrayExceptSelfBrute(nums: list[int]) -> list[int]:
    # O(N^2)
    def prodOfExcept(idx: int) -> int:
        acc = 1
        for i in range(len(nums)):
            if i != idx:
                acc *= nums[i]
        return acc

    return [prodOfExcept(i) for i in range(len(nums))]


"""
Thinking:

Given an integer array `nums`, return an array `answer` such that answer[i]
is equal to the product of all elements of nums except nums[i]

[1,2,3,4]   -> (TotalProd:24)
[24,12,8,6]

I notice from the examples...
* If there's ONE zero in nums, then everything is answer is 0 besides the 
index with a 0 in nums, which has (numsProduct) init.
* If there are MORE THAN ONE zeroes in nums, I assume the entire answers list should be zeroes
* If there are NO zeroes, then everything is nums[i]/numsProduct

We have to do this in O(N) time too.

INSIGHT:

[1,2,(3),4,5]           (totalProduct: 120)

Say we're considering the index 2, containing the value (3).
We'd like to do 120/3=40, but we can't do division.
What we CAN DO is take the sum of all of the numbers BEFORE this number,
and the sum of all of the numbers AFTER this number.

That can be two arrays that we generate ahead of time!
Call them `prefix` and `suffix`
`prefix`: The product of all values UP TO AND INCLUDING this index's value.
`suffix`: The product of all values INCLUDING AND AFTER this index's value.
"""


def productOfArrayExceptSelf(nums: list[int]) -> list[int]:
    # Generate "prefix" list
    prefix = []
    acc = 1
    for num in nums:
        acc *= num
        prefix.append(acc)

    # Generate "suffix" list
    suffix = []
    acc = 1
    for num in nums[::-1]:  # Could do this with constant memory easily too.
        acc *= num
        suffix.append(acc)
    suffix = suffix[::-1]

    # Generate "answer" list
    answer = []
    for idx in range(0, len(nums)):
        before = prefix[idx - 1] if idx - 1 >= 0 else 1
        after = suffix[idx + 1] if idx + 1 < len(nums) else 1
        answer.append(before * after)

    return answer


def test(fn):
    assert fn([1, 2, 3, 4]) == [24, 12, 8, 6]  # Prefix: [1, 2, 6, 24], Suffix: [24,
    assert fn([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]


test(productOfArrayExceptSelfBrute)
test(productOfArrayExceptSelf)
