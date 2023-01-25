from __future__ import annotations
from typing import Optional, Iterable

"""
LCA of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA)
of two given nodes in the tree.

According to the definition of LCA on Wikipedia: "The lowest
common is defined between two nodes p and q as
the lowest node in T that has both p and q as descendants
(where we allow a node to be a descendant of itself)
"""


class Node:
    def __init__(self, value: int, left: Optional[Node] = None, right: Optional[Node] = None):
        self.value = value
        self.left = left
        self.right = right


"""
Insight: 
- There are only a few different ways that this could go down
1.  p and q are in different subtrees of the root
    - The root is the LCA
2. p and q are in the same subtree, and either p/q is in the subtree of the otehr
    - The "higher" of the two nodes is the LCA
3. p and q are in the same subtree, but they aren't in the subtree of eachother
    - The LCA is somewhere in that subtree... Recurse into that subtree of the root?
    - Optimization: Alternatively maybe when we found p/q we also returned the "path" that we traveled through, and having both the path of P/Q, we can just pluck out the last element of the common path, which would be the LCA

We need:
- A search function that searches a tree for two values, p, q. If it finds either
p or q, it doesn't continue search "below" that node (ie its subtree)
            
            0
        1       4   
    2     3   5   7

So if I asked for p=1,q=3 on this tree, it would only find p=1
   if I asked for p=1 q=4, it would find both p=1 and q=4
.

"""


def count_not_none(it: Iterable):
    count = 0
    for el in it:
        if el is not None:
            count += 1
    return count


def first_not_none(it: Iterable) -> Optional[any]:
    for el in it:
        if el is not None:
            return el


def lca(root: Node, p: Node, q: Node) -> Node:
    def search_for_p_and_q(node: Optional[Node]) -> list[Node]:
        found = [None, None]
        if node is None:
            return found

        # Do any sort of search through the tree
        node_stack = [node]
        # While we have nodes to explore and we haven't found both nodes already
        while node_stack and not all(found):
            node = node_stack.pop()

            # Process Node
            if node == p:
                found[0] = node
            elif node == q:
                found[1] = node
            # Continue exploring only if we didn't find p or q here
            else:
                if node.left:
                    node_stack.append(node.left)
                if node.right:
                    node_stack.append(node.right)

        return found

    leftp, leftq = search_for_p_and_q(root.left)
    rightp, rightq = search_for_p_and_q(root.right)

    # Case: Both found in one of the trees; Recurse
    if leftp and leftq:
        return lca(root.left)
    if rightp and rightq:
        return lca(root.right)

    # Case: One found in each subtree; LCA is root
    if count_not_none([leftp, leftq]) == 1 and count_not_none([rightp, rightq]) == 1:
        return root

    # Case: Only one found; that node is the LCA
    if count_not_none([leftp, leftq, rightp, rightq]) == 1:
        return first_not_none([leftp, leftq, rightp, rightq])


def test(fn):
    """
                3
        5               1
    6      2        0      8
          7 4

    """
    p = Node(5, Node(6), Node(2, Node(7), Node(4)))
    q = Node(1, Node(0), Node(8))
    root = Node(3, p, q)
    assert fn(root, p, q).value == 3

    """
                    3
          5                     1
     6       2             0        8
           7   4
    """
    q = Node(4)
    p = Node(5, Node(6), Node(2, Node(7), q))
    root = Node(3, p, Node(1, Node(0), Node(8)))
    assert fn(root, p, q).value == 5


test(lca)
