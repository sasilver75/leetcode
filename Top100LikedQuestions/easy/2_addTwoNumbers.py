"""
Given two non-empty linked lists representing two non-negative integers.

The digits are stored in reverse order, with each of their nodes containing
a single digit.

Add the two numbers and return the sum as a linked list

You may assume that the two numbers DO NOT contain any leading zero, except
the number 0 itself
"""
from __future__ import annotations
from typing import Optional


class Node:
    def __init__(self, value: int, next: Optional[Node] = None):
        self.value = value
        self.next = next

    def as_list(self):
        acc = []
        cur = self
        while cur:
            acc.append(cur.value)
            cur = cur.next
        return acc

    def get_number(self):
        digits = self.as_list()
        return "".join([str(el) for el in digits[::-1]])

    @classmethod
    def from_list(cls, nums: list[int]):
        dummy = Node(None)
        cur = dummy
        for n in nums:
            new_node = Node(n)
            cur.next = new_node
            cur = new_node
        return dummy.next




"""
Think:
Say we're adding 342 and 564 = 906
How would we do this, abstracted from code?

We add the ones place (2+6) = 6 with no carry
We add the tens place (4+6) = 0 with 1 carry
We add the hundreds place (3+5) = 8 + 1 carry = 9 with no carry

So we get 906!

We're given these numbers "reversed," so we just need to process the lists in lockstep left to right, I think

The easiest case is this pair of lists
(2) -> (4) -> (3) ->
n1
(5) -> (6) -> (4) -> 
n2

(dummy) -> 
cur

And just move them across while you have n1 and n2


"""
def add_two_numbers(l1: Optional[Node], l2: Optional[Node]) -> Optional[Node]:
    dummy = Node(None)
    cur = dummy
    carry = 0
    while l1 and l2:
        _sum = l1.value + l2.value + carry
        val = _sum % 10
        carry = _sum // 10

        next_node = Node(val)
        cur.next = next_node
        cur = next_node

        l1 = l1.next
        l2 = l2.next

    while l1:
        _sum = l1.value + carry
        val = _sum % 10
        carry = _sum // 10

        next_node = Node(val)
        cur.next = next_node
        cur = next_node

        l1 = l1.next


    while l2:
        _sum = l2.value + carry
        val = _sum % 10
        carry = _sum // 10

        next_node = Node(val)
        cur.next = next_node
        cur = next_node

        l2 = l2.next

    if carry:
        next_node = Node(carry)
        cur.next = next_node

    return dummy.next





# Adding 342 and 564
l1 = Node(2, Node(4, Node(3)))
l2 = Node(5, Node(6, Node(4)))
a1 = add_two_numbers(l1, l2)
assert a1.get_number() == "807" # 342 + 465 = 807

l1 = Node(0)
l2 = Node(0)
a2 = add_two_numbers(l1, l2)
assert a2.get_number() == "0"

l1 = Node.from_list([9,9,9,9,9,9,9])
l2 = Node.from_list([9,9,9,9])
a3 = add_two_numbers(l1, l2)
assert a3.get_number() == "10009998"