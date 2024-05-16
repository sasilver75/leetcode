"""
Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself
(symmetric around the center)
"""

from typing import Optional


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_symmetric(root: Optional[Node]) -> bool:

    def _is_symmetric(left: Optional[Node], right: Optional[Node]) -> bool:
        # If both are None, they're identical
        if left is None and right is None:
            return True
        # IF ONE is none, they're not identical
        if left is None or right is None:  # By putting this after the previous statement, this really means XOR
            return False
        
        # PREORDER
        if left.value != right.value:
            return True
        
        # Inside symmetry
        inside_symmetric = _is_symmetric(left.right, right.left)

        # Outside symmetry
        outside_symmetric = _is_symmetric(left.left, right.right)

        return inside_symmetric and outside_symmetric
    
    return _is_symmetric(root, root)


        


case1 = Node(1,Node(2, Node(3), Node(4)), Node(2, Node(4), Node(3)))
case2 = Node(1, Node(2, None, Node(3)), Node(2, None, Node(3)))

assert is_symmetric(case1)
assert not is_symmetric(case2)

