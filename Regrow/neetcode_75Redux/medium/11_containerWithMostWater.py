"""
Container with Most Water
- Given an integer array height of length n.
- There are n vertical lines drawn such that two endpoints of the ith line are (i, 0) and (i, height[i])
- Find two lines that together with teh x axis form a container, such that the container contains the msot water.
- Return the maximum amount of water that a container can store.

Note that you may not sland the container.
See picture here: https://leetcode.com/problems/container-with-most-water/


Constraints:
n == height.length
2 <= n <= 10^5  (There will always be at least two elements in the list)
0 <= height[i] <= 10^4
"""

"""
Thinking:
The idea of this one is t
"""

def most_water_naive(heights: list[int]) -> int:
    """A Naive O(N^2) Solutoin"""
    max_volume = -float('inf')
    for left in range(len(heights)):
        for right in range(left+1, len(heights)):
            width = right - left
            height = min(heights[left], heights[right])
            volume = width * height
            max_volume = max(max_volume, volume)
    return max_volume


"""
Can we do it in less than O(N^2) time?
Well because the relative orderings of the heights are important, I doin't think there's some NLogN solution where we'll be sorting it.
How bout an O(N) solution?

If we start at a reasonable starting point (like let's say the furthest-apart heights)... and then iteratively, greedily "close in" one of the two sides of the container.
Which side of the container should we pick? Well we'd like to retain the higher of the two of them, in hopes that we'll find a higher one to pair with.
"""
def most_water(heights: list[int]) -> int:
    left, right = 0, len(heights) - 1
    max_volume = -float('inf')
    while left < right:
        # Assess Current Volume
        width = right - left
        height = min(heights[left], heights[right])
        volume = width * height

        # Update Current Volume
        max_volume = max(max_volume, volume)

        # Move the lesser of the two posts inwards
        if heights[left] <= heights[right]:
            left += 1
        else:
            right -= 1

    return max_volume


def test(fn):
    assert fn([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert fn([1, 1]) == 1

test(most_water_naive)
test(most_water)