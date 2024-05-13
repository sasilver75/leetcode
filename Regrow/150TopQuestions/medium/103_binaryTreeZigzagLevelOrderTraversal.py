"""
Binary Tree ZigZag Level Order Traversal

Given the `root` of a BINARY TREE, return the ZIGZAG LEVEL ORDER TRAVERSAL
of its nodes values
(i.e. from left to right, then right to left for the next level, and
alternate between)

                        3
                9              20          ->       [[3], [9,20], [15,7]]
                            15      7
"""
from __future__ import annotations

import collections
from typing import Optional

class Node:
    def __init__(self, value: int, left: Optional[Node] = None, right: Optional[Node] = None):
        self.value = value
        self.left = left
        self.right = right

def zigzag_travsal(root: Optional[Node] = None) -> list[list[int]]:
    level_values = collections.defaultdict(list) # level: [...values]
    bfs_queue = collections.deque() # appendleft to enqueue, pop to deque
    if root:
        bfs_queue.appendleft((root, 0, False))

    while bfs_queue:
        # Process Node
        node, level, left_to_right = bfs_queue.pop()
        level_values[level].append(node.value)

        # Sweep in appropriate direction, enqueueing
        next_level = [node.left, node.right] if left_to_right else [node.right, node.left]
        for child_node in next_level:
            if child_node:
                bfs_queue.appendleft((child_node, level+1, not left_to_right))

    return list(level_values.values())



# -- Test --
head = Node(3, Node(9), Node(20, Node(15), Node(7)))
assert zigzag_travsal(head) == [[3], [20,9], [15,7]]

head = Node(1)
assert zigzag_travsal(head) == [[1]]

head = None
assert zigzag_travsal(head) == []