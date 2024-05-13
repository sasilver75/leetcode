from __future__ import annotations
from typing import Optional
"""
Construct Binary Tree from Preorder and Inorder Traversal
Category: Tree [Some people say this ought to be a Hard]

Given two integer arrays `preorder` and `inorder` where `preorder` is the
preorder traversal of a binary tree, and `inorder` is the inorder traversal
of the same tree, construct and return the binary tree!

                3
        9               20
                    15      7

preorder: [3, 9, 20, 15, 7]
inorder: [9, 3, 15, 20, 7]
"""



class Node:
    def __init__(self, value: int, left: Optional[Node] = None, right: Optional[Node] = None):
        self.value = value
        self.left = left
        self.right = right

# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solutions/34543/simple-o-n-without-map/
def construct_tree(preorder: list[int], inorder: list[int]) -> Optional[Node]:
    def build(stop):
        if inorder and inorder[-1] != stop:
            root = Node(preorder.pop())
            root.left = build(root.val)
            inorder.pop()
            root.right = build(stop)
            return root
    preorder.reverse()
    inorder.reverse()
    return build(None)

def test(fn):
    ans1 = fn([3,9,20,15,7], [9,3,15,20,7])
    ans2 = fn([-1], [-1])
    print("Done!")
