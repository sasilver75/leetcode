from __future__ import annotations
from typing import Optional

"""
You are given two binary trees root1 and root2

Imagine when you put one of them to cover the other
Some of the nodes are overlapped while others are not
You need to merge the two trees into a new binary tree.

The merge rule is that if two nodes overlap, then sum node values up
as the new value of the merged node.
Otherwise, the NOT NULL of the two nodes will be used
as the node of the new tree!

Return the merged tree.

Note: The merging process must start from the root of both nodes

        1                   2                   3
    3       2     +     1       3      =    4       5
5                         4       7       5   4       7
"""


def merge_two_binary_trees(root1: Optional[Node], root2: Optional[Node]) -> Node:
    if not root1 and not root2:
        return None

    merge_value = (root1.value if root1 else 0) + (root2.value if root2 else 0)
    merge_node = Node(merge_value)

    merge_node.left = merge_two_binary_trees(
        root1.left if root1 else None,
        root2.left if root2 else None
    )
    merge_node.right = merge_two_binary_trees(
        root1.right if root1 else None,
        root2.right if root2 else None
    )

    return merge_node


class Node:
    def __init__(self, value: int, left: Optional[Node] = None, right: Optional[Node] = None):
        self.value = value
        self.left = left
        self.right = right



# Case 1
root1 = Node(1, Node(3, Node(5)), Node(2))
root2 = Node(2, Node(1, None, Node(4)), Node(3, None, Node(7)))
merged = merge_two_binary_trees(root1, root2)
"""
        1                   2                   3
    3       2     +     1       3      =    4       5
5                         4       7       5   4       7
"""
print("Done! Use Debugger to Verify")