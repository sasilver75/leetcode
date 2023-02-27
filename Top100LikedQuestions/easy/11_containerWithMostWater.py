"""
Container with Most Water

Given an integer array HEIGHT with length n
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i])
Find two lines that together with the Y axis form a container that contains the most water
Return the maximum amount of water a container can hold
"""

def most_water_naive(heights: list[int]) -> int:
    # Consider every pair of heights in O(N^2) time
    max_cap = 0
    for left_height_idx in range(len(heights)):
        for right_height_idx in range(left_height_idx+1, len(heights)):
            width = right_height_idx - left_height_idx
            height = min(heights[left_height_idx], heights[right_height_idx])
            cap = width * height
            max_cap = max(max_cap, cap)

    return max_cap

def most_water(heights: list[int]) -> int:
    # Start with the widest pair of poles, and move the poles closer to eachother, moving the shorter of the two poles.
    l, r = 0, len(heights) - 1
    max_cap = 0
    while l < r:
        width = r - l
        height = min(heights[l], heights[r])
        cap = width * height
        max_cap = max(max_cap, cap)

        if heights[l] <= heights[r]:
            l += 1
        else:
            r -= 1

    return max_cap





def test(fn):
    assert fn([1,8,6,2,5,4,8,3,7]) == 49
    assert fn([1,1]) == 1

# test(most_water_naive)
test(most_water)



