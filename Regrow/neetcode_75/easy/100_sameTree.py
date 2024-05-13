from __future__ import annotations
from typing import Optional

"""
Same Tree
Category: Tree

Given the roots of two binary trees `p` and `q`, write a function
to check if they are the same or not.

Two binary trees are considered the SAME if they are structurally
identical, and the nodes have the same value.
"""


class Node:
    def __init__(self, value: int, left: Optional[Node] = None, right: Optional[Node] = None):
        self.value = value
        self.left = left
        self.right = right


def is_same_tree(p: Optional[Node], q: Optional[Node]):
    # We just traverse both trees at the same time, in any fashion
    p_nodes, q_nodes = [p], [q]

    while p_nodes and q_nodes:
        p = p_nodes.pop()
        q = q_nodes.pop()

        if p.value != q.value:
            return False

        lefts = [p.left, q.left]
        if any(lefts) and not all(lefts):
            return False
        if p.left:
            p_nodes.append(p.left)
            q_nodes.append(q.left)

        rights = [p.right, q.right]
        if any(rights) and not all(rights):
            return False
        if p.right:
            p_nodes.append(p.right)
            q_nodes.append(q.right)

    # Both should be empty
    return not (p_nodes or q_nodes)


# -- Test Zone --
def test(fn):
    phead = Node(1, Node(2), Node(3))
    qhead = Node(1, Node(2), Node(3))
    assert fn(phead, qhead) == True

    phead = Node(1, Node(2))
    qhead = Node(1, None, Node(2))
    assert fn(phead, qhead) == False


test(is_same_tree)
