from __future__ import annotations
from typing import Optional
"""
104
Maximum Depth of a Binary Tree

Given the `root` of a binary tree, return its maximum depth.

A binary tree's maximum depth is the NUMBER OF NODES along hte LONGEST PATH from the root node down to the further leaf node.

"""

class Node:
    def __init__(self, value: int, left: Optional[Node] = None, right: Optional[Node] = None):
        self.value = value
        self.left = left
        self.right = right


"""
It's a truth that we need to explore the entire tree in order to be able to determine the maximum depth/height of a node in it.
So just explore the tree in any manner that you'd like. 
"""
def maximum_depth(root: Optional[Node]) -> int:
    if not root:
        return 0

    maximum_height = 0

    def recursive_height_explorer(node: Node, height: int):
        """
        Only called on a valid Node and its height
        We could either update the maximum height at every node, or we could just do it when we reach a leaf node -- won't change the runtime complexity.
        """
        nonlocal maximum_height

        if not any([node.left, node.right]):
            maximum_height = max(maximum_height, height)
            return

        if node.left:
            recursive_height_explorer(node.left, height+1)
        if node.right:
            recursive_height_explorer(node.right, height+1)

    recursive_height_explorer(root, 1)
    return maximum_height


# -- Tets --

"""
            3
    9               20
                15      7
"""
root = Node(3, Node(9), Node(20, Node(15), Node(7)))
assert maximum_depth(root) == 3

root = Node(1, None, Node(2))
assert maximum_depth(root) == 2