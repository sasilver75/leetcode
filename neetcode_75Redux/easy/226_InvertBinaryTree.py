"""
Invert Binary Tree

Given the ROOT of a binary tree, INVERT
the binary tree, and return its root!

Example:
        4                           4
    2       7           ->      7       2
1     3   6    9            9     6    3   1

{So this really seems more like "rotate around the Y axis"}
"""

"""
Thinking:
So I think what we need to do locally is :

Rotate-In-Place the left node's subtree
Rotate-In-Place the right node's subtree
Swap left/right nodes

Recursively, do this.
"""