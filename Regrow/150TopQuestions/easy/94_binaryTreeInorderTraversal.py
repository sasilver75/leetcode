from __future__ import annotations
from typing import Optional
"""
Binary Tree Inorder Traversal

Given the ROOT of a binary tree, return the inorder traversal of its nodes
values!
"""


class Node:
    def __init__(self, value: int, left: Optional[Node] = None, right: Optional[Node] = None):
        self.value = value
        self.left = left
        self.right = right

def in_order_traversal(node: Node) -> list[int]:
    acc = []
    explore(node, acc)
    print(acc)
    return acc

def explore(node: Optional[Node], acc: list[int]) -> None:
    """
    Inorder Recursive Traversal of a Tree, appending to acc
    Recall: Inorder === Recurse Left, Exploit Cur, Recurse Right

    as opposed to Preorder (Exploit, Left, Right) or Postorder (Left, Right, Exploit)
    """
    if not node:
        return
    explore(node.left, acc)
    acc.append(node.value)
    explore(node.right, acc)


# Case 1
"""
                1
                    2
                  3
"""
root = Node(1, None, Node(2, Node(3)))
assert in_order_traversal(root) == [1,3,2]

# Case 2
root = None
assert in_order_traversal(root) == []


# Case 3
root = Node(1)
assert in_order_traversal(root) == [1]