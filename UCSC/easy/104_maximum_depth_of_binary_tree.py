"""
Given the ROOT of a binary tree, return its MAXIMUM DEPTH

A binary tree's maximum depth is the number of nodes along the lognest path from the root down to the furthest leaf node
"""

from typing import Optional


class Node:
    def __init__(self, value: int, left: Optional['Node'] = None, right: Optional['Node'] = None) -> None:
        self.value = value
        self.left = left
        self.right = right


def max_depth(node: Optional[Node]) -> int:
    """
    For this one, you can do any sort of tree traversal, just keep track of your depth and update some maxDepth variable
    """
    maxDepth = 0
    
    def recurse(node: Optional[Node], depth) -> None:
        nonlocal maxDepth

        if node is None:
            return
        
        # We're at a real node, let's check to see if we should update maxDepth
        maxDepth = max(maxDepth, depth)

        recurse(node.left, depth+1)
        recurse(node.right, depth+1)
    
    recurse(node, 1)
    print(maxDepth)
    return maxDepth
        


case1 = Node(3, Node(9), Node(20, Node(15), Node(7)))
case2 = Node(1, None, Node(2))

assert max_depth(case1) == 3
assert max_depth(case2) == 2