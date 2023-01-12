"""
Implement a last-in-first-out (LIFO) stack using
only two queues!
The implemented stack should support all the functions
of a normal stack: (push, top, pop, and empty).

push(x: int) -> None: Push elt x onto stack
pop() -> int: pop elt off of stack and return
top() -> int: return the element on top of stack
empty() -> bool: return whether stack is empty

Note that the queue you can use supports push, pop, size, and is_empty operations
"""

# Note that it's probably a good exercise to implement a Queue using a Doubly Linked List so you can have constant time prepends/appends.
from typing import Optional


class Queue:
    def __init__(self):
        self.items = []
    def push(self, item: int):
        self.items = [item, *self.items]
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def is_empty(self):
        return False if len(self.items) else True


"""
push(2)
push(3)
push(4)
pop() -> 4
pop() -> 3
top() -> 2
push(5)
pop() -> 5
is_empty() -> False
pop() -> 2
pop() -> None
is_empty() -> None

Thinking...
I think the concept of "dumping" a queue onto another queue is important, in some way?
Do I leave one queue open as a landing spot for pushes, and then immediately "dump"
the other queue's values onto it, and then the other queue becomes thte landing spot?
"""

# Todo in the morning! How can we make a LIFO stack out of two FIFO queues?
# I'm guessing there's a better way than this solution :)
class Stack:
    def __init__(self):
        self.buffer_queue = Queue()
        self.stack_queue = Queue()
    def push(self, val: int) -> None:
        self.buffer_queue.push(val)
        while not self.stack_queue.is_empty():
            self.buffer_queue.push(self.stack_queue.pop())
        while not self.buffer_queue.is_empty():
            self.stack_queue.push(self.buffer_queue.pop())

    def pop(self) -> Optional[int]:
        return self.stack_queue.pop()

    def top(self) -> Optional[int]:
        """Peek"""
        tmp = self.stack_queue.pop()
        if not tmp:
            return None

        while not self.stack_queue.is_empty():
            self.buffer_queue.push(self.stack_queue.pop())
        self.stack_queue.push(tmp)
        while not self.buffer_queue.is_empty():
            self.stack_queue.push(self.stack_queue.pop())
    def empty(self) -> bool:
        return self.stack_queue.is_empty()

stack = Stack()
stack.push(4)
stack.push(5)
stack.push(6)
print(stack.pop())
stack.push(7)
print(stack.pop())
print(stack.pop())
print(stack.empty())
print(stack.top())
print(stack.pop())
print(stack.empty())

