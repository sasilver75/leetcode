from __future__ import annotations

import collections
from typing import Optional

"""
Binary Tree Zigzag Level Order Traversal

Given the `root` of a binary tree, return the ZIGZAG level order traversal
of its nodes values
(ie from left to right, then right to left for the next, and alternate
between)
"""


class Node:
    def __init__(self, value: int, left: Optional[Node] = None, right: Optional[Node] = None):
        self.value = value
        self.left = left
        self.right = right


"""
Is this just a level order traversal but we shift whether we right/left or left/right
based on the current height?
So if nodeHeight % 2 == 0: Right/Left
   if nodeHeight % 2 == 1: Left/Right
?
Will that work? I think so.
"""


def zigzag_traversal(root: Optional[Node]) -> list[list[int]]:
    node_values_by_level = collections.defaultdict(list)
    if not root:
        return []

    bfs_queue = collections.deque()
    bfs_queue.appendleft((root, 0))

    while bfs_queue:
        node, level = bfs_queue.pop()

        node_values_by_level[level].append(node.value)

        children = [node.left, node.right] if level % 2 == 1 else [node.right, node.left]
        for child in children:
            if child is not None:
                bfs_queue.appendleft((child, level + 1))

    return list(node_values_by_level.values())


def test(fn):
    root = Node(3, Node(9), Node(20, Node(15), Node(7)))
    assert fn(root) == [[3], [20, 9], [15, 7]]

    assert fn(Node(1)) == [[1]]

    assert fn([]) == []


test(zigzag_traversal)
