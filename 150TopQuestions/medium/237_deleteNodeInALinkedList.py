from __future__ import annotations
from typing import Optional

"""
Delete Node in a Linked List

There's a singly-linked list with a `head`, and we want to delete ` node` in it.

You are given the `node` to be deleted.
You will NOT be given access to the first node of `head`

All the values of the linked list are UNIQUE, and it is guaranteed that the
given node `node` is NOT the last node in the linked list.

Delete the given node. Note that by deleting the node, we don't mean removing
it from memory. We mean:
1) The value of the given node should not exist in the linked list
2) The number of nodes in the linked list should decrease by one
3) All the values before `node` should be in the same order
4) All the values after `node` should be in the same order

"""


class Node:
    def __init__(self, val: int, next: Optional[Node] = None):
        self.val = val
        self.next = next

# This is super stupid.
"""
I think it's saying:

Given a reference to a node that is a non-tail node in a linked list,
how would we in-place (without returning anything) remove the node from the linked 
list?
We can do it as follows
"""
def deleteNode(node: Node) -> None:
    node.val = node.next.val
    node.next = node.next.next
