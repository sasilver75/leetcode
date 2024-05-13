from __future__ import annotations
from typing import Optional

"""
Lowest Common Ancestor of a Binary Search Tree
Category: Tree

Given a BINARY SEARCH TREE (BST), find the loweset common ancestor (LCA) node
of two given nodes in the BST.

According to the definition of LCA on Wikipedia:
The LCA is defined between two nodes `p` and `q` as the lowest node in `T` that
has both `p` and `q` as descendants (swhere we allow a node to be a descendant of
itself).
"""


class Node:
    def __init__(self, value: int, left: Optional[Node] = None, right: Optional[Node] = None):
        self.value = value
        self.left = left
        self.right = right


"""
Thinking:

Where are P and Q?
    - Both P and Q are in the same subtree (say: left)
        - One is in the subtree of the other
            ! Meaning the "higher" of the two is the LCA
        - Neither are in the subtree of the other
            -> Meaning that the LCA is somewhere in the (say) left subtree
                - So recurse left. At some point, one of the other cases will be true.
    - P and Q are in opposite subtrees of the current node
        ! The current node is the LCA
        
In the best case this would be O(N) as we traverse down the tree and see that they're either
both in opposite subtrees or one of them is obviously hte LCA of both.

                    root
            ()              ()
        (p)      ()       ()     ()             Case 1
     (q)   ()  ()  ()   ()  ()  ()  ()
     
     
                    root
            (p)              (q)
        ()      ()       ()     ()              Case 2
     ()   ()  ()  ()   ()  ()  ()  ()
     
     
                    root
            ()              ()
        (p)      (q)       ()     ()            Case 3  (In no particular order)
     ()   ()  ()  ()   ()  ()  ()  ()
     
      

"""


def search(n: Optional[Node], p: Node, q: Node) -> list[Node]:
    # Search for either P, Q
    if n is None:
        return []

    if n in [p, q]:
        return [n]

    left_search = search(n.left, p, q)
    right_search = search(n.right,p,q)

    return [*left_search, *right_search]



def lowest_common_ancestor(root: Node, p: Node, q: Node) -> Node:
    if root in [p, q]:
        return root

    left_search = search(root.left, p, q)
    right_search = search(root.right, p, q)

    # Both in Left or Right subtree; recurse into that side
    if len(left_search) == 2:
        return search(root.left, p, q)
    if len(right_search) == 2:
        return search(root.right, p, q)

    # Root is LCA
    if len(right_search) == 1 and len(left_search) == 1:
        return root

    # Q is a child of P or P of Q. The only found one is the
    if len(left_search) == 1 and len(right_search) == 0:
        return left_search[0]
    if len(right_search) == 1 and len(left_search) == 0:
        return right_search[0]


# -- Test --
p = Node(2, Node(0), Node(4, Node(3), Node(5)))
q = Node(8, Node(7), Node(9))
root = Node(6, p, q)
assert lowest_common_ancestor(root, p, q) == root

q = Node(4, Node(3), Node(5))
p = Node(2, Node(0), q)
root = Node(6, p, Node(8, Node(7), Node(9)))
assert lowest_common_ancestor(root, p, q) == p

q = Node(1)
root = p = Node(2, q)
assert lowest_common_ancestor(root, p, q) == p
