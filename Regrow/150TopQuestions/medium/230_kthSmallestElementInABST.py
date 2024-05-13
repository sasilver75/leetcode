from __future__ import annotations
from typing import Optional
"""
Kth Smallest Element in a BST

Given the `root` of a binary search tree, and an integer `k`, return the
`kth` smallest value (1-indexed) of all of the values of the nodes
in the tree!
"""

class Node:
    def __init__(self, value: int, left: Optional[Node] = None, right: Optional[Node] = None):
        self.value = value
        self.left = left
        self.right = right

def merge(l1: list[int], l2: list[int]) -> list[int]:
    # ASC
    acc = []
    p1, p2 = 0, 0
    while p1 < len(l1) and p2 < len(l2):
        e1, e2 = l1[p1], l2[p2]
        if e1 <= e2:
            acc.append(e1)
            p1 += 1
        else:
            acc.append(e2)
            p2 += 1

    acc.extend(l1[p1:])
    acc.extend(l2[p2:])
    return acc


def sort(nums: list[int]) -> list[int]:
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    return merge(
        sort(nums[:mid]),
        sort(nums[mid:]),
    )


def kthSmallestNaive(root: Node, k: int) -> int:
    # O(NLogN), O(N) solution would be to go BST -> List -> SortedList -> SortedList[k-1]
    nums = []

    # Traverse in any way through all of tree. This will be O(N) time.
    # (Iterative inorder DFS being used below)
    nodes = [root]
    while nodes:
        curNode = nodes.pop()
        nums.append(curNode.value)
        if curNode.right:
            nodes.append(curNode.right)
        if curNode.left:
            nodes.append(curNode.left)

    # Sort the list
    nums = sort(nums)

    # Select the k-1th element
    return nums[k-1]

"""
Thinking:
How can we do better?
Let's consider one of the examples:

                        5
               3                 6
            2       4
        1
                         

Say we wanted to select the... 4'th smallest element in the list.
This happens to be the node (4), above.

Starting at the root, how would we know that that's the case?
How would we know to look to the left, as opposed to the right?
If there were fewer nodes in the left subtree, it might be the case that 
the 4th smallest element would have been in the right subtree!

It feels to me like we might need to know how many nodes are in both the left
and right subtrees?...

Say we knew in our example...

                     (4 Nodes) <- 5 -> (1 Node)

Would this help us find the 4th smallest element in the list?
It would in this case, we'd know that it has to be the largest node in the left
subarray. We could then trace down to it pretty quick...

But what if it were a little harder than that 
                    

                        5
               3                 6
            2       4
        1              4.5
                
What if we wanted the 4th smallest element, which again is (4)?

                (5 Nodes) <- 5 -> (1 Node)   # Costs O(N)
            Let's call (5Nodes) "Left" and (1Node) "Right"
        
        Since k <= "Left": Look Left?
        
        Hmmm..
        
"""

"""
Neetcode time!

Remember: 
A Binary Search Tree means...
that for any given node X:
    * Everything in X's left subtree is LESS THAN X
    * Everything in X's right subtree is GREATER THAN X
    
    k=1
            3
    1               4       --> [1,2,3,4] -> 1
        2
        
Your first thought might be to do what we just did:
* Take the binary search tree, put it into a sorted array
* Select the k-1'th element.

BUT if you traverse the binary search tree "dumbly" and put it into an
UNSORTED array like I did above, then yeah, we have to sort it.

But can we traverse the list in such a way that we GET a sorted array out of it?
How do we choose when to do the three actions:
    1)  Traverse Left (if appropriate)
    2) Process Current Node (meaning add it to accumulated list)
    3) Traverse Right (if appropriate)
    
Let's look at an example and see if we can determine that:
                3
    1                   4
        2       
        
In this example, we start at 3. |  []
Does 3 have a left? yes
We traverse left, to 1.
Does 1 have a left? No --> This means 1 is the MINIMUM
Process 1                   [1]
Does 1 have a right? Yes
Traverse right to 2
Does 2 have a left? No
Process 2                   [1,2]
Does 2 have a right? No
(Bubble back up to 3)
Process 3                   [1,2,3]
Does 3 have a right? Yes
Traverse to 4           
Does 4 have a left? No
Process 4                   [1,2,3,4]
Does 4 have a right? No

[1,2,3,4]

Checking: Does this also work on 
                        5
               3                 6
            2       4
        1
                       
? It does!
"""

def kthSmallest(root: Node, k: int) -> int:
    nums = []

    def helper(node: Node) -> None:
        # Recurse left
        if node.left:
            helper(node.left)
        # Process node
        nums.append(node.value)

        # Recurse right
        if node.right:
            helper(node.right)

    helper(root)

    return nums[k-1]




"""
Followup: If the BST is modified often (ie we can do insert and delete operations).
and you need to find the kth smallest frequently, how would you optimize?
"""




# -- Test Zone --
def test(fn):
    """
                    3
            1               4
                2
    """
    head = Node(3, Node(1, None, Node(2)), Node(4))
    assert fn(head, 1) == 1

    """
                        5
               3                 6
            2       4
        1
                                
    """
    head = Node(5, Node(3, Node(2, Node(1)), Node(4)), Node(6))
    assert fn(head, 3) == 3


test(kthSmallestNaive)
test(kthSmallest)