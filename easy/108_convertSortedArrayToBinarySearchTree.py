"""
Given an integer array NUMS where the elements are sorted in ASC order,
convert it to a HEIGHT-BALANCED binary search tree.

A HEIGHT_BALANCED binary tree is a tree inw hich the depth of every node
never differs by more than one.
"""
from __future__ import annotations
from typing import Optional


class BSTNode:
    def __init__(self, value: int, left: Optional[BSTNode] = None, right: Optional[BSTNode] = None):
        self.value = value
        self.left = left
        self.right = right


"""
Recall the rules of a binary search tree:
1) Every element in n's left subtree is less than or equal to the 
element in node n.  (<=)
2) Every element in n's right subtree is greater than the element in node n. (>)

If we want the BST we create to be HEIGHT-BALANCED...
Well let's look at the example of 

[-10, -3, 0,  5, 9]
becoming
            0
        -3      9
    -10       5
    
At least in this example, we chose the middle value (by index, since sorted) to be
the midpoint. As a result we've got 2 nodes on either side of the middle index

Once we place 0

        0
        
Let's just think about the left subtree.
In the array, now we have [-10, -3] to think about.
Can this be a recursive case? Can we take the "middle" value of these two?
len(array) // 2 == index 1
We can take this [-10, -3] subarray and create a new subtree to the left of our root.


"""
def sorted_array_to_bst(arr: list) -> BSTNode:

    def helper(left: int, right: int) -> BSTNode:
        # Base Case: Exit when left > right (we've ran off the edge)
        if left > right:
            return None

        # Construct a node from the mid elt
        mid = (left + right) // 2
        mid_node = BSTNode(arr[mid])

        # Recurse on left and right subtrees
        mid_node.left = helper(left, mid - 1)
        mid_node.right = helper(mid + 1, right)

        return mid_node



    root = helper(0, len(arr)-1)
    return root


# Case 1
soln1 = sorted_array_to_bst([-10, -3, 0, 5, 9])
"""
Produced:
          0
     -10       5
        -3       9
Good!
"""

# Case 2
soln2 = sorted_array_to_bst([1, 3])
"""
Produced
        1
            3
Good!
"""
