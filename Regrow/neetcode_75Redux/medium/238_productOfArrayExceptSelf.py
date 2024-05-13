"""
Product of Array Except Self (Medium)

- Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]
- The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer
- You must write an algorithm that runs in O(N) time and without using the division operation
"""

"""
Ways of going about this:
1. For every element in nums, scan the entire list and get the product of every other element O(N^2)
2. [WRONG, WON'T WORK]: Get the product of the entire list, and for each element, divide the product by the element
    - This won't work because there can be zeroes in the list. This actually DOES work for 2+ zeroes, but not for just one zero
3. Generate a "Prefix Sums" list and a "Suffix Sums" list 
"""


def product_of_array_except_self_naive(nums: list[int]) -> list[int]:
    acc = []
    for base_index in range(len(nums)):
        product = 1
        for idx in range(len(nums)):
            if idx != base_index:
                product *= nums[idx]
        acc.append(product)
    return acc


def product_of_array_except_self(nums: list[int]) -> list[int]:
    prefix = [1]  # Note that these have to have 1's on the end
    for idx in range(1, len(nums)):  # [_, b, c, d]
        prefix.append(prefix[-1] * nums[idx - 1])

    suffix = [1]
    for idx in range(len(nums) - 2, -1, -1):  # [a, b, c, _]
        suffix.append(suffix[-1] * nums[idx + 1])
    suffix.reverse()

    print(f"{nums = }")
    print(f"{prefix = }")
    print(f"{suffix = } \n")

    return [p * s for p, s in zip(prefix, suffix)]


def test(fn):
    assert fn([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert fn([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]


test(product_of_array_except_self_naive)
test(product_of_array_except_self)
