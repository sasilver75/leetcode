from __future__ import annotations
from typing import Optional
"""
Evaluate Boolean Binary Tree

You're given the `root` of a FULL binary tree with the following properties:
    * Leaf nodes have either the value 0 or 1, where 0 represents `False` and 1 represents `True`
    * Non-leaf nodes have either the value 2 or 3, where 2 represents the boolean `OR` and 3 represents the boolean `AND`

The evaluation of a node is as follows:
    * If the node is a leaf node, the evaluation is the value of the node, i.e. True or False
    * Otherwise, evaluate the node's two children and APPLY the boolean operation of its value with the value of its children's evaluations

Return the boolean result of evaluating the `root` node

NOTE:
    - A "full" binary tree is one where any node that has children has two children. (0 or 2 children)
    - A leaf node is a node that has zero children
"""

class Node:
    def __init__(self, value: int, left: Optional[Node] = None, right: Optional[Node] = None):
        self.value = value
        self.left = left
        self.right = right


# This uh... isn't a binary search problem. Not sure why it's here?
def evaluate_tree(root: Optional[Node]) -> bool:
    if root is None:
        return False

    if root.value == 0:
        return False
    elif root.value == 1:
        return True
    elif root.value == 2:
        return evaluate_tree(root.left) or evaluate_tree(root.right)
    else:
        return evaluate_tree(root.left) and evaluate_tree(root.right)


def test(fn):
    head = Node(2, Node(1), Node(3, Node(0), Node(1)))
    assert fn(head) == True

    head = None
    assert fn(head) == False

test(evaluate_tree)


