"""
Container with Most Water

Given an integer array height of length n
Ther are n vertical lines drawn such that the two endpoitns of the ith line are (i, 0), and (i, height[i])
Find two lines that together with the x axis form a container such that the contain contains the most water

Return the maximum amount of water a container can store

Notice that you may not slant the container
"""


def biggest_container_naive(heights: list[int]) -> int:
    biggest_container = 0

    # How to determine container volume
    def get_container_volume(left: int, right: int):
        return (right - left) * min([heights[left], heights[right]])

    # Compare each N^2 pair of left/rights, keeping track of the biggest container
    for left in range(len(heights) - 1):
        for right in range(left + 1, len(heights)):
            biggest_container = max(biggest_container, get_container_volume(left, right))

    return biggest_container

"""
How can we do better than O(N^2)?
The relative positioning of the heights is important to preserve, so I don't think sorting is an option for an O(NLogN) solution.
Is there a way to do it in O(N) time?

Are there any notable characteristics of the problem?
The volume = width * height relationship obviously indicates that we care both about the distance between pillars as well as the minimum height of two pillars...

Let's assume that we start with the widest container possible, which feels like a good starting point for "most volume".
In order for a thinner container to have MORE volume, then the thinner container has to have a HIGHER height.
So given that we have a left, right at [0, len(heights) - 1], if we want to appraise a thinner container, which pointer should we move?
    -> We should move the one with the smaller current height, because that gives us the possibility of having a higher, thinner container.

Let's do this while l < r, keeping track of the maximum container volume.
"""
def biggest_container(heights: list[int]) -> int:
    l, r = 0, len(heights) - 1
    max_vol = 0
    while l < r:
        # Consider current volume
        vol = (r - l) * min([heights[l], heights[r]])
        max_vol = max(max_vol, vol)

        # Move the lower of the two pointers towards the center
        if heights[l] <= heights[r]:
            l += 1
        else:
            r -= 1
    return max_vol


def test(fn):
    assert fn([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert fn([1, 1]) == 1

test(biggest_container_naive)
test(biggest_container)