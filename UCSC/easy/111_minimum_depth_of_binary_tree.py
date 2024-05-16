from math import inf
from typing import Optional


class Node:
    def __init__(self, value: int, left: Optional['Node'] = None, right: Optional['Node'] = None) -> None:
        self.value = value
        self.right = right
        self.left = left


def minimum_depth(root: Node) -> int:
    
    def _depth(node: Node, depth: int) -> int:
        """
        This only returns the depth when it hits a leaf node. It's never called on None nodes
        It's called with its depth already have been added
        """
        if node.left is None and node.right is None:
            return depth
        
        return min(
            _depth(node.left, depth+1) if node.left else inf,
            _depth(node.right, depth+1) if node.right else inf
        )
        
    return _depth(root, 1)

assert minimum_depth(Node(3, Node(9), Node(20, Node(15), Node(7)))) == 2
assert minimum_depth(Node(2, None, Node(3, None, Node(4, None, Node(5, None, Node(6)))))) == 5
