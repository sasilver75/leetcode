"""
Maximum Product Subarray

Given an integer array nums, find the contiguous subarray within an array
(containing at least one number) which has the largest product.

Sam Note: Recall that a SUBARRAY (this problem) is a CONTIGUOUS part of an array AND
maintains relative ORDERING of elements. (Versus a Subsequence, which maintains ordering, but need not be contiguous)

Sam Note: It seems like we don't count length-1 arrays to be subarrays.
"""
from typing import Callable


# def generate_subarrays(nums: list[int]) -> int:
#     subarrays = []
#     for start in range(0, len(nums)):
#         for end in range(start, len(nums)):
#             subarrays.append(nums[start:end+1])
#     print(subarrays)
#
# generate_subarrays([1,2,3])


def maximum_product_subarray_brute(nums: list[int]) -> int:
    # Here's the dumbest way to do it -- generate every possible subarray, then determine the one with the minimum product!
    subarrays = []

    for start in range(0, len(nums)):
        for end in range(start + 1,
                         len(nums)):  # We don't count length-1 subarrays to be subarrays in this question, so start+1
            subarrays.append(nums[start:end + 1])

    # print(subarrays)

    max_product = -float('inf')
    for subarray in subarrays:
        product = 1
        for num in subarray:
            product *= num
        max_product = max(max_product, product)

    return max_product


"""
How can we be a little more intelligent? Can this be decomposed into smaller problems?
Before we were generating subarrays in O(N^2) and then doing O(N) work for each subarray, totaling O(N^3)

Can we cut that down to O(N^2)?
If we know what {some subarray product} is, then expanding that product by one value should be an O(1) 
operation of multiplying the new element by the subarray product, rather than doing a full O(N) scan again.
"""


def maximum_product_subarray(nums: list[int]) -> int:
    max_product = -float('inf')
    for start in range(0, len(nums)):
        product = 1
        for end in range(start, len(nums)):
            product *= nums[end]
            if end != start:  # We don't consider length-1 subarrays to be subarrays in this problem
                max_product = max(max_product, product)

    # print(max_product)
    return max_product


"""
Okay cool. That's how we should have done it in the first place, in O(N^2) time.
What about the actual DP solution?

It's not like we can start at the end and then choose whether to inlcude or not include
numbers... It's not like we have a window that we're growing and shrinking... do we?
The idea that it's contiguous is useful, maybe?...Like a window is contiguous. But as you're expanding
in one direction, there's not a way to know whether you'd end with a large negative or large positive number, right?
So you'd still have to expand the window to the max in each direction, assuming you don't hit a zero?

How can we do better? Are there any Patterns to this problem that will help us get 
a better solution than O(N^2)?

[1,2,3] <-- Notice something here? ALL ELEMENTS ARE POSITIVE. That means
that the maximum product subarray is going to be the WHOLE array. We can effectively
combine these elements into one element (1*2*3=6), if we wanted to, right?

[-1, -2, -3] <-- What about ALL NEGATIVE numbers? This is more tricky...
It has to be an even-length subarray, and in this case it's the [-2, -3] subarray.
When we have negatives consecutively, the product flips from positive/negative.

*** Even though we're looking for hte max product subarray, Neetcode says we're also
going to have to keep track of the MINIMUM. Why?

If we wanted to find the max product subarray of [-1, -2, -3]... it might be 
useful for us to solve the maxProductSubarray of [-1, -2]... and then use that
to get the entire one. We know that the max product subarray of that is 2.

But we have a [{2}, -3] -- that doesn't help, does it?
Let's ALSO get the MINIMUM PRODUCT SUBARRAY OF THESE FIRST TWO ELEMENTS AS WELL!
The MINIMUM product subarray sum of [-1, -2] is just -2 ([-2]).
So we have 2 and -2 as the Max/Min subarray products...

So now considering each of those 2(Max) and -2(Min) numbers, and considering
the NEXT number in the list (-3). 
When we multiple by the Max, we get 2 * -3 = -6. When we multiply by the Min,
we get -2 * -3 = 6. So now we can say for the [-1, -2, -3] range we can say
that the min is -6 and the max is 6. This is the answer we wanted!

Let's say the next number in the list were -4.
We would again do:
(-6, 6) * -4 = (24, -24) --> Min of -24 and Max of 24

But there IS an edge case... The dreaded ZERO value.
What if we had [-1, -2, -3, 0, 3, 5]?
The 0 is going to kill our min/max streak :( since {anything}*0 = 0, and 0*{anything} = 0

We're going to handle these in a different way...
Anytime we get to a Zero value, we're going to reset our Min/Max to 1/1
"""


def maximum_product_subarray_dp(nums: list[int]) -> int:
    maximum = nums[0] # Some number
    min_p, max_p = 1, 1
    for num in nums:
        if num == 0:
            min_p = 1
            max_p = 1
            maximum = max(maximum, num) # We want to "reset" our min_p/max_p, but 0 could possibly be still the maximum in the array by itself!
            continue

        a, b = min_p * num, max_p * num
        min_p = min(a, b, num)
        max_p = max(a, b, num)
        maximum = max(maximum, max_p)

    print(maximum)
    return maximum


def neetcode_solution(nums: list[int]) -> int:
    res = max(nums)
    curMin, curMax = 1, 1

    for num in nums:
        if num == 0:
            curMin, curMax = 1, 1
            continue

        tmp = curMax * num
        curMax = max(num * curMax, num * curMin, num)
        curMin = min(tmp, num * curMax, num)
        res = max(res, curMax)

    return res


# --- Test ---
def test(fn: Callable) -> None:
    assert fn([2, 3, -2, 4]) == 6  # [2,3] has the largest product 6
    assert fn([-2, 0, -1]) == 0  # The result cannot be 2, because [-2, -1] is not a subarray


test(maximum_product_subarray_brute)
test(maximum_product_subarray)
test(maximum_product_subarray_dp)
test(neetcode_solution)