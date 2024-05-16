"""
Given a binary tree, determine if it is heigth balanced

A height-balanced binary tree is a binary tree in which the depth
 of the two subtrees of every node never differs by more than one.
"""

from typing import Optional


class Node:
    def __init__(self, value: int, left: Optional['Node'] = None, right: Optional['Node'] = None) -> None:
        self.value = value
        self.left=left
        self.right = right


def balanced(root: Optional[Node]) -> bool:
    """
    A tree is balanced when the depth of the two subtrees of every node never differs by mode than one

    Where the depth is defined as the deepest depth

    Given a single node, how can it be unbalanced?
    - The left is very short and the right is very long
    - Or the left is very long and the right is very short
    We know how to check for the minimum depth or maximum depth of a tree... so do we just do both?
    """

    def _get_min_depth(node: Node, height: int) -> int:
        """This is only called on actual nodes"""
        if node is None:
            return height    
        return min(_get_min_depth(node.left, height+1), _get_min_depth(node.right, height+1))
    
    def _get_max_depth(node: Node, height: int) -> int:
        """This is only called on actual nodes"""
        if node is None:
            return height    
        return max(_get_max_depth(node.left, height+1), _get_max_depth(node.right, height+1))
    
    if not root:
        return True

    left_min = _get_min_depth(root.left, 1)
    right_min = _get_min_depth(root.right, 1)

    left_max = _get_max_depth(root.left, 1)
    right_max = _get_max_depth(root.right, 1)

    print(left_min, right_min, left_max, right_max)

    if abs(left_min - left_max) > 1 or abs(left_max - right_min) > 1:
        return False
    return True

    

        
        


case1 = Node(3, Node(9), Node(20, Node(15), Node(7)))
case2 = Node(1, Node(2, Node(3, Node(4), Node(4)), Node(3)), Node(2))

assert balanced(case1)
assert not balanced(case2)
