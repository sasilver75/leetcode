from __future__ import annotations
from typing import Optional
"""
Same Tree

Given the roots of two BINARY TREES `p` and `q`, write a function to check
if they are the same or not.

Two binary trees are considered the same if they're STRUCTURALLY IDENTICAL, and
the nodes have the same values.

"""

class Node:
    def __init__(self, value: int, left: Optional[Node] = None, right: Optional[Node] = None):
        self.value = value
        self.left = left
        self.right = right

"""
Thinking: Is it enough to check the validity condition locally for 
every position in the tree? I think it might be, becasue we're only talking 
about checking that it's a binary search tree
"""

def is_same_tree(p: Optional[Node], q: Optional[Node]) -> bool:
    # Attempt to disprove the validity of the tree at the current location
    """
    1. One of p/q is None, and the other is not
    2. p/q are both present, but their values are different
    """
    if (
            (p is None and q is not None) or
            (p is not None and q is None) or
            (p and q and p.value != q.value)
    ):
        return False

    # Now, we know that either both are present (with same values) or both are not present
    if p is None and q is None:
        return True

    # Now, we know that both are present with the same values
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)





# --- test --
p = Node(1, Node(2), Node(3))
q = Node(1, Node(2), Node(3))
assert is_same_tree(p, q) == True

p = Node(1, Node(2))
q = Node(1, None, Node(2))
assert is_same_tree(p, q) == False

p = Node(1, Node(2), Node(1))
q = Node(1, Node(1), Node(2))
assert is_same_tree(p, q) == False
