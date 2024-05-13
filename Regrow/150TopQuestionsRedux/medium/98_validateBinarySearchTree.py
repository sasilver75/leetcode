from __future__ import annotations
from typing import Optional

"""
Validate Binary Search Tree

Given the ROOT of a binary tree, determine if it is a valid binary search tree (BST)

A valid BST is defined as follows:
1) The left subtree of a node contains only nodes with keys less than the node's key
2) The right subtree of a node contains only nodes with keys greater than the ndoe's key
3) Both the left and right subtrees must also be binary search trees
"""


class Node:
    def __init__(self, value: int, left: Optional[Node] = None, right: Optional[Node] = None):
        self.value = value
        self.left = left
        self.right = right


"""
How should we validate a binary search tree (BST)?
A BST is a bianry tree where all values less than a node are in a node's left 
subtree, and all values greater than a node are in a node's right subtree.

Proposal 1:
We just validate the BST condition locally at a node, and then validate each of 
the left and right subtrees of the node by the same proposed logic.

Okay... yeah, that worked. Nice.
"""
def validate_binary_search_tree(root: Optional[Node]) -> bool:
    # Assuming that a tree contains only unique values
    if not root:
        return True

    if root.left and root.value < root.left.value:
        return False
    if root.right and root.value > root.right.value:
        return False

    return validate_binary_search_tree(root.left) and validate_binary_search_tree(root.right)


def test(fn):
    assert fn(Node(2, Node(1), Node(3))) == True
    assert fn(Node(5, Node(1), Node(4, Node(3), Node(6)))) == False


test(validate_binary_search_tree)
