from __future__ import annotations
from typing import Optional

"""
Given the heads of two singly linked lists headA and headB, return
the node at which two lists intersect! If the two linked lists have no 
intersection at all, return null!

For example, the following linked lists begin to intersect at node c1
  
    a1  ->  a2
                \
                c1 -> c2 -> c3
                /
b1 -> b2 -> b3

NOTE that the linked lists must maintain theri original structure
after the function returns!
"""


class Node:
    def __init__(self, value: int, next: Optional[Node] = None):
        self.value = value
        self.next = next


"""
Thinking:

One dumb way would be to have a "slow chain" and a "fast chain," essentially
doing a double-nested loop where when we advance a pointer one spot in slow
chain, we run through the entire fast chain looking for an intersection.
That would be O(N^2) time and O(1) memory

    a1  ->  a2
                \
                c1 -> c2 -> c3
                /
b1 -> b2 -> b3

Observation 1:
Both lists share the same tail nodes c1, c2, c3.
These tail nodes are identical in value and quantity.

Observation 2:
We really would like it if both of the chains were the same length, wouldn't
we? That's like... the hard part. Because imagine if they were the same length!
We'd just take a pointer on each chain and walk them down at the same speed -- we'd
be GUARANTEED to have the two pointers touch at the intersection point.

So... Can we synthetically extend the shorter of the two chains?

"""


def intersection(node1: Node, node2: Node) -> Optional[Node]:
    # Get the length of each chain
    cur1 = node1
    count1 = 0
    while cur1:
        count1 += 1
        cur1 = cur1.next

    cur2 = node2
    count2 = 0
    while cur2:
        count2 += 1
        cur2 = cur2.next

    # Extend the shorter chain to be the same length as the longer chain
    # Generate a chain of length (diff)
    diff = abs(count1 - count2)
    if diff:
        dummy = Node(None)
        d_cur = dummy
        while diff:
            d_cur.next = Node(None)
            d_cur = d_cur.next
            diff -= 1

        # Prepend the chain to the shorter of the two chains
        if count1 > count2:
            d_cur.next = node2
            node2 = dummy.next
        else:
            d_cur.next = node1
            node1 = dummy.next

    # Walk two pointers in lockstep down each chain, looking for intersection
    while node1 and node2:
        if node1 == node2:
            return node1
        node1 = node1.next
        node2 = node2.next

    # At least one of the two chains has been exhausted without intersection
    return None



# Case 1
a1 = Node(4)
a2 = Node(1)
b1 = Node(5)
b2 = Node(6)
b3 = Node(1)
c1 = Node(8)
c2 = Node(4)
c3 = Node(5)
a1.next = a2
a2.next = c1
b1.next = b2
b2.next = b3
b3.next = c1
c1.next = c2
c2.next = c3
assert intersection(a1, b1) == c1

# Case 2
x1 = Node(1)
x2 = Node(9)
x3 = Node(1)
y1 = Node(3)
z1 = Node(2)
z2 = Node(4)
x1.next = x2
x2.next = x3
x3.next = z1
y1.next = z1
z1.next = z2
assert intersection(x1, y1) == z1

# Case 3
i1 = Node(2, Node(6, Node(4)))
j1 = Node(1, Node(5))
assert intersection(i1, j1) == None

# Follow up: Could you solve in O(m + n) time and  O(1) memory?
