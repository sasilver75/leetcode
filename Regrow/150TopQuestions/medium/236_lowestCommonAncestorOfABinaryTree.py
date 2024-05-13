from __future__ import annotations
from typing import Optional
"""
Lowest Common Ancestor of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes
in the tree!

According to the definition of LCA on Wikipedia:
"The lowest common ancestor is defined between two nodes p, q as the lowest node
in T that has both p and q as descendants (where we DO ALLOW a node to be
a descendant of itself!).
"""

class Node:
    def __init__(self, value: int, left: Optional[Node] = None, right: Optional[Node] = None):
        self.value = value
        self.left = left
        self.right = right


"""

I think we might be able to do a traversal of the tree...
I think it might be a POST-ORDER traversal (either depth or breadth)...
or is it a PRE-ORDER?

The condition that we're looking for, for the closest ancestor would be:
            ANCESTOR
        PorQ            QorP
        
            ANCESTOR(PorQ)                 or      ANCESTOR(PorQ)
         _               QorP                   QorP                _
         

There can also be significant distance between Ancestor and P/Q  
                            ANCESTOR
                        _           _
                    _      P      _     Q
                    
        

So it's:
_ First Process? Check for immediate to exit early
1) Recurse Left
2) Recurse Right
3) Process Current Node
    : If all(target in (node, node.left, node,right) for taget in (p,q):
            return currentNode.value

Hmmm that's not quite it, is it?

Neetcode:
We're supposed to find the LOWEST COMMON ANCESTOR of two given nodes
Basically defined as the lowest node in the tree such that P and Q are 
descendants of this node, or P and Q happen to be EQUAL to the node.

                6
        2               8
    0       4       7       9
          3   5

p=2, q=8

In this example, we'll start at the Root, since the root is always 
going to be a common ancestor of any two nodes in the tree. Easy :)

It isn't necessarily the lowest common ancestor, though.

In our example:
    * p=2 is in the left subtree of the root, and happens to
    be the immediate left child of the root.
    * q=8 is in the right subtree of hte root, and happens to be 
    the immediate right child of the root.

INSIGHT: We know that 2 can't be the ancestor of 8 (or vice versa), since
they're in different subtrees of the current node!

Oh, this is giving me an idea. Let's pause at 2:28 and code it out.
"""

def lca_on_bst_only(root: Node, p: int, q: int) -> Node:
    """
    Ah damn, this only works if it's a binary search tree! We don't have a
    way of knowing whether p/q will be on left/right sides of the current
    node in just a regular old binary tree :(

    This DOES work for binary search trees though, and was a good implementation!
    Nice!
    """
    def helper(cur: Node) -> Node:
        # If the root has p and q evenly divided between subtrees (or the root itself is p or q) and one subtree
        if any([
            p <= root.value < q,
            q <= root.value < p,
            p < root.value <= q,
            q < root.value <= p
        ]):
            return cur

        if cur.left:
            helper(cur.left)
        if cur.right:
            helper(cur.right)

    lca_node = helper(root)

    return lca_node.value

"""
Let's talk about just LCA of a Binary Tree :), NOT a Binary Search Tree

                    3
            5               1
        6       2       0       8
              7   4

p=5,q=1 --> Return 3
p=5, q=4 --> Return 5
p=2, q=7 --> Return 2

The LCa is the LOWEST (height) node in T that has both p and q as 
descendants, where we allow a node to be a descendant of itself.

This problem is relatively simple, in that there are only three cases
that can occur (and they're in the examples above)

1) The two nodes will be on opposite sides of the tree. We want to find
the node with those p,q as immediate children.
2) Where q is a descendant of p, meaning p is our LCA
3) Where p is a descendant of q, meaning q is our LCA

Those are our three cases! :) 
We want to do a depth-first search through our tree, looking 
on each side of the root node for either p or q.
We return when we find EITHER p or q in either side (one call of this on either side of root)

There are three cases:
1) We find p in the left subtree and q in the right subtree
* Therefore root is the answer
2) We find p in (ex) the left subtree and nothing in the right subtree
* therefore p is an ancestor of q, and p is the answer
3) We find q in (ex) the left subtree and nothing in the right subtree
* therefore q is an ancestor of p, and q is the answer

Wait, does this answer something liek this?
                        3
                4               6
        5             2
    1                     5

where our p and q are (1, 5)? The answer should be 4. But I don't think it 
is from the rules above.
>>> It does! read the code below :) 
"""

"""
                3
    5)                   1   
6       2             0     8
      7    4)
"""
def lca_on_binary_tree(root: Node, p: int, q: int) -> Node:
    if root is None:
        return None

    if root.value == p or root.value == q:
        return root

    # Now we need to go in the tree left/right subtrees
    l = lca_on_binary_tree(root.left, p, q)
    r = lca_on_binary_tree(root.right, p, q)

    # if l and r are both non-null, current node has to be LCA
    if l and r:
        return root
    # If just l, then l must be the ancestor
    elif l:
        return l
    # If just r, then r must be the ancestor
    elif r:
        return r
    # If we're at a leaf node that's a dead end, it's possible that l and r are both None
    else:
        return None









def test(fn):
    """
                3
    5
 6      2
      7   4
    """
    root = Node(3, Node(5, Node(6), Node(2, Node(7), Node(4))), Node(1, Node(0), Node(8)))
    assert fn(root, 5, 1).value == 3 # The lca of nodes 5 and 1 is 3

    """
                    3
        5                       1
    6       2               0       8
          7    4
    """
    root = Node(3, Node(5, Node(6), Node(2, Node(7), Node(4))), Node(1, Node(0), Node(8)))
    assert fn(root, 5, 4).value == 5 # The LCA of nodes 5 aand 4 is 5, since a node CAN be a descendant of itself according to the LCA definition

    """
        1
            2
    """
    root = Node(1, None, Node(2))
    assert fn(root, 1, 2).value == 1

test(lca_on_binary_tree)
