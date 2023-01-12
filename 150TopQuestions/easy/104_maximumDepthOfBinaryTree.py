from __future__ import annotations
from typing import Optional

"""
Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from
the root node down to the farthest leaf node.
"""


class Node:
    def __init__(self, value: int, left: Optional[Node] = None, right: Optional[Node] = None):
        self.value = value
        self.left = left
        self.right = right


def maximum_depth(node: Node) -> int:
    if not node:
        return 0
    return 1 + max(maximum_depth(node.left), maximum_depth(node.right))


# Case 1
"""
            3
        9       20
             15     7
"""
root = Node(3, Node(9), Node(20, Node(15), Node(7)))
assert maximum_depth(root) == 3

# Case 2
"""
            1
                2
"""
root = Node(1, None, Node(2))
assert maximum_depth(root) == 2
