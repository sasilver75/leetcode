from __future__ import annotations
from typing import Optional
"""
Remove Nth Node frmo End of List

Given the HEAD of a linked list, remove the NTH node from the end of the
list and return its head
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
        print(acc)
        return acc

def removeNthFromEnd(head: Optional[Node], n) -> Optional[Node]:
    # How many nodes are there in the list?
    k = 0
    cur = head
    while cur:
        k += 1
        cur = cur.next

    """
    If there are K nodes, how many steps do we need to take to get to the node
    before the node that we want to remove?
    Well the one we want to remove is 
    
    
    5 -> 2 -> 1 -> 4 -> 7 ->
    
    K=5, N=1 --> Take 3 steps to get to the node before the one we want to remove
    K=5, N=3 --> Take 1 step to get to the node before the one we want to remove
    K=5, N=4 --> Take 0 Steps to get to the node before the one we want to remove
    K=5, N=5 --> No steps needed, just return node.next (either None or a Node)  
    """
    cur = head

    if n == k:
        return cur.next
    # Take n-k-1 steps to the node before the one we want to remove
    for _ in range(k-n-1):
        cur = cur.next
    # Now remove the next node by stitching the current node's next "over" it
    cur.next = cur.next.next

    return head

# Tests
head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
assert removeNthFromEnd(head, 2).to_list() == [1,2,3,5]

head = Node(1)
assert removeNthFromEnd(head, 1) == None

head = Node(1, Node(2))
assert removeNthFromEnd(head, 1).to_list() == [1]

