"""
4Sum II

Given FOUR integer arrays `nums1`, `nums2`, `nums3`, `nums4` all of length n,
return the NUMBER of tuples (i, j, k, l) such that:

0 <= i, j, k, l <= n     (they are valid indices)
and
nums1[i] + nums2[j] + nums3[k] + nums4[l]           (that sum to 0)

"""


def for_sum_count_naive(nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
    # O(N^4)
    ways = 0
    for i in nums1:
        for j in nums2:
            for k in nums3:
                for l in nums4:
                    if i + j + k + l == 0:
                        ways += 1
    return ways

"""
Can we do better?

I thought for a second that I could do some sort of binary searching
thing on the other integer arrays, but A they aren't sortd and B even if they
were there are multiple possible pairings of numbers...

Can I preprocess the nums into some other data structure? 
What would make this problem easier?
What makes this problem harder than two-sum?
How do we solve two-sum again?
"""
def two_sum_naive(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
# print(two_sum_naive([2,7,11,15], 9))

def two_sum_smart(nums: list[int], target:int) -> list[int]:
    complements = {
        target - num: idx
        for idx, num in enumerate(nums)
    }
    for idx, num in enumerate(nums):
        if num in complements:
            return [idx, complements[num]]
# print(two_sum_smart([2,7,11,15], 9))


"""
Okay, back to our actual problem...
What would make this four-sum problem easier?
I mean, why is it hard? :) Because there are four lists!
Is there any way that we can combine these lists to make our lives easier?

Let's combine nums1 and nums2 into dict of:
{
   elementSum: [index1, index2]
}

and do the same thing for num3 and nums4

Then we can iterate through every element in nums1num2 product and look
for the complement in nums3nums4 product, similar to what we did in twoSum!


The calculation of nums1nums2 product is O(N^2)
The calculation of nums3nums4 product is O(N^2)

We then scan across one of these and look for the complement in the other O(N^2)

So this all boils down to simply O(N^2), instead of O(N^4)!
"""

def four_sum_count(nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
    nums1nums2sum = {}
    for idx1, num1 in enumerate(nums1):
        for idx2, num2 in enumerate(nums2):
            sum = num1+num2
            nums1nums2sum[sum] = [idx1, idx2]

    nums3nums4sum = {}
    for idx3, num3 in enumerate(nums3):
        for idx4, num4 in enumerate(nums4):
            sum = num3 + num4
            nums3nums4sum[sum] = [idx3, idx4]

    # Counts Ways that the two dicts can be combined
    ways = 0
    for sum, indices in nums1nums2sum.items():
        complement = 0 - sum # "target" - sum
        if complement in nums3nums4sum:
            ways += 1

    return ways

    # There is guaranteed to be an answer, apparently, so nothing further should be needed


def test(fn):
    assert fn(
        [1, 2],
        [-2, -1],
        [-1, 2],
        [0, 2]
    ) == 2  # (0,0,0,1), (1,1,0,0)  [indices]

    assert fn(
        [0],
        [0],
        [0],
        [0],
    ) == 1  # (0,0,0,0)

# test(for_sum_count_naive)
test(four_sum_count)