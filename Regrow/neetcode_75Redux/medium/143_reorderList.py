from __future__ import annotations
from typing import Optional

"""
Reorder List

Given the head of a singly linked list:

The list can be represented

L0 -> L1 -> ... -> Ln-1 -> Ln

Reorder the list to be on the following form:
L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...

You can not modify the values in the list nodes; only the nodes themselves may be changed.

"""


class Node:
    def __init__(self, value: int, next: Optional[Node] = None):
        self.value = value
        self.next = next

    def to_list(self):
        acc = []
        cur = self
        while cur:
            acc.append(cur.value)
            cur = cur.next
        return acc


"""
I think the move here is to take 

1 -> 2 -> 3 -> 4 -> 5       [Answer: 1 5 2 4 3 ]

Find the middle

1 -> 2 -> 3 -> 4 -> 5 -> 
          ^

And reverse the second half of it

1 -> 2 -> 5 -> 4 -> 3 ->  
^         ^

Then march your pointers rightwards len(nodes)//2  (+1 one more on the right if odd length)
and create the final list
1 -> 5 -> 2 -> 4 -> 3 ->
"""


def reorder_list(head: Node) -> Node:
    # Count number of nodes
    # Walk to middle node (and drag one behind) by talking count//2 steps
    # Reverse the list starting at middle (and use the dragged behind to point to returned value)
    # Set lhead to head, rhead to dragged.next
    # while lhead != dragg.next:
    # march them left right to right, adjusting next pointers
    pass


head = Node(1, Node(2, Node(3, Node(4))))
assert reorder_list(head).to_list() == [1, 4, 2, 3]
head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
assert reorder_list(head) == [1, 5, 2, 4, 3]


