from __future__ import annotations
import collections
from typing import Optional
"""
Populating Next RIrght Pointers in Each Node

You are given a PERFECT BINARY TREE, where all leaves are on the same
level, and every parent has two children.

The binary tree has the following definition:

Node:
    int     val
    Node    left
    Node    right
    Node    next

Populate each next pointer to point to its next right node.
If there is no next right node, the next pointer should be set to NULL.

Initially, all pointers are set to null.
"""

"""
Thinking:
I think an easy way of doing this is to do a L->R level-order traversal of 
the binary tree, and to point each node to the next node in the level
"""

class Node:
    def __init__(self, value: int, left: Optional[Node] = None, right: Optional[Node] = None):
        self.value = value
        self.left = left
        self.right = right
        self.next = None


def connect(root: Optional[Node] = None) -> Optional[Node]:
    if root is None:
        return None

    level_nodes = collections.defaultdict(list)
    bfs_queue = collections.deque() # appendLeft to enqueue, pop to dequeue
    bfs_queue.appendleft((root, 0))

    # Level Traverse, Populating Level Values
    while bfs_queue:
        node, level = bfs_queue.pop()

        level_nodes[level].append(node)

        if node.left:
            bfs_queue.appendleft((node.left, level+1))
        if node.right:
            bfs_queue.appendleft((node.right, level+1))


    # For each level, point nodes to following nodes:
    for level in list(level_nodes.values()):
        for i in range(0, len(level) - 1):
            level[i].next = level[i+1]

    return root


# -- Test Zone --
root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
after = connect(root)

assert connect(None) == None