from __future__ import annotations

import collections
from typing import Optional

"""
Invert Binary Tree
Category: Tree

Given the roots of a binary tree, INVERT THE TREE, and return its root!

        4                           4
    2       7           ->      7       2
1     3  6     9              9  6     3  1

Note that this really appears to be "mirroring it around the middle",
ie left becomes right, etc. Rather than it being flipped upside down,
or something, as you might expect of "invert."
"""


class Node:
    def __init__(self, value: int, left: Optional[Node] = None, right: Optional[Node] = None):
        self.value = value
        self.left = left
        self.right = right


def invert_tree(root: Optional[Node]) -> Optional[Node]:
    if root.left:
        invert_tree(root.left)
    if root.right:
        invert_tree(root.right)

    root.left, root.right = root.right, root.left

    return root


def levels(root: Optional[Node]) -> Optional[Node]:
    # Given a FULL tree, return the list of nodes in level order, left to right
    # Using a BFS
    acc = []
    if not root:
        return acc
    nodes = collections.deque([root])
    while nodes:
        node = nodes.pop()
        acc.append(node.value)
        if node.left:
            nodes.appendleft(node.left)
        if node.right:
            nodes.appendleft(node.right)

    print(acc)
    return acc


# -- Test Zone --
head = Node(4, Node(2, Node(1), Node(3)), Node(7, Node(6), Node(9)))
assert levels(invert_tree(head)) == [4, 7, 2, 9, 6, 3, 1]

head = Node(2, Node(1), Node(3))
assert levels(invert_tree(head)) == [2, 3, 1]
