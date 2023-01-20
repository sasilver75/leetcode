"""
Min Stack

Design a stack that supports `push`, `pop`, `top`, and retrieving
the minimum element in constant time.

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function
"""
from typing import Optional


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> Optional[int]:
        popped = self.stack.pop()
        if popped == self.min_stack[-1]:
            self.min_stack.pop()
        return popped


    def top(self) -> Optional[int]:
        return self.stack[-1] if self.stack else None

    def get_min(self) -> Optional[int]:
        return self.min_stack[-1] if self.min_stack else None

ms = MinStack()
ms.push(-2)
ms.push(0)
ms.push(-3)
assert ms.get_min() == -3
assert ms.pop() == -3
assert ms.top() == 0
assert ms.get_min() == -2
