from __future__ import annotations

import collections
from typing import Optional

"""
Binary Tree Level Order Traversal

Given the root of a binary tree, return the LEVEL ORDER TRAVERSAL of its
nodes values (ie from left to right, level by level)
"""


class Node:
    def __init__(self, value: int, left: Optional[Node] = None, right: Optional[Node] = None):
        self.value = value
        self.left = left
        self.right = right


def level_order_naive(node: Optional[Node]) -> list[list[int]]:
    if node is None:
        return []

    levels = collections.defaultdict(list)

    bfs_queue = collections.deque()
    bfs_queue.appendleft((node, 0))

    while bfs_queue:
        node, level = bfs_queue.pop()

        # Process
        levels[level].append(node.value)

        # Enqueue Available Children
        if node.left:
            bfs_queue.appendleft((node.left, level+1))
        if node.right:
            bfs_queue.appendleft((node.right, level+1))


    return list(levels.values())

"""
Is there a better way to do it, perhaps one that doesn't take O(N) memory?
The thing is, we're returning a list of lists, so it's going to take O(N)
memory regardless. I don't think we can do better than this. Asmyptotically
"""

# -- Test Zone --
def test(fn):
    head = Node(3, Node(9), Node(20, Node(15), Node(7)))
    assert level_order_naive(head) == [[3], [9, 20], [15, 7]]

    head = Node(1)
    assert level_order_naive(head) == [[1]]

    head = None
    assert level_order_naive(head) == []

test(level_order_naive)