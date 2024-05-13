from __future__ import annotations
from typing import Optional

"""
Convert Sorted Array to Binary Search Tree

Given an integer array `nums` where the elements are sorted in ascending order, convert it to a height-balanced binary search tree!

    -> A height balanced binary search tree is a tree in which the height of the left and right subtree of any node differs by not more than 1
"""


class Node:
    def __init__(self, value: int, left: Optional[Node] = None, right: Optional[Node] = None):
        self.value = value
        self.left = left
        self.right = right


def sorted_array_to_bst(nums: list[int]) -> Optional[Node]:

    def helper(l: int, r: int) -> Optional[Node]:
        """
        Where l and r are the inclusive indices of where we can select from
        """
        # Base Case: There aren't any nodes to consider remaining
        if l > r:
            return None
        # Base Case: We're looking at a leaf node
        if l == r:
            return Node(nums[l])

        mid_idx = l + (r - l)//2
        node = Node(nums[mid_idx])
        node.left = helper(l, mid_idx - 1)
        node.right = helper(mid_idx+1, r)

        return node

    mid_idx = len(nums)//2
    root = Node(nums[mid_idx])
    root.left = helper(0, mid_idx - 1)
    root.right = helper(mid_idx+1, len(nums)-1)

    return root




"""
                0
        -3              9
    -10             5
    
or

                0
        -10             5
            -3              9
    
From [-10, -3, 0, 5, 9]
"""
ans = sorted_array_to_bst([-10, -3, 0, 5, 9])
print(ans) # This is the second option from the answers

"""
            3                   1
        1            or              3
        
        from [1,3]
"""
ans = sorted_array_to_bst([1, 3])
print(ans) # This is the first option from the answers
