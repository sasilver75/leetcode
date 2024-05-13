from __future__ import annotations
from typing import Optional
"""
Kth Smallest Elemetn in a BST
Category: Tree

Given the `root` of a binary search tree (BST), and an integer `k`,
return the `kth` smallest value (`1-indexed`) of all of the values of the nodes
in the tree.
"""

class Node:
    def __init__(self, value: int, left: Optional[Node] = None, right: Optional[Node] = None):
        self.value = value
        self.left = left
        self.right = right


def kth_smallest_naive(root: Optional[Node], k: int) -> int:
    node_values = []

    def helper(node: Optional[Node]):
        if node is None:
            return
        node_values.append(node.value)
        helper(node.left)
        helper(node.right)

    helper(root)

    node_values.sort()

    return node_values[k-1]


"""
Can we do it in better than O(NLogN) time 
by actually taking advantage of the fact that it's a binary search tree?

The O(NLogN) time in the previous example came from the fact that we had
to traverse the whole tree, and THEN sort the values into a sorted list.

Take advantage of the fact that we're in a BST, is there a way to traverse
the tree and simply END UP WITH a sorted list?
Then we could do this in O(N) time / O(N) space!
            
                    5
                3         6
            2      4
        1

Left, Middle, Right --> Infix DFS?
Let's try it!
"""
def kth_smallest(root: Optional[Node], k: int) -> int:
    if root is None:
        return None

    values = []

    def helper(node: Optional[Node]) -> None:
        if node is None:
            return

        helper(node.left)
        values.append(node.value)
        helper(node.right)

    helper(root)
    return values[k-1]


# -- Test Zone --
def test(fn):
    head = Node(3, Node(1, None, Node(2)), Node(4))
    assert fn(head, 1) == 1

    head = Node(5, Node(3, Node(2, Node(1)), Node(4)), Node(6))
    assert fn(head, 3) == 3

test(kth_smallest_naive)
test(kth_smallest)