"""
Given a binary tree, find its minimum depth

The minimum depth is the shortest number of nodes along the hosrtestt
path from the root node down to the nearest leaf node, where a leaf
node is a node with no children.
"""
from __future__ import annotations
from typing import Optional

class Node:
    def __init__(self, val: int, left: Optional[Node] = None, right: Optional[Node] = None):
        self.val = val
        self.left = left
        self.right = right


def minimum_depth(root: Node):
    def helper(node: Node, depth: int):
        # Base Case: You are a leaf node with no children. Return your height.
        if not any([node.left, node.right]):
            return depth

        # Recursive case. You have children! Return the minimum of child subtree(s)
        if node.left and node.right:
            # If there are two children, return min of each subtree
            return min(
                helper(node.left, depth+1) if node.left else depth,
                helper(node.right, depth+1) if node.right else depth
            )
        elif node.left:
            # If just left child, return height of left subtree
            return helper(node.left, depth+1)
        else:
            # If just right child, return height of right subtree
            return helper(node.right, depth+1)
    if not root:
        return 0
    return helper(root, 1)

## Case 1
"""
        3
    9       20
          15  7
Ans: 2
"""
r = Node(3)
n2 = Node(9)
n3 = Node(20)
n4 = Node(15)
n5 = Node(7)
r.left = n2
r.right = n3
n3.left = n4
n3.right = n5
print(minimum_depth(r)) # 2


# Case 2
"""
   2
     3
       4
        5
          6

Ans: 5
"""
r = Node(2)
n2 = Node(3)
n3 = Node(4)
n4 = Node(5)
n5 = Node(6)
r.right = n2
n2.right = n3
n3.right = n4
n4.right = n5
print(minimum_depth(r)) # 5




