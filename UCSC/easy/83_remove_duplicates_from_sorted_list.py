"""
Given the `head` of a sorted list, delete all duplicate such that each elemnt
appears only once! Return thlinked list SORTED as well!
"""

from typing import Optional


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

def remove_duplicates_list(head: Node) -> Node:
    """
    To delete all duplicates, we're going to have to keep track of the
    elements that we're seen. This is best done by using a hashset...
    Except that it's a SORTED list, so we don't even need to use a hashsset

    What we can do is the same thing as we did for th remove duplicates in an array INPLACE
    But do it with a list, moving the values around
    So we have a left pointer and right pointer, and the left keept track of the latest uniqu element
    """
    left = head # The "tail" of alist of unique numbers
    right = head # Moving along teh list as normal

    while right is not None:
        # New number? Thread it as our new tail and move left to point at it
        if right.value != left.value:
            left.next = right
            left = left.next
        
        right = right.next
    
    # Clip off the end of the unique list, if it exists
    left.next = None

    # head should still be the head of the unique list
    return head


def print_list(head: Node) -> None:
    cur = head
    while cur is not None:
        print(cur.value)
        cur = cur.next

def generate_list(nums: list[int]) -> Optional[Node]:
    dummy = Node("Blah")
    cur = dummy
    for num in nums:
        newNode = Node(num)
        cur.next = newNode
        cur = newNode

    return dummy.next


print_list(remove_duplicates_list(generate_list([1,1,2])))
print_list(remove_duplicates_list(generate_list([1,2,3])))