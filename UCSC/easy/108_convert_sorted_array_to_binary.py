"""
Given an integer array `nums` where the elements are sorted in ASC order, convert it to a height-balanced BST

A height-balanced binary tree is a binary tree in which the depth of the two subtrees 
of every node never differs by more than one.
"""

import math
from typing import Optional


class Node:
    def __init__(self, value: int, left: Optional['Node'], right: Optional['Node']) -> None:
        self.value = value
        self.left = left
        self.right = right


def sorted_array_to_bst(nums: list[int]):
    """
    Recall the rules of a Binary SEARCH Tree (BST)
    1) Every element in n's left subtree is <= the element in node n
    2) Every element in n's right subtree is >= the element in node n

    [-10, -3, 0,  5, 9]
    becoming
            0
        -3      9
    -10       5

    At least in this example, we chose to MIDDLE VALUE (By index)
    as the midpoint; as a result, we've got 2 nodes on either side

    So if we place 0

            0

    Then consider each side:
    [-10, -3]  and  [5, 9]


    See what to do?

    So we need a function that, given an array, creates a node for the center element
    Then sets node.left to the recurse(leftArray) and node.right to be recurse(rightArray), right?
    Base case being an empty list, I hope
    """

    def helper(nums: list[int]) -> Optional[Node]:
        if not nums:
            return None
        
        center_idx = math.floor(len(nums)/2)

        node = Node(
            nums[center_idx],
            helper(nums[:center_idx]),
            helper(nums[center_idx+1:])
        )

        return node

    return helper(nums)


case1 = sorted_array_to_bst([-10,-3,0,5,9])
case2 = sorted_array_to_bst([1,3])
print("Yay!") # Worked

                                            

    




