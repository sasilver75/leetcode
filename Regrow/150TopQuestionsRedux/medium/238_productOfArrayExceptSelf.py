"""
Product of Array Except Self

Given an integer array NUMS, return an array ANSWER such that
ANSWER[i] is equal to hte product of all of the elements of NUMS
except NUMS[i]

The product of any prefix or suffix of nums is guaranteed to
fit in a 32-bit integer.

You must write an algo that runs in O(N) time, and without
using the division operation.
"""

"""
Naive options you might think of:
1. O(N^2), doing an O(N) product for each index
    - This will work! 
2. O(N), trying to get a sum of the entire list, and then for each element 
diving the list product by the element.
    - This will NOT WORK if there are any 0s in the list!
    - If there is a single zero in the list, then that zero will still have a 
value in the resulting array. If there are two zeroes, then this would work fine.

"""


def product_except_self_naive(nums: list[int]) -> list[int]:
    ans = []
    for ignore_idx in range(0, len(nums)):
        acc = 1
        for idx in range(0, len(nums)):
            if idx != ignore_idx:
                acc *= nums[idx]
        ans.append(acc)
    print(ans)
    return ans


"""
How can we be smarter?
- We can precompute two different lists: "Prefix" and "Suffix"
    - Where Prefix[i] is the product of numbers BEFORE idx i in nums  
    - Where Suffix[i] is hte product of numbers AFTER idx i in nums

"""


def product_except_self(nums: list[int]) -> list[int]:
    print(f"{nums = }")

    prefix_sums = []
    prefix_sums.append(1)  # For prefix, append a 1 before, and don't consider the last
    acc = 1
    for num in nums[:-1]:
        acc *= num
        prefix_sums.append(acc)
    print(f"{prefix_sums = }")

    suffix_sums = []  # For a postfix, append a 1 after, and don't consider the first el
    acc = 1
    for num in nums[-1:0:-1]:
        acc *= num
        suffix_sums.append(acc)
    suffix_sums = suffix_sums[::-1]
    suffix_sums.append(1)
    print(f"{suffix_sums = }")

    answer = []
    for i in range(len(prefix_sums)):
        answer.append(prefix_sums[i] * suffix_sums[i])
    return answer

# -------------
def test(fn):
    nums = [1, 2, 3, 4]
    assert fn(nums) == [24, 12, 8, 6]

    nums = [-1, 1, 0, -3, 3]
    assert fn(nums) == [0, 0, 9, 0, 0]


test(product_except_self_naive)
test(product_except_self)
