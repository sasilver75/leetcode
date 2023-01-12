"""
Given the root of a binary tree, check whether it's a mirror of itself
(ie) symmetricl around its center

        1
    2       2
3      4 4      3    This is symmetric!
"""

from __future__ import annotations

from typing import Optional


class BSTNode:
    def __init__(self, value, left: Optional[BSTNode] = None, right: Optional[BSTNode] = None):
        self.value = value
        self.left = left
        self.right = right

"""
Need a recursive helper
"""
def isSymmetric(root: BSTNode) -> bool:
    return isSymmetricHelper(root, root)

"""
Base Cases:
* If neither are present, that's True
* If only one is present, that's False
* If both are present and the values aren't the same, that's False
"""
def isSymmetricHelper(left: Optional[BSTNode], right: BSTNode) -> bool:
    if not left and not right:
        return True
    if (left and not right) or (not left and right):
        return False
    if left.value != right.value:
        return False

    return isSymmetricHelper(left.left, right.right) and (isSymmetricHelper(left.right, right.left))


# -------


"""
        1
     2     2
   3   4  4  3 

"""
# Case 1:
root = BSTNode(1)
n1 = BSTNode(2)
n2 = BSTNode(2)
n3 = BSTNode(3)
n4 = BSTNode(4)
n5 = BSTNode(4)
n6 = BSTNode(3)
root.left = n1
root.right = n2
n1.left = n3
n1.right = n4
n2.left = n5
n2.right = n6

print(isSymmetric(root)) # True


# Case 2:

"""
            1
        2       2
          3       3
"""

root = BSTNode(1)
n2 = BSTNode(2)
n3 = BSTNode(2)
n4 = BSTNode(3)
n5 = BSTNode(3)

root.left = n2
root.right = n3
n2.right = n4
n3.right = n5

print(isSymmetric(root)) # False
