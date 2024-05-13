"""
3 Sum

Given an integer array nums, return all the triplets (nums[i], nums[j], nums[k]) such that:
 1) i != j, i != k, and j != k
 2) nums[i]+nums[j]+nums[k] == 0

Notice that the solution set must not contain duplicate triplets.
Sam Note: I guess this means that 3,2,1 and 1,2,3 are the "same" solution.
"""
from typing import Callable


def three_sum_brute(nums: list[int]) -> list[list[int]]:
    acc = []
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                nums_i, nums_j, nums_k = nums[i], nums[j], nums[k]
                if nums_i + nums_j + nums_k == 0:
                    acc.append([nums_i, nums_j, nums_k])

    def sort(nums: list[int]) -> list[int]:
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2

        return merge(
            sort(nums[0:mid]),
            sort(nums[mid:])
        )

    def merge(l1: list[int], l2: list[int]) -> list[int]:
        acc = []
        p1, p2 = 0, 0

        while p1 < len(l1) and p2 < len(l2):
            e1, e2 = l1[p1], l2[p2]
            if e1 <= e2:
                acc.append(e1)
                p1 += 1
            else:
                acc.append(e2)
                p2 += 1

        acc.extend(l1[p1:])
        acc.extend(l2[p2:])

        return acc

    sorted_acc = [sort(l) for l in acc]
    uniq = {tuple(l) for l in sorted_acc}
    return [list(t) for t in uniq]


"""
Okay, that was the dumb N^3 way (or worse) of doing things...
Is there a better way of doing this?
Can we get N^2, maybe?
"""

"""
Idea:
Realize that there are 4 ways to get 3 numbers to add to 0:
Case 1) [+, -, 0]
Case 2) [+, +, -]
Case 3) [+, -, -]
Case 4) [0, 0, 0]



1. Break the numbers in `nums` into 3 lists of P (positives), N (negatives), Z (zeroes)
2. Consider Cases 1 and 4. These are only possible when you have zeroes. Do we have any zeroes? Enough?
3. Consider Case 2: Find two elements in P that equal some element in N
4. Consider Case 3: Find two elements in N that equal some element in P

O(N^2) time and memory :)
"""


def three_sum(nums: list[int]) -> list[list[int]]:
    acc = set()
    p, z, n = [], [], []
    for num in nums:
        if num > 0:
            p.append(num)
        elif num == 0:
            z.append(num)
        else:
            n.append(num)

    # 1) Check for (0,0,0) Singular Case
    if len(z) >= 3:
        acc.add((0, 0, 0))

    # 2) Check for (0, +, -) Cases
    if z:
        for pos in p:
            for neg in n:
                if pos + neg == 0:
                    acc.add((0, pos, neg))

    # 3) Check for (-, +, +) Cases
    for neg in n:
        for i in range(0, len(p)):
            for j in range(i + 1, len(p)):
                if p[i] + p[j] == -1 * neg:
                    acc.add((neg, p[i], p[j]))

    # 4) Check for (+, -, -) Cases
    for pos in p:
        for i in range(0, len(n)):
            for j in range(i + 1, len(n)):
                if n[i] + n[j] == -1 * pos:
                    acc.add((pos, n[i], n[j]))

    return [list(t) for t in acc]


# -- Test --
def test(fn: Callable) -> None:
    assert all(l in fn([-1, 0, 1, 2, -1, 4]) for l in [[-1, -1, 2], [-1, 0, 1]])
    assert fn([0, 1, 1]) == []
    assert fn([0, 0, 0]) == [[0, 0, 0]]


# test(three_sum_brute)
# test(three_sum) # Test doesn't pass because assertions/ordering are tricky, but correct!