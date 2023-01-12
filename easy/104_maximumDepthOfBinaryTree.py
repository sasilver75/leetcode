from __future__ import annotations
from typing import Optional

"""
Given the ROOT of a binary tree, return its MAXIMUM DEPTH
A binary tree's maximum depth is the number of nodes along the longest path 
from the root node down to the farthest leaf node.
"""


class BSTNode:
    def __init__(self, value: int, left: Optional[BSTNode] = None, right: Optional[BSTNode] = None):
        self.value = value
        self.left = left
        self.right = right


def max_depth(root: BSTNode):
    return max_depth_helper(root, 0)


def max_depth_helper(root: BSTNode, depth: int):
    """"""
    if not root:
        return depth
    return max(max_depth_helper(root.left, depth + 1), max_depth_helper(root.right, depth + 1))


# Case 1:
r = BSTNode(3)
n2 = BSTNode(9)
n3 = BSTNode(20)
n4 = BSTNode(15)
n5 = BSTNode(7)
r.left = n2
r.right = n3
n3.left = n4
n3.right = n5
print(max_depth(r))  # 3

# Case 2:
r = BSTNode(1)
n2 = BSTNode(2)
r.right = n2
print(max_depth(r))  # 2
