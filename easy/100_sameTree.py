"""
Given the roots of two binary trees p and q, write a function to check
if they are the same or not

Two binary trees are considered the same if they're structurally identical,
and the nodes have the same value
"""


class BSTNode:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


"""
Hmm... how should we go about this?
We could serialize each of them using the same traversal into a list, and then compare the lists?
    * Is it possible that two different lists could have the same serialization? Not if it's a good one, I'd think...
Or could we do the traversal of them both at the same time, and fail early if we detect a mismatch?
    * This isn't better than the other O(N) time... but at least it doesn't use O(N) space?
    
WHAT IF THIS WERE THE CASE:
Two trees are the same if their roots are the same and their left and right subtrees are the same
"""

# """

"""
Think: Comparing trees recursively.
Just thinking about the roots, what are all the things we can say about two
trees just by looking at the roots?
1. If the roots are both None/Null, then we know there aren't going to be children, and 
that the "trees" are identical.
2. If one of the roots is present and the other isn't, we know they aren't identical trees
3. If both roots are present but the values of the roots are not identical, the trees aren't either.

Then, we want to recursively do the same to each  
"""
def are_same_tree(p: BSTNode, q: BSTNode):
    # Base
    # Case 1: Both Empty Trees
    if not p and not q:
        return True
    # Case 2: One Empty Tree
    if not p or not q:
        return False
    # Case 3: Root Values not Same
    if p.value != q.value:
        return False

    # Recursive
    return are_same_tree(p.left, q.left) and are_same_tree(p.right, q.right)


# Case 1
p1 = BSTNode(1)
pn2 = BSTNode(2)
pn3 = BSTNode(3)
p1.left = pn2
p1.right = pn3

q1 = BSTNode(1)
qn2 = BSTNode(2)
qn3 = BSTNode(3)
q1.left = qn2
q1.right = qn3

print(are_same_tree(p1, q1)) # True

# Case 2
p1 = BSTNode(1)
pn2 = BSTNode(2)
p1.left = pn2

q1 = BSTNode(1)
qn2 = BSTNode(2)
q1.right = qn2

print(are_same_tree(p1, q1)) # False

# Case 3
p1 = BSTNode(1)
pn2 = BSTNode(2)
pn3 = BSTNode(1)
p1.left = pn2
p1.right = pn3

q1 = BSTNode(1)
qn2 = BSTNode(1)
qn3 = BSTNode(2)
q1.left = qn2
q1.right = qn3

print(are_same_tree(p1, q1)) # False