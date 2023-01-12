"""
Given the heads of TWO singly linked lists headA and headB,
return the node at which the two lists intersect.
If the two lists have NO intersection, return NULL.

        a1   -   a2   \
                        c1  -   c2  -  c3
    b1 -  b2  -   b3  /

Above: c1

Note these there are no cycles in these structures.
Note that the LLs must retain their original structure after the function returns
"""
from __future__ import annotations
from typing import Optional

"""
Thinking:
So there are two heads, so I'm thinking we'll in some way have two pointers,
and be walking them along.

An easy thing to do would be to keep a set of the visited nodes. Since 
we know there aren't going to be cycles in the graph, we can just check if the 
node that we're at with either pointer has been visited. You can walk the pointers one 
at a time or walk them "together," it's still gonna be O(N) either way.

Otherwise we could do two whole walks through the list with two pointers, mutating
a new .seen property on nodes that we've seen. Then whenever we already encounter
a node with a .seen, we know we're at an intersection. Afterwards, do another pass
through to clean up the added properties. While this doesn't entail the use of a "seaprate
data strucutre" like a set in the previous example, the amount of memory used (new properties)
still grows O(N), so it's not any better.
"""

class Node:
    def __init__(self, value: int, next: Optional[Node] = None):
        self.value = value
        self.next = next

def intersect(a1: Node, b1: Node) -> None:
    """Prints intersection node value"""
    seen = set()
    cur_a = a1
    cur_b = b1
    # While there are still nodes to process
    while cur_a or cur_b:
        # If we haven't run off the tail for a
        if cur_a:
            # If we've seen this node before, we've found intersection!
            if cur_a in seen:
                print("FOUND: ", cur_a.value)
                return # exit
            else: # We haven't seen this node. Mark it and continue
                seen.add(cur_a)
                cur_a = cur_a.next
        # If we haven't run off the tail for b
        if cur_b:
            # If we've seen this node before, we've found intersection!
            if cur_b in seen:
                print("FOUND: ", cur_b.value)
                return # exit
            else: # We haven't seen this node. Mark it and continue
                seen.add(cur_b)
                cur_b = cur_b.next

    print("No intersection found")

"""
Can we do this using O(1) time complexity though?
The idea is that we want to make sure that the two pointers reach the intersection 
node at the same time...
We can use TWO iterations to do that.
In the first iteration, we reset the point of one LL to the head of the other LL after 
it reaches the tail node.
In the second iteration, we move both pointers until they point to the same node...

I think another way of saying this is to connect the a pointer (after the null point at the end of the link)
to the head of the "B" list
And the b pointer ot hte head of the "A" list, after it's null.
And then we just need racing them around while they both don't equal null.

--------------------
Here's the NeetCode explaination:
          a1     a2
                       c1   c2   c3
   b1     b2     b3
   
One of these lists is longer the other. The "a1" list has 5 elements, while
the "b1" list has 6 elements. If they DO intersect, we know that the END (tail)
of the list will be the exact same.

So what we could do is:
* First determine the length of each of the LL chains by walking from their root
    - 5 (a) and 6 (b)
* Reset the pointers to Head
* Increment the longer chain's pointer by the DIFFERENCE between the lengths (1)
* Then, do a two-pointer lockstep stepthrough of each of the chains. Since they
are both moving at the same speed, and start the same distance from the end, they should
reach instersecting nodes at the same time, if they exist.
"""

def intersection(a1: Node, b1: Node) -> None:
    a_length = get_chain_length(a1)
    b_length = get_chain_length(b1)
    diff = abs(a_length - b_length)

    a_cur = a1
    b_cur = b1
    if a_length > b_length:
        while diff:
            a_cur = a_cur.next
            diff -= 1
    if b_length > a_length:
        while diff:
            b_cur = b_cur.next
            diff -= 1

    # Pointers are now equidistant frmo the ends of their respective lists, whether they intersect or not
    # We can now walk them in lockstep until they equal eachother (whether at Nones, in the case of non-intersecting, or at the first intersecting node)
    while (a_cur != b_cur):
        a_cur = a_cur.next
        b_cur = b_cur.next

    # Both point to the same thing -- either a Node or None
    if a_cur and b_cur and a_cur == b_cur: # "and b cur" is not needed, really
        print("Found intersection: ", a_cur.value)
    else:
        print("No Intersection")



def get_chain_length(head: Node) -> int:
    count = 0
    cur = head
    while cur:
        count += 1
        cur = cur.next
    return count


# Case 1
"""
4   1 
            8  4   5
5   6   1

"""
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
intersection(a1, b1) # 8

# Case 2
a1 = Node(1)
a2 = Node(9)
a3 = Node(1)
b1 = Node(3)
c1 = Node(2)
c2 = Node(4)
a1.next = a2
a2.next = a3
a3.next = c1
b1.next = c1
c1.next = c2
intersection(a1, b1) # 2

# Case 3
a1 = Node(2)
a2 = Node(6)
a1 = Node(4)
b1 = Node(1)
b2 = Node(5)
a1.next = a2
a2.next = a3
b1.next = b2
intersection(a1,b1) # No intersection


