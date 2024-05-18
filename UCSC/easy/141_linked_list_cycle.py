"""
Given `head`, the head of a linked list, determine if the linked list has a cycle in it!
"""

from typing import Optional


class Node:
    def __init__(self, value: int, next: Optional['Node'] = None):
        self.value = value
        self.next = next



