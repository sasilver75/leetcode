from __future__ import annotations
from typing import Optional

"""
Remove Nth Node from End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.

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
Duumy -> 1 -> 2 -> 3 -> 4 ->  5 ->
slow   fast

N=2 targets the "4" element
How many steps do we need to take to get our fast pointer to the target element?
If we consider "Number of Nodes" as 5, then N=2 takes 3 steps
                                     , then N=1 takes 4 steps
                                     , then N=3 takes 2 steps
So it's count-N steps to get fast to the deletion point
And then we "stitch over" fast, setting slow.next = fast.next
 

"""

# I'm assuming that we're going to be given a valid input
def remove_nth_node(head: Optional[Node], n: int) -> Optional[Node]:
    # Get number of nodes
    count = 0
    cur = head
    while cur:
        count += 1
        cur = cur.next

    # Prepend a dummy node to the list
    new_head = Node(None, head)

    # From OG head, how many steps to we need to take to get to the deletion node? count-n
    slow, fast = new_head, head
    for _ in range(count - n):
        slow = fast
        fast = fast.next

    # Stitch
    slow.next = fast.next

    return new_head.next


# -----
head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
assert remove_nth_node(head, 2).to_list() == [1, 2, 3, 5]

head = Node(1)
assert remove_nth_node(head, 1) == None

head = Node(1, Node(2))
assert remove_nth_node(head, 1).to_list() == [1]
