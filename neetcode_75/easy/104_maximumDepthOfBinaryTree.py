from __future__ import annotations

import collections
from typing import Optional

"""
Maximum Depth of Binary Tree
Category: Tree

Given the `root` of a binary tree, return its MAXIMUM DEPTH!

A binary tree's maximum depth is the number of nodes along
the longest path from the root node down to the furthest leaf node.
"""


class Node:
    def __init__(self, value: int, left: Optional[Node] = None, right: Optional[Node] = None):
        self.value = value
        self.left = left
        self.right = right


def max_depth(root: Optional[Node]) -> int:
    if not root:
        return 0

    max_depth = 0
    def helper(node: Optional[Node], depth: int) -> None:
        nonlocal max_depth

        max_depth = max(max_depth, depth)

        if node.left:
            helper(node.left, depth+1)
        if node.right:
            helper(node.right, depth+1)

    helper(root, 1)
    return max_depth

def max_depth_dfs_iterative(root: Optional[Node]) -> int:
    # To do a DFS, append and pop from a list (stack)
    if not root:
        return 0

    max_depth = 0
    nodes = [(root, 1)]
    while nodes:
        node, depth = nodes.pop()
        max_depth = max(max_depth, depth)

        if node.right:
            nodes.append((node.right, depth+1))
        if node.left:
            nodes.append((node.left, depth+1))
    return max_depth


def max_depth_bfs_iterative(root: Optional[Node]) -> int:
    # To do a DFS, appendLeft and pop from a list (queue)
    if not root:
        return 0

    max_depth = 0
    nodes = collections.deque()
    nodes.appendleft((root, 1))
    while nodes:
        node, depth = nodes.pop()
        max_depth = max(max_depth, depth)
        if node.left:
            nodes.appendleft((node.left, depth+1))
        if node.right:
            nodes.appendleft((node.right, depth+1))

    return max_depth


# -- Test --
def test(fn):
    root = Node(3, Node(9), Node(20, Node(15), Node(7)))
    assert fn(root) == 3

    root = Node(1, None, Node(2))
    assert fn(root) == 2

test(max_depth)
test(max_depth_dfs_iterative)
test(max_depth_bfs_iterative)