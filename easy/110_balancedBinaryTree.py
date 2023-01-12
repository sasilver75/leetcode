"""
Given a Binary Tree, determine if it is HEIGHT-BALANCED!
For this problem, a heigh-balanced tree is defined as:
A binary tree in which the left and right subtrees of every node differ
by no more than 1.
"""
from __future__ import annotations
from typing import Optional


class Node:
    def __init__(self, value: int, left: Optional[Node] = None, right: Optional[Node] = None):
        self.value = value
        self.left = left
        self.right = right


def is_balanced(root: Node):

    def helper(root: Optional[Node], height: int):
        if not root:
            return height
        return max(helper(root.left, height+1), helper(root.right, height+1))

    if not root:
        return True
    if abs(helper(root.left, 1) - helper(root.right, 1)) > 1:
        return False
    return True



# Case 1
"""
           3
      9         20
            15      7
Ans: True
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

print(is_balanced(r)) # True

# Case 2
"""
             1
         2       2
    3      3
   4  4
Ans: False
"""
r = Node(1)
n2 = Node(2)
n3 = Node(2)
n4 = Node(3)
n5 = Node(3)
n6 = Node(4)
n7 = Node(4)
r.left = n2
r.right = n3
n2.left = n4
n2.right = n5
n4.left = n6
n4.right = n7

print(is_balanced(r)) # False
