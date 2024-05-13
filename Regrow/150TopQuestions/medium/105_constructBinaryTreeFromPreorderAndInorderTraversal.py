"""
Construct Binary Tree from Preorder and Inorder Traversal

Given two integer arrays `preorder` and `inorder`
where `preorder` is ht preorder traversal of a binary tree
and `inorder` is the inorder traversal of the binary tree

Construct and return the binary tree

Ex:
preorder = [3,9,20,15,7]
inorder: [9,3,15,20,7]

Output:
                        3
                9               20
                            15      7
"""
from __future__ import annotations
from typing import Optional

class Node:
    def __init__(self, value: int, left: Optional[Node] = None, right: Optional[Node] = None):
        self.value = value
        self.left = left
        self.right = right

"""
Leetcode tip:

There's an interesting property of the INORDER traversal:

                    3
                9       20
            1         15   7

                                    root
                                       _
                                [1, 9, 3, 15, 20, 7]
                                _____     _________
                               subtree      subtree  

We can leverage this property and find a way to recursively construct
the tree.

Two key observations:

1) Preorder traversal follows 
        Root -> Left -> Right
Therefore given the preorder array, we have each access to the root, preorder[0]

2) Inorder traversal follows
        Left -> Root -> Right
Therefore if we know the position of Root, we can recursively split
the entire array into two subtrees.

SO...
We will design a recursion function that:
 * Sets the first element of `preorder` as the root
 * then constructs the entire tree.
    * To find the left and right subtrees, it will look for the root in `inorder`
    * Everything on the left should be the left subtree, and everything on the right
    should be the right subtree.
    * Both subtrees (left and right) can be constructed by making another recursive call
    
It's worth noting -- while recursively construct the subtrees, we should choose
the NEXT ELEMENT in `preorder` to initialize as the new roots. This is because the 
current one has already been initialized to a parent node for the subtrees.
"""

def build_tree(preOrder: list[int], inOrder: list[int]) -> Node:
    """
                    3
                9       20
            1     2  15     7

    PREORDER: [3, 9, 1, 2, 20, 15, 7] (Use to choose Roots)
    INORDER: [1, 9, 2, 3, 15, 20, 7] (Use to determine left/right subtrees)
    """




# -- Test Zone
ans = build_tree([3,9,20,15,7], [9,3,15,20,7])

ans = build_tree([-1,], [-1])

print("Done!")