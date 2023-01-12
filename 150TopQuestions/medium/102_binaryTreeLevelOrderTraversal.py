"""
Binary Tree Level Order Traversal

Given the `root` of a binary tree, return the LEVEL ORDER TRAVERSAL of its
nodes' values!
ie: From left to right, level by level

                3
        9               20          -->  [3, [9, 20], [15, 7]]
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


"""
Thinking:

One dumb way of going about this would be to traverse throug the three in any manner,
appending into a list (height, value) for each node in the tree.

A better way is to just do a breadth-first search of 
"""


def level_order_traversal(root: Optional[Node] = None) -> list[list[int]]:
    level_values = collections.defaultdict(list)  # level:values
    bfs_queue = collections.deque()  # appendLeft to enqueue, pop to dequeue

    if root:
        bfs_queue.appendleft((root, 0))

    while bfs_queue:
        # Process next node
        node, level = bfs_queue.pop()
        level_values[level].append(node.value)

        # Enqueue appropriate nodes
        if node.left:
            bfs_queue.appendleft((node.left, level+1))
        if node.right:
            bfs_queue.appendleft((node.right, level+1))

    ans = list(level_values.values())
    print(ans)
    return ans


# -- Test --
head = Node(3, Node(9), Node(20, Node(15), Node(7)))
assert level_order_traversal(head) == [[3], [9, 20], [15, 7]]

head = Node(1)
assert level_order_traversal(head) == [[1]]

head = None
assert level_order_traversal(head) == []
