"""
Given the "head" of a LL and an integer "val", remove all the
nodes of the linked list that has Node.val == val, and return
the new head.
"""
from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, value: int, next: Optional[ListNode] = None):
        self.value = value
        self.next = next


# [1,2,6,3,4,5,6], 6  --> [1,2,3,4,5]
def remove_elements(head: Optional[ListNode], target: int) -> Optional[ListNode]:
    # Remove the node from the head of the list as many times as needed, if there's a node at the head
    while head and head.value == target:
        head = head.next

    # If there's nothing in the list, return None
    if not head:
        return None

    lead = head.next
    follow = head
    while lead:
        if lead.value == target:
            lead = lead.next
            follow.next = lead
        else:
            lead = lead.next
            follow = follow.next
    return head


def get_val_list(head: Optional[ListNode]) -> list[int]:
    vals = []
    while head:
        vals.append(head.value)
        head = head.next
    return vals


# Case 1
head = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
print(f"Before: {get_val_list(head)}")
print(f"After: {get_val_list(remove_elements(head, 6))}") # [1,2,3,4,5]

# Case 2
head = None
print(remove_elements(head, 1)) # []

# Case 3
head = ListNode(7, ListNode(7, ListNode(7, ListNode(7))))
print(f"Before: {get_val_list(head)}")
print(f"After: {get_val_list(remove_elements(head, 7))}") # []


