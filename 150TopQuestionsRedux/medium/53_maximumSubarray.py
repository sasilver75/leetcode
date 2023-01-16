"""
Maximum Subarray

Given an integer arrays nums, find the subarray with teh largest sum, and return its sum
"""

def mss_naive(nums: list[int]) -> int:
    if not nums:
        raise ValueError("Nums must be a list with length at least one")
    # Generate every subarray (Note that we could take subarray sums here as we go, and not even accumulate the subarrays)
    subarrays = []
    for starting_index in range(len(nums)):
        for ending_index in range(starting_index, len(nums)):
            subarrays.append(nums[starting_index: ending_index+1])

    mss = -float('inf')
    for sa in subarrays:
        mss = max(mss, sum(sa))
    return mss

"""
How can we do better than O(N^2)?
The thing to realize here is that subarrays are contiguous portions of teh array.... and we'd want to extend any existing subarray as long as its subarray sum is GREATER than 0!
So we can do it in a single pass
"""
def mss(nums: list[int]) -> int:
    max_running = nums[0]
    running = nums[0]
    for i in range(1, len(nums)):
        num = nums[i]
        running = max(0, running+num)
        max_running = max(max_running, running)
    return max_running


def test(fn):
    assert fn([1,2,3]) == 6
    assert fn([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert fn([1]) == 1
    assert fn([5,4,-1,7,8]) == 23

test(mss_naive)
test(mss)