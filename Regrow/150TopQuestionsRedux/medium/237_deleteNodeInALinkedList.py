from __future__ import annotations
from typing import Optional

"""
Delete Node in a Linked List

There's a singly-linked list `head`, and we want delete a node`node`

You're given the node to be deleted `node` -- you wil NOT be given
access to the first node of `head`.

All of the values of the linked list are UNIQUE, and it's guaranteed
that the given node `node` is NOT the last node in the list.

Delete the given node:
- The value of the given node should not exist in the LL
- The number of nodes in the LL should decrease by one
- All of the values before node should be in the same order
- ALl the values after node should be in the same order

The node to be deleted is in the list and is not a tail node

Don't return anything; modify the node in-place instead
"""

"""
THINKING:
This clearly seems like a trick question in some way

The "obvious" thing is to have node.prev.next point to node.next,
but we can't do that because we don't have prev access in a SLL.

We need to overwrite nodes, instead!
For each node n in range [node...lastNode]
    
cur = node
while cur:    
    - cur.value = cur.next.value (shift the value left)
    - cur = cur.next
But the last node has to set cur.value to None... or more specifically,
the second-to-last node needs to set it .next to None.

We have the guarantee above that `node` is NOT the last node in the linked list.
"""


class Node:
    def __init__(self, value: int, next: Optional[Node] = None):
        self.value = value
        self.next = next

    def as_list(self) -> list[int]:
        acc = []
        cur = self
        while cur:
            acc.append(cur.value)
            cur = cur.next
        print(acc)
        return acc


def delete_node(node: Node) -> None:
    cur = node
    while cur:
        cur.value = cur.next.value
        if cur.next.next == None:
            cur.next = None
        cur = cur.next


# -- Test --
def test(fn):
    # 4519 del(5)  419
    node = Node(5, Node(1, Node(9)))
    root = Node(4, node)
    fn(node)
    assert root.as_list() == [4, 1, 9]

    # 4519 del(1)  459
    node = Node(1, Node(9))
    root = Node(4, Node(5, node))
    fn(node)
    assert root.as_list() == [4, 5, 9]

test(delete_node)