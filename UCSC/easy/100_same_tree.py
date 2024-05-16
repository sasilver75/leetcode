"""
Given the roots of two binary trees `p` and `q`

Write a function to check if they're the same or not

Two binary trees are considered same IF
- They are structurally identical
- Nodes have the same value
"""

from typing import Optional


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_same_tree(p: Optional[Node], q: Optional[Node]) -> bool:
    """
    We're basically going to be traversing through the two trees
    as the same time.
    We can use any tree traverasl method we'd like, as long as we do 
    it the same for each.
    So we'll basically just use an preorder traversal here, but have a reference
    to a node in each tree.
    """

    def _is_same_tree(pee: Optional[Node], que: Optional[Node]):
        # check for local failure (preorder)
        if pee is None and que is None:
            return True
        
        if any([
            pee and que is None,
            que and pee is None,
            pee and que and pee.value != que.value
        ]):
            return False
        
        # check for failure in recursion    
        left_good = _is_same_tree(pee.left, que.left) if pee.left or que.left else True
        right_good = _is_same_tree(pee.right, que.right) if pee.right or que.right else True
        
        if not all([left_good, right_good]):
            return False
        
        # if we didn't find a failure, return true
        return True

    return _is_same_tree(p, q)


case1 = (
    Node(1, Node(2), Node(3)),
    Node(1, Node(2), Node(3)),
    True
)

case2 = (
    Node(1, Node(2)),
    Node(1, None, Node(2)),
    False
)

case3 = (
    Node(1, Node(2), Node(1)),
    Node(1, Node(1), Node(2)),
    False
)

for p, q, ans in (case1, case2, case3):
    assert is_same_tree(p, q) == ans