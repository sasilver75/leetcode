"""
Given the ROOT of a binary tree and an integer
targetSum, return True if the tree has a ROOT-TO-LEAF path
such that adding up all the values along the path equals TARGETSUM

A LEAF is a node with no children
"""
from __future__ import annotations
from typing import Optional


class Node:
    def __init__(self, value: int, left: Optional[Node] = None, right: Optional[Node] = None):
        self.value = value
        self.left = left
        self.right = right

def pathSum(root: Optional[Node], target: int) -> bool:
    def helper(node: Node, sum: int) -> bool:
        # Increment our running sum
        sum += node.value

        # Are we at a leaf node?
        if not node.left and not node.right:
            return sum == target
        # We have 1 or 2 children - recurse into them!
        return any([
            helper(node.left, sum) if node.left else False,
            helper(node.right, sum) if node.right else False
        ])

    if not root:
        return False

    return helper(root, 0)





# Case 1
"""
Note to self: A binary SEARCH tree is different from a binary tree. The former
has impilications around the ordering of elements. The latter is just the degree of nodes.

            5
        4       8
    11        13   4
  7   2               1

Ans: 22
"""
r = Node(5)
n2 = Node(4)
n3 = Node(8)
n4 = Node(11)
n5 = Node(13)
n6 = Node(4)
n7 = Node(7)
n8 = Node(2)
n9 = Node(1)
r.left = n2
r.right = n3
n2.left = n4
n3.left = n5
n3.right = n6
n4.left = n7
n4.right = n8
n6.right = n9
print(pathSum(r, 22)) # true

# Case 2
"""
       1
   2       3
"""
r = Node(1)
n2 = Node(2)
n3 = Node(3)
r.left = n2
r.right = n3
print(pathSum(r, 5)) # false


# Case 3
print(pathSum(None, 0)) # false