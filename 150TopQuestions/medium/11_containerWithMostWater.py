"""
Container with Most Water

You are given an integer array HEIGHT of length N. There are N vertical lines drawn such that
the two endpoints of the ith line are (i,0) and i(height[i])

Find two lines that together with the x axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

See picutres: https://leetcode.com/problems/container-with-most-water/
"""
from typing import Callable

"""
This sort of reminds me of the max stock price one, in a way... is that possible?
Let's do the dumb solution first in O(N^2) time
"""


def max_area_brute(heights: list[int]) -> int:
    if len(heights) < 2:
        return 0

    max_area = 0

    for i in range(len(heights)):
        for j in range(i + 1, len(heights)):
            height = min(heights[i], heights[j])
            width = j - i
            area = height * width

            max_area = max(max_area, area)

            j += 1

    return max_area


"""
Can we do better than O(N^2)?
What information would we need to keep track of?

What strategies might there be? Sliding/expanding window? Dynamic Programing? Two Pointers?

What's the best "pair" height that any given height could work with? 
Is the answer the tallest one? Nope - that's not enough to know that you've got the max.
Is it the one that's at least as tall as you are and maximally far away? Not necessarily either...

What data could we keep track of?
"""

"""
Intuition:
1. The widest container (using i=0 and j=len(heights)-1) could be a good candidate, because of its width.
Its water level is the height of the smaller of the two heights[i]/heights[j].
2. All other container are going to be less wide -- so we'll need a higher water level in order to hold
more water.
3. Therefore the smaller of the two current heights should be removed from further consideration.

Using two pointers and then greedily shrinking the container on the side with a shorter line.
"""




def max_area_two_pointers(heights: list[int]) -> int:
    # O(N) with two pointers, greedily shrinking the container
    i, j = 0, len(heights) - 1
    max_area = 0
    while i < j:
        length = j - i
        height = min(heights[i], heights[j])
        area = length * height
        max_area = max(max_area, area)

        if heights[i] <= heights[j]:
            i += 1
        else:
            j -= 1

    return max_area


"""
But: Why does this O(N) solution above obviously work?

How another user understood it:
1. Check areas from largest widths to lowest widths... Initiate the first area with the only possible
option of hte largest width.
2. The area for the next smaller width cannot increase UNLESS the minimum height of our last largest area increases.
3. Move the pointer associated with the min height
4. We now know the maximum area for max_width and max_width-1, and just repeat this process until we reach 1 width.
"""

# https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg

# -- Test --
def test(fn: Callable):
    assert fn([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert fn([1, 1]) == 1

test(max_area_brute)
test(max_area_two_pointers)
