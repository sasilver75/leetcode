from __future__ import annotations
from typing import Optional, Union

"""
98 Validate Binary Search Tree
Category: Tree

Given the `root` of a binary tree, determine whether it is a valid
BINARY SEARCH TREE (BST).

A valid BST is defined as follows:
    1) The left subtree of a node contains only nodes less than the node's key
    2) The right subtree of a node contains only nodes greater than the node's key
    3) Both the left and right subtrees must also be binary search trees

Sam Note: It seems like there aren't going to be "repeat" elements in a BST,
according to the rules above.
"""


class Node:
    def __init__(self, value: int, left: Optional[Node] = None, right: Optional[Node] = None):
        self.value = value
        self.left = left
        self.right = right


def is_bst(root: Optional[Node]) -> bool:
    if root is None:
        return False

    def helper(node: Optional[Node], low_bound: Union[int, float], high_bound: Union[int, float]):
        """Node.value must be strictly > low_bound and < high_bound"""
        if node is None:
            return True

        if not (low_bound < node.value < high_bound):
            return False

        return helper(node.left, low_bound, node.value) and helper(node.right, node.value, high_bound)


    return helper(root, -float('inf'), float('inf'))


# -- Test --
def test(fn):
    head = Node(2, Node(1), Node(3))
    assert is_bst(head) == True

    head = Node(5, Node(1), Node(4, Node(3), Node(6)))
    assert is_bst(head) == False  # The root node's value is 5, but its right child is 4!

test(is_bst)