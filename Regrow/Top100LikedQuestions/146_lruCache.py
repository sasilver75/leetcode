"""
LRU Cache

Design a data structure for an LRU Cache

Implement:
    - LRUCache(int capacity): Initialize the LRU cache with positive size capacity
    - int get(int key): Return the value of the key if the key exists, otherwise -1
    - void put(int key, int, value): Update the value of the key if the key exists; otherwise, add the key-value pair to the cache.
        - If the number of keys exceeds the capacity from this operation, evict the least-recently-used key

The GET and PUT functions must each run in O(1) average time complexity.
"""
from datetime import datetime


class Node:
    """
    A Doubly-Linked List Node, with value, prev, next
    """
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.current_capacity = 0
        self.values = {} # key: Node
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.values:
            return -1

        # Update the recency of access of the key before returning its value, by moving it to the front of the recency list
        node = self.values[key]
        # Stitch it out
        node.prev.next = node.next
        node.next.prev = node.prev
        # Stitch it in
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

        return node.value

    def put(self, key: int, value: int) -> None:
        self._insert(key, value)
        if self.current_capacity > self.capacity:
            self._evict()  # Evict the latest


    def _insert(self, key: int, value: int) -> None:
        # Is the key already in self.values?
        if key in self.values:
            self.values[key].value = value
        else:
            new_node = Node(key, value)
            self.values[key] = new_node

            new_node.next = self.head.next
            new_node.prev = self.head
            self.head.next.prev = new_node
            self.head.next = new_node

            self.current_capacity += 1



    def _evict(self) -> None:
        # Assuming it's a "valid" evict, for now
        target_node = self.tail.prev
        if target_node is self.head:
            # if there aren't any nodes to evict, just return.
            return

        node_key = target_node.key

        # Remove from Ordering
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev

        # Remove from Values
        del self.values[node_key]



lru = LRUCache(2)
lru.put(1, 1)
lru.put(2,2)
assert lru.get(1) == 1
lru.put(3,3)
assert lru.get(2) == -1 # Because the get of 1 made 2 the lru key
lru.put(4,4)
assert lru.get(1) == -1
assert lru.get(3) == 3
assert lru.get(4) == 4
