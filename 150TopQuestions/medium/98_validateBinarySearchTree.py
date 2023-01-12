"""
Validate Binary Search Tree

Given the `root` of a binary tree, determine if it is a VALID BST

A valid BST is defined as follows:
* The left subtree of a node contains only nodes with keys LESS THAN the node's key
* The right subtree of a node contains only nodes with keys GREATER than the node's key
* Both the left and right subtrees must also be binary search trees

--> Q: What about identically-valued nodes? I'll say those need to be in the right subtree
"""
from __future__ import annotations

from typing import Optional


class Node:
    def __init__(self, value: int, left: Optional[Node] = None, right: Optional[Node] = None):
        self.value = value
        self.left = left
        self.right = right


"""
Okay, so the naive thing to do (which is just WRONG in this case)
would be to do something like:

At the current node, confirm that the BST rules are respected LOCALLY just
with respect to the current node and its two children.
Then recurse into the children.

That would work fine for a binary (possibly search) tree this:
                        5
                     3     10
                  .. ..   ..  ..

But when we recurse to the left into 3:
                        5
                3               10
            1     6          8      12
            
We see again that the rule is respected locally W.R.T. (1,3,6), however
the global rule is violated because 6 > 5, but 6 is in 5's left subtree!

So what information can we keep track of as we traverse down?
Do we keep track of some min and max value of above layers?
Let's try that...
            
"""


def validate_bst(root: Node) -> bool:
    violation = False

    def find_violation(cur: Node, min: int, max: int):
        """
        :param cur: Current Node
        :param min: Minimum ALLOWED Value (Must be >)
        :param max: Maximum ALLOWED Value (Must be <)
        :return: Boolean

        Rule Respected:
        min < cur.value < max

        Rule Violated:
        cur.value < min  or cur.value > max
        """
        nonlocal violation
        # Process Current Node: Do we violate bounds?
        if cur.value < min or cur.value > max:
            violation = True
            return

        # Recurse Left
        if cur.left:
            find_violation(cur.left, min, cur.value)
        # Recurse Right
        if cur.right:
            find_violation(cur.right, cur.value, max)

    find_violation(root, -float('inf'), float('inf'))

    return not violation


"""
Neetcode

We want to determine if it's a valid BinarySearchTree or not.

                    5
            3               7
                        4       8
                        
Is not a valid BST, because 4 is not greater than 5.

Brute force would be:
For each node cur:
    For each value in left subtree, make sure that value is less than cur
    For each value in right subtree, make sure that value is greater than cur
Which would be O(N*N) = O(N^2), since each node is compared with every other node
Can we do better than O(N^2)

Note that there aren't any restrictions on the root value.
So we can say that the root value can be any value between negative infinity and positive infinity.

When we go down to the left subtree, we need to check that 
          3 < 5 and 3 > negative infinity
Which is to say, when we recursed LEFT, we updated MAX to be the previously-cur .value

Assumedly when we recurse RIGHT, we update MIN to be the previously-cur .value
"""


def neetcode_validation(root: Node) -> bool:
    def valid(node, left, right):
        if not node:
            return True

        if not (left < node.value < right):
            return False

        return valid(node.left, left, node.value) and valid(node.right, node.value, right)

    return valid(root, float('-inf'), float('inf'))


# -- Test Zone --
head = Node(2, Node(1), Node(3))
assert validate_bst(head) == True

head = Node(5, Node(1), Node(4, Node(3), Node(6)))
assert validate_bst(head) == False
