"""
Given the head of a sorted linked list, delete all duplicates
such that each element appears only once. return the linked list sorted
as well.
"""
from typing import Optional


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

"""
   1->2->3
       a ac c   
# [1,1,2,3,3] -> [1,2,3]
"""
def without_duplicates(head: Node) -> Node:
    # Singly Linked List is already Sorted
    anchor = head
    cur = head
    while cur:
        # If cur a new value, point to it!
        if cur.value != anchor.value:
            # When we see a new value, point cur to it, then set cur to be anchor
            anchor.next = cur
            anchor = cur
        # Progress cur
        cur = cur.next

    # At the end, anchor will be the last unique value and cur will have progressed off the chain.
    anchor.next = None
    return head


def construct_linked_list(lst: list) -> Optional[Node]:
    if not lst:
        return None
    head = Node(lst[0])
    cur = head
    for el in lst[1:]:
        node = Node(el)
        cur.next = node
        cur = node
    return head

def print_linked_list(head: Node):
    cur = head
    while cur:
        print(cur.value, end=", ")
        cur = cur.next
    print()


head_case_1 = construct_linked_list([1,1,2])
head_case_2 = construct_linked_list([1,1,2,3,3])

print_linked_list(without_duplicates(head_case_1))
print_linked_list(without_duplicates(head_case_2))
