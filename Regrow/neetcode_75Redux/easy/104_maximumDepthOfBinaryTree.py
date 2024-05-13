from __future__ import annotations
from typing import Optional

"""
Given the root of a binary tree, return its MAXIMUM DEPTH

A binary tree's maximum depth is the number of nodes along
the LONGEST PATH from the root node down to the farthest
leaf node.
"""
class Node:
    def __init__(self, value: int, left: Optional[Node] = None, right: Optional[Node] = None):
        self.value = value
        self.left = left
        self.right = right

""""
Literally use any sort of tree traversal method,
keeping track of the deepest level that we've reached.
So you just have to keep track of the level that you're at,
and whenever you're at a leaf node, update the max_depth
"""

def maximum_depth(root: Optional[Node]) -> int:
    max_depth = 0

    # Doing iterative DFS
    node_stack = []
    if root:
        node_stack.append((root, 1))

    while node_stack:
        node, depth = node_stack.pop()

        # Are we at a leaf node? Update max depth
        if node.left is None and node.right is None:
            max_depth = max(max_depth, depth)
            continue

        if node.left:
            node_stack.append((node.left, depth+1))
        if node.right:
            node_stack.append((node.right, depth+1))

    return max_depth


root = Node(3, Node(9), Node(20, Node(15), Node(7)))
assert maximum_depth(root) == 3

root = Node(1, None, Node(2))
assert maximum_depth(root) == 2