from __future__ import annotations
from typing import Optional
"""
Binary Tree Paths
Given hte ROOT of a binary tree, return all ROOT-TO-LEAF
paths in ANY ORDER

A LEAF is a node with no children
"""

"""
Intuition:
1) helper(node, list = [])
2) If current node is None, append list to a master_list
3) 
"""


class Node:
    def __init__(self, value: int, left: Optional[Node] = None, right: Optional[Node] = None):
        self.value = value
        self.left = left
        self.right = right

def paths(root: Node) -> list[str]:
    master_paths = []

    def helper(node: Node, built_path: list[int]):
        # At a leaf node? Add the built path to master_paths
        if not node.left and not node.right:
            master_paths.append([*built_path, node.value])
            return
        # Recurse Left if possible
        if node.left:
            helper(node.left, [*built_path, node.value])
        # Recurse Right if possible
        if node.right:
            helper(node.right, [*built_path, node.value])

    helper(root, [])

    return [" -> ".join([str(val) for val in path]) for path in master_paths]

# Case 1
head = Node(1, Node(2, None, Node(5)), Node(3))
print(paths(head))

# Case 2
head = Node(1)
print(paths(head))