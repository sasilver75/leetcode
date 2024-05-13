"""
155_minStack

Design a stack that supports push, pop, top and retrieving the MINIMUM
ELEMENT in constant time!

Implement the minStack class:
* MinStack() initializes the stack object
* void push(int val) pushes the element val onto the stack
* void pop() removes and returns the element on the top of the stack
* int top() retrieves the top element of the stack
* int getMin retrieves the minimum element in the stack

You must implement a solution with O(1) time complexity for each function!
"""
from typing import Optional


"""
I'm going to assume that pop/top/getMin on an empty MinStack return None


We need to have some notion of the stack.. Okay, that could be just 
a list that supports append and pop.
That would satisfy O(1) for push/pop/top.

But we also need to keep track of the minimum element in the stack.
Okay, so what if that were just a register with an int? That would work
fine for the .getMin call, but what how would we change that register when
we pop off the min?

The fact that we can only append and remove items from this data
structure in FIFO order is useful, I think.

Imagine we've appended values in the following order:
[3,5,2,7]
And those values are internally contained in the minStack data structure somehow.
If I asked for the minimum value, it would be 2.
Now imagine that I pop 2 times.
What would the minimum value be?
It would be 3.

So if we internally kept track of an ADDITIONAL stack
itemStack = [3,5,2,7]
minimumStack = [3,2]
Where we only add an item to minimumStack when the item being added to 
itemStack is LESS THAN OR EQUAL TO the top value on minimumStack.
Because the truth is that an item like 5 will NEVER be the minimum value --
Since a smaller value occurred BEFORE 5. 
"""

class MinStack:
    def __init__(self):
        self.item_stack = []
        self.minimum_stack = []

    def push(self, val: int) -> None:
        self.item_stack.append(val)
        if not self.minimum_stack or val <= self.minimum_stack[-1]:
            self.minimum_stack.append(val)

    def pop(self) -> Optional[int]:
        if not self.item_stack:
            return None
        item = self.item_stack.pop()
        # If there was an item in item stack, there must be item(s) in minimum stack
        if item == self.minimum_stack[-1]:
            self.minimum_stack.pop()
        return item


    def top(self) -> Optional[int]:
        return self.item_stack[-1] if self.item_stack else None

    def getMin(self) -> Optional[int]:
        return self.minimum_stack[-1] if self.minimum_stack else None


# Test Zone
ms = MinStack()
ms.push(-2)
ms.push(0)
ms.push(-3)
assert ms.getMin() == -3
assert ms.pop() == -3
assert ms.top() == 0
assert ms.getMin() == -2