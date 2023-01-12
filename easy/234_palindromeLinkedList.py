"""
Given the HEAD of a singly linked list,
return TRUE if it is a palindrome, or FALSE otherwise.
"""
from __future__ import annotations
from typing import Optional

"""
Thinking:
Usually, with a palindrome check on a list, we have two pointers
that we walk in backwards towards eachother.

Because this is a singly linked list, we've lost the ability to do that
reverse stepping.

What we COULD do is an O(N^2) type thing...
Where for each node 0...n-1 in chain of length n, 
we step forward to look at the  len(chain)-1-i 'th node, which is the corresponding node on the 
other "side" of the chain...

    0  1  2  3  4     length=5
    
Okay, so that's like O(N^2) with O(1) Memory.

----
There's an O(N) time and O(N) memory solution too!
We want to compare the first node to the last node, the second node to the 
second last node, the third node to the third last node, etc.

Can we first traverse the list, and insert the values as we go into 
some sort of data structure that can give us the values "back" in reverse
order to what they were added in? Wait... that's "LIFO", isn't it?
We can use a stack!

So traverse the list, adding values as you go into a stack.
Then, traverse the list again, comparing each value to the popped value from the stack,
which is the "mirrored/comparison" value for the current node.

0 -> 1 -> 2 -> 3 -> 4     Stack:  BOTTOM 0,1,2,3,4 TOP
----

Theres... another solution too, which is O(N) time and O(1) space, as long
as we're allowed to modify the list. Read to the next section to see it!
"""

class Node:
    def __init__(self, value: int, next: Optional[Node] = None):
        self.value = value
        self.next = next

def is_palindrome(head: Node) -> bool:
    stack = []
    cur = head
    while cur:
        stack.append(cur.value)
        cur = cur.next
    cur = head
    while cur:
        cur_val = cur.value
        if cur_val != stack.pop():
            return False
        cur = cur.next
    return True

"""
There's actually another way that we could do this -- one 
that runs in O(N) time and O(1) space!
It's a little tricky though, and it requires being able to mutate the 
linked list, assuming we want to have O(1) space usage.

Here's an example

        0  ->  2  ->  1  ->  1 ->  2 -> 0
        
What we do...

Is we walk one pointer from head out to the end of the list, counting the length as you go

                                        V
        0  ->  2  ->  1  ->  1 ->  2 -> 0   (Steps = 5) -> "While cur.next ... step+=1

Is we walk from head to the MID by taking (Steps // 2) steps (2)

                      V                 
        0  ->  2  ->  1  ->  1 ->  2 -> 0
                     MID
                     
Except while we do that walk... we REVERSE the list too!

                      v      v        
        0  <-  2  <-  1      1  -> 2 -> 0
                     MID
    
    Except before we reverse the mid element, we also set a second
    pointer at the .next element
    
    Now we've got two linked lists, and we can walk them!
    
    
    One snaggle:
    What if we had an odd-lengthed list?
    
    0 -> 2 -> 1 -> 6 ->  1 -> 2 -> 0
    
    1) Walk the list, get the length. Length = 7, Steps = 6
    
    2) mid = Steps / 2 steps MINUS ONE == 6/2 - 1 = 2 
              v
    0 -> 2 -> 1 -> 6 -> 1 -> 2 -> 0
              MID
    
    Reversing along the way. But then set the second pointer to be 
    cur.next.next, before reversing the lsat one!
                      
              V       V
    0 <- 2 <- 1  6 -> 1 -> 2 -> 0
    
    Now walk them in lockstep again.
    
    **NOTE**
    There's actually a better way to determine the midpoint of a linked 
    list, which is the so-called "fast-slow" method! You walk two pointers
    rightwards from the head. One moves "fast" (2 jumps, if possible), and hte
    other moves "slow" (1 jump).
    When the fast node reaches the TAIL node (or the None just after it), the
    slow node should be at the middle node.
    
    THEN, follow the instructions below! 
    https://leetcode.com/problems/palindrome-linked-list/discuss/1137027/JS-Python-Java-C%2B%2B-or-Easy-Floyd's-%2B-Reversal-Solution-w-Explanation
    
    Here's my interpretation of it
    1) Okay, so do the fast/slow method to find the midpoint.
    At this point, we've got our midpoint pointer, and we've got a 
    pointer that's walked either to the tail node (odd length list) or 
    to the None at the end of the linked list.
    2) From the midpoint, walk to the right, reversing nodes,
    until you get to the tail node.
    3) Now, we've got a linkedlist where each of the head/tail point
    inwards towards the midpoint, and we have a pointer at the "end"
    of the list.
    4) Set a new pointer to the head of the list
    5) Walk the two pointers inward until one/both of them 
    reach the mid node (which we've saved in a register)

"""

# This is from Leetcode -- doesn't seem to actually work.
def isPalindrome(head: Node) -> bool:
    slow, fast, prev = head, head, None
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    prev, slow, prev.next = slow, slow.next, None
    while slow:
        slow.next, prev, slow = prev, slow, slow.next
    fast, slow = head, prev
    while slow:
        if fast.val != slow.val: return False
        fast, slow = fast.next, slow.next
    return True

# Case 1
head = Node(1, Node(2, Node (2, Node(1))))
print(is_palindrome(head)) # true

# Case 2
head = Node(1, Node(2))
print(is_palindrome(head)) # false