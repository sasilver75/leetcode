"""
Given the rOOT of a binary tree and an integer TARGETSUM, return TRUE if the tree has a
root-to-leaf path such taht adding up all values along that path equals targetSum!

A leaf is a node with no children
"""

from typing import Optional


class Node:
    def __init__(self, value: int, left: Optional['Node'] = None, right: Optional['Node'] = None) -> None:
        self.value = value
        self.left = left
        self.right = right

def hasPathSum(root: Optional[Node], target_sum: int) -> bool:
    """
    This is another one where we can traverse the tree in any way that we like.
    As we traverse, we need to keep track of the sum.

    At any node: Increment the sum with our current node value
    If at a leaf node (no children), check to see if sum=targetSum; if so, return True
    When called on a None node, return False.
    """
    if root is None:
        return False
    
    def _recurse(node: Optional[Node], current_sum: int) -> bool:
        if node is None:
            return False
        
        # Process current node
        current_sum += node.value

        # Check to see if leaf node
        if node.left is None and node.right is None:
            return current_sum == target_sum

        # If it's not, then we have recursing to do.
        # If we can find a good pathSum on either subtree, that's all we need!
        # It's fine to recurse on a none.
        return _recurse(node.left, current_sum) or _recurse(node.right, current_sum)
    

    return _recurse(root, 0)


case1 = Node(5, Node(4, Node(11, Node(7), Node(2))), Node(8, Node(13), Node(4, None, Node(1))))
case2 = Node(1, Node(2), Node(3))
case3 = None

assert hasPathSum(case1, 22)
assert not hasPathSum(case2, 5)
assert not hasPathSum(None, 0)
