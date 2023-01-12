from __future__ import annotations
from typing import Optional
"""
Convert Sorted Array to Binary Search Tree

Given an integer array nums where the elements are sorted in ASCENDING order,
convert it to a HEIGHT-BALANCED binary search tree!

A height-balanced binary tree is a binary tree in which the depth of the
two subtrees of every node never differs by more than one.
"""
class Node:
    def __init__(self, value: int, left: Optional[Node] = None, right: Optional[Node] = None):
        self.value = value
        self.left = left
        self.right = right

"""
Thinking :)

Given [-10, -3, 0, 5, 9]

What if we picked 0 as the middle node, because it's the middle value of the list?

                0

And maybe we recurse on the left side of the array from 0  ([-10, -3]) to populate
the left side of the tree.

root.left = recursive([-10, -3])
root.right = recursive([5,9])
                0



"""

def convert_array(nums: list[int]) -> Node:
    if not nums:
        return None

    middle_idx = len(nums) // 2
    mid_node = Node(nums[middle_idx])

    mid_node.left = convert_array(nums[0:middle_idx])
    mid_node.right = convert_array(nums[middle_idx+1:])

    return mid_node


# Case 1
"""
            0            or         0
        -3      9               -10     5
      -10      5                   -3     9
      
"""
# Solution #1 above
root = convert_array([-10, -3, 0, 5, 9])

# Case 2
"""
        3       or      1
    1                       3
"""
# Solution 1 above
root = convert_array([1, 3])