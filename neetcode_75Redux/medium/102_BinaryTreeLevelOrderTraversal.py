from __future__ import annotations

import collections
from typing import Optional

"""
Binary Tree Level Order Traversal

Given the `root` of a binary tree, return the LEVEL ORDER TRAVERSAL OF
ITS NODES VALUES (ie from left to right, level by level).


"""


class Node:
    def __init__(self, value: int, left: Optional[Node] = None, right: Optional[Node] = None):
        self.value = value
        self.left = left
        self.right = right


"""
Thinking: I think there are two options for what I could do here:
1. I think it's going to be important to do a BFS of the tree, and accumulate
 
"""


def level_order_bfs(root: Optional[Node]) -> list[list[int]]:
    levels = collections.defaultdict(list)
    node_queue = collections.deque()
    if root:
        node_queue.appendleft((root,0))

    while node_queue:
        node, level = node_queue.pop()

        levels[level].append(node.value)

        if node.left:
            node_queue.appendleft((node.left, level+1))
        if node.right:
            node_queue.appendleft((node.right, level+1))

    ans = list(levels.values())
    print(f"{ans = }")
    return ans



def test(fn):
    root = Node(3, Node(9), Node(20, Node(15), Node(7)))
    assert fn(root) == [[3], [9, 20], [15, 7]]

    root = Node(1)
    assert fn(root) == [[1]]

    root = None
    assert fn(root) == []

test(level_order_bfs)