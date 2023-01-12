"""
Peak Index in a Mountain Array

An array `arr` is a MOUNTAIN if the following properties
hold:

- arr.length >= 3
- There exists some i with 0 < i < arr.length - 1 (NOT an end index)
such that:
    * arr[0] < arr[1] < ... < arr[i-1] < arr[i]
    * arr[i] > arr[i+1] > ... > arr[arr.length - 1]

Meaning:
        /\
      /   \

Given a mountain array, return the index of the peak

You must solve it in log(arr.length) time complexity
"""


def peakIndexInMountainArray(arr: list[int]) -> int:
    l, r = 0, len(arr)-1

    while l <= r:
        mid_idx = l + (r - l) // 2
        mid_val = arr[mid_idx]

        left_neighbor = arr[mid_idx-1] if mid_idx-1 >= 0 else -float('inf')
        right_neighbor = arr[mid_idx+1] if mid_idx+1 < len(arr) else -float('inf')

        # We know that we're strictly either ascending or descending, and that there's only one peak:
        if left_neighbor < mid_val > right_neighbor:
            return mid_idx
        elif mid_val > left_neighbor:
            # ASC: Look Right
            left = mid_idx + 1
        else:
            right = mid_idx - 1

    return -1




def test(fn):
    assert fn([0, 1, 0]) == 1
    assert fn([0, 2, 1, 0]) == 1
    assert fn([0, 10, 5, 2]) == 1

test(peakIndexInMountainArray)