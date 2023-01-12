from __future__ import annotations
from typing import Optional

"""
Linked List Cycle

Given head, the had of a linked list, determine if
the linked list has a cycle in it.
"""


class Node:
    def __init__(self, value: int, next: Optional[Node] = None):
        self.value = value
        self.next = next


"""
Insight: There's this thing called Floyd's Cycle Finding Algorithm
It's in the category of "fast-slow pointer" or "hare-tortoise" algorithms.

It's used to find the loop in a linked list!
Two things may happen:
1) The fast pointer may reach the end (hit a NULL), showing no loop in the list
2) The fast pointer may catch the slow pointer at some time, showing a loop!

The insight is that while the fast pointer moves 2 nodes at a time and the slow
only at 1 node at a time, the fast node moves 1 node RELATIVE to the slow one.

Think about why we couldn't just have a stationary slow one at the head and
a "fast" one that moves only 1 at a time! It's because if there's a loop that 
begins later on in the chain, the fast one will cycle endlessly around it, never
encountering the slow one.  
"""


def has_cycle(node: Node) -> bool:
    slow, fast = node, node
    while fast:
        slow = slow.next
        fast = fast.next.next if fast.next else fast.next  # 2 if you can, 1 if you can't
        if fast and fast == slow:  # To catch for Case 3
            return True
    return False


# Case 1
a1 = Node(3)
b1 = Node(2)
c1 = Node(0)
d1 = Node(-4)
a1.next = b1
b1.next = c1
c1.next = d1
d1.next = b1
assert has_cycle(a1) == True

# Case 2
a2 = Node(1)
b2 = Node(2)
a2.next = b2
b2.next = a2
assert has_cycle(a2) == True

# Case 3: Problem with this one is both nodes "meet" at None, off the end of the chain
a3 = Node(1)
assert has_cycle(a3) == False
