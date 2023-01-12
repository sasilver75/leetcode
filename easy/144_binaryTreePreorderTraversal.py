"""
Given the ROOT of a binary tree, returnr the preorder traversal
of its nodes values!
"""
from __future__ import annotations

from typing import Optional


class BSTNode:
    def __init__(self, value: int, left: Optional[BSTNode] = None, right: Optional[BSTNode] = None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node: {self.value}"

def preorder_traverse(node: BSTNode) -> list[int]:
    # print("Node: ", node)
    if node:
        print(node.value)
    if hasattr(node, "left") and node.left:
        preorder_traverse(node.left)
    if hasattr(node, "right") and node.right:
        preorder_traverse(node.right)

# case 1
head1 = BSTNode(1)
n2 = BSTNode(2)
n3 = BSTNode(3)
head1.right = n2
n2.left = n3
preorder_traverse(head1) # 1, 2, 3
print("---")

# case 2
head2 = None
preorder_traverse(head2) #
print("---")

# case 3
head3 = BSTNode(1)
preorder_traverse(head3) # 1
print("---")