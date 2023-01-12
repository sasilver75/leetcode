from __future__ import annotations
from typing import Optional

"""
Subtree of Another Tree
Category: Tree

Given the roots of two binary trees `root` and `subRoot`, return `true` if
there is a subtree of `root` with the same structure and node values of `subroot`,
and false otherwise!

A subtree of a binary tree is a tree that consists of a node in `tree`
and all of this nodes descendants. The tree `tree` could also be
considered a subtree of itself.
"""


class Node:
    def __init__(self, value: int, left: Optional[Node] = None, right: Optional[Node] = None):
        self.value = value
        self.left = left
        self.right = right


"""
The way that I can think of doing this is calling "is_same_tree" on 
every node in root's tree.

If there were R nodes in root and S nodes in subRoot, this would
only be O(R*S), which wouldn't be so bad if S were a small subroot.

I don't otherwise know offhand how to subproblem this one out. 
Let's do this first and then check Leetcode solutions for hints.
"""


def is_subtree(root: Optional[Node], subRoot: Optional[Node]):
    # Return true if subRoot is a subtree of root

    def is_same_tree(p: Optional[Node], q: Optional[Node]) -> bool:
        p_nodes = [p]
        q_nodes = [q]

        while p_nodes and q_nodes:
            p = p_nodes.pop()
            q = q_nodes.pop()

            if p.value != q.value:
                return False

            lefts = [p.left, q.left]
            rights = [p.right, q.right]

            if (any(lefts) and not all(lefts)) or (any(rights) and not all(rights)):
                return False

            if p.left:
                p_nodes.append(p.left)
                q_nodes.append(q.left)

            if p.right:
                p_nodes.append(p.right)
                q_nodes.append(q.right)

        return not (p_nodes or q_nodes)

    # Walk through root checking if is_same_tree(cur, subRoot)
    nodes = [root]
    while nodes:
        node = nodes.pop()
        if is_same_tree(node, subRoot):
            return True
        if node.left:
            nodes.append(node.left)
        if node.right:
            nodes.append(node.right)

    return False

"""
Okay, so is there a "better" way to do this?

We could serialize the tree into a string, and then see if the subRoot string is in the root string!
        
        3                   4
    4       5           1       2
  1   2

If we serialized level-order into
34512 and 412
This wouldn't work

What about infix DFS?
14235  142
That would work!

Are there cases where it wouldn't work, where we'd have to note down the NONES in the serialization?

                3                   4
            2      5            1     2
        4
    1


This would be incorrect! So I think we need to record nulls in an infix dfs

For the FIRST example above, this would look like:R
$1$4$2$3$5$     $1$4$2$   This would work!

For the SECOND example above, this would look like:
$$14$2$35$$     $$142$$     This would work, in the sense that subRoot isn't a valid subtree :)
"""


def serialize(r: Optional[Node]) -> str:
    # This is an infix DFS, but I think it works with Prefix too. It's important that you mark $ if r is None.
    return serialize(r.left) + str(r.value) + serialize(r.right) if r is not None else "$"


def is_subtree_smarter(root: Optional[Node], subRoot: Optional[Node]) -> bool:
    if any([root, subRoot]) and not all([root, subRoot]):
        return False

    root_serialization = serialize(root)
    subroot_serialization = serialize(subRoot)

    # print(root_serialization, subroot_serialization)

    # This is still O(N^2), isn't it? "Is StringA in StringB" can be O(N) using the Knuth-Morris-Pratt (KMP) algorithm!
    return subroot_serialization in root_serialization

# -- Test Zone --
def test(fn):
    root = Node(3, Node(4, Node(1), Node(2)), Node(5))
    subRoot = Node(4, Node(1), Node(2))
    assert fn(root, subRoot) == True

    """
         3
    4          5                    4
1      2                        1       2
     0

    """
    root = Node(3, Node(4, Node(1), Node(2, Node(0))), Node(5))
    subRoot = Node(4, Node(1), Node(2))

    assert fn(root, subRoot) == False

test(is_subtree)
test(is_subtree_smarter)