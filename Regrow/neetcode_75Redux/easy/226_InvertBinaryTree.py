from __future__ import annotations
from typing import Optional
"""
Invert Binary Tree

Given the ROOT of a binary tree, INVERT
the binary tree, and return its root!

Example:
        4                           4
    2       7           ->      7       2
1     3   6    9            9     6    3   1

{So this really seems more like "rotate around the Y axis"}
"""
from typing import Optional


class Node:
    def __init__(self, value: int, left: Optional[Node] = None, right: Optional[Node] = None):
        self.value = value
        self.left = left
        self.right = right


"""
Thinking:
So again this is more like a "rotate around the y axis"
So I think what we need to do locally is :

Rotate-In-Place the left node's subtree
Rotate-In-Place the right node's subtree
Swap left/right nodes

Recursively, do this.

        4                           4
    2       7           ->      7       2
1     3   6    9            9     6    3   1




"""

def invert_binary_tree_mutative(root: Node) -> Node:
    def rotate(node: Node):
        if node.left:
            rotate(node.left)
        if node.right:
            rotate(node.right)
        node.left, node.right = node.right, node.left

    rotate(root)
    return root

r = Node(4, Node(2, Node(1), Node(3)), Node(7, Node(6), Node(9)))
invert_binary_tree_mutative(r)
print(r)
"""
Goal: 
        4                           4
    2       7           ->      7       2
1     3   6    9            9     6    3   1

            4
        7       2
     9     6  3    1
     
It worked!
"""