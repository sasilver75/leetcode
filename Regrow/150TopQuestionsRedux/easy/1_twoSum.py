"""
1. Two Sum

"""


def two_sum(nums: list[int], target: int) -> list[int]:
    enumerated_nums = list(enumerate(nums))
    num_lookup = {num: idx for idx, num in enumerated_nums}
    for idx, num in enumerated_nums:
        num_complement = target - num
        if num_complement in num_lookup and num_lookup[num_complement] != idx:
            print(idx, num_lookup[num_complement])
            return [idx, num_lookup[num_complement]]

"""
Note that hings like the last case will be "naturally" solved, because the hashtable is populated from left to right,
so the last occurrence of a given nmber is what will be present in the hashtable, and then we eagerly return, looking at numbers
from left to right if we see a match -- so if there were three occurrences of a number, the outermost occurrences are what 
would be returned.
"""

assert two_sum([2, 7, 11, 15], 9) == [0, 1]
assert two_sum([3, 2, 4], 6) == [1, 2]
assert two_sum([3, 3], 6) == [0, 1]
