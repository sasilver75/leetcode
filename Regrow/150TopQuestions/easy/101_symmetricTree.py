from __future__ import annotations
from typing import Optional

"""
Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself!
IE, symmetric around the center
                |
                1
        2       |        2
    3       4   |    4       3
                |
"""


class Node:
    def __init__(self, value: int, left: Optional[Node] = None, right: Optional[Node] = None):
        self.value = value
        self.left = left
        self.right = right


"""
Thinking:
A tree is symmetric if its left and right subtrees are symmetric

Options:
Two pointers, each walking down the in opposite  directions?

"""


def is_symmetric(root: Node) -> bool:
    return helper(root, root)


def helper(lnode: Optional[Node], rnode: Optional[Node]) -> bool:
    # Check the current nodes
    if any([lnode, rnode]) and not all([lnode, rnode]):
        return False
    if not any([lnode, rnode]):
        return True

    # Check the exterior recursion (leftLEFT and rightRIGHT) and interior recursion (leftRIGHT and rightLEFT)
    return helper(lnode.left, rnode.right) and helper(lnode.right, rnode.left)


# Case 1: [1,2,2,3,4,4,3]
root = Node(1, Node(2, Node(3), Node(4)), Node(2, Node(4), Node(3)))
assert is_symmetric(root) == True

# Case 2: [1,2,2,null,3,null,3]
root = Node(1, Node(2, None, Node(3)), Node(2, None, Node(3)))
assert is_symmetric(root) == False
