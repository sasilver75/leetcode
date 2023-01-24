from __future__ import annotations
from typing import Optional

"""
Kth Smallest Element in a BST

Given the `root` of a binary search tree, and an integer `k`,
return the kth smallest value (1-indexed) of all of the values
of the nodes in the tree!
"""


class Node:
    def __init__(self, value: int, left: Optional[Node] = None, right: Optional[Node] = None):
        self.value = value
        self.left = left
        self.right = right

"""
How might we go about this?

I believe it's true than an Inorder DFS (left, mid, right) traversal of a 
binary tree results in an ASC traversal of node values in the tree

Let's do that, then select the kth element!

Note:
Inorder Traversal
    - Recurse on Left child, Process Current Node, Recurse on Right Child
    - In the case of BST, gives nodes in Non-Decreasing Order
Preorder Traversal
    - Process Current Node, Recurse on Left Child, Recurse on Right Child
    - Used to create a copy of a tree
PostOrder Traversal
    - Recurse on left child, Recurse on Right child, Process Current Node
    - Used to delete a tree

"""
def kth_smallest_naive(root: Optional[Node], k: int) -> int:
    nodes = []
    def recursive_explorer(node: Node) -> None:
        if node.left:
            recursive_explorer(node.left)
        nodes.append(node.value)
        if node.right:
            recursive_explorer(node.right)

    recursive_explorer(root)
    return nodes[k-1]


"""
Okay, the above solution is fine, but it necessarily requires visiting all nodes.
We could cut this short by "counting" the number of visited nodes that we're on,
and just returning when we reach that one. 
"""
def kth_smallest(root: Optional[Node], k: int) -> int:
    visited_count = 0
    kth_smallest = None

    def recursive_explorer(node: Node) -> None:
        nonlocal visited_count
        nonlocal kth_smallest

        if visited_count > k:
            return

        if node.left:
            recursive_explorer(node.left)

        visited_count += 1
        if visited_count == k:
            kth_smallest = node.value

        if node.right:
            recursive_explorer(node.right)

    recursive_explorer(root)
    return kth_smallest



# ----------------------------------------
def test(fn):
    """
                3
        1                 4
            2
    """
    assert fn(
        Node(3, Node(1, None, Node(2)), Node(4)),
        k=1
    ) == 1

    """ 
                    5
            3               6
         2      4
      1
    """
    assert fn(
        Node(5, Node(3, Node(2, Node(1)), Node(4)), Node(6)),
        k=3
    ) == 3


test(kth_smallest_naive)
test(kth_smallest)