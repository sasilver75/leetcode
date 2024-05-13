from __future__ import annotations
from typing import Optional

"""
94: Binary Tree Inorder Traversal

Given the `root` of a binary tree, return the INORDER TRAVERSAL of its nodes' values
"""


class Node:
    def __init__(self, value: int, left: Optional[Node] = None, right: Optional[Node] = None):
        self.value = value
        self.left = left
        self.right = right



"""
An inorder traversal of a tree means:
Explore the left tree
Visit the current node
Explore the right tree
"""
def inorder_traversal(root: Optional[Node]) -> list[int]:
    acc = []

    def recursive_helper(node: Optional[Node]) -> None:
        """
        When called on an optional Node, proceeds to do an inorder traversal on the subtree below the node, adding nodes
        to the accumulator acc in inorder order
        """
        if not node:
            return

        recursive_helper(node.left)
        acc.append(node.value)
        recursive_helper(node.right)

    recursive_helper(root)

    return acc



"""
        1
  _             2
             3
"""
root = Node(1, None, Node(2, Node(3)))
assert inorder_traversal(root) == [1,3,2]


assert inorder_traversal(None) == []
assert inorder_traversal(Node(1)) == [1]