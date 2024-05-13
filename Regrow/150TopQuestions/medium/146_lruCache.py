from __future__ import annotations
from typing import Optional

"""
LRU Cache

Implement an LRU Cache class that:

* LRUCache(int capacity):
    Initialize the LRU Cache with Positive size `capacity`
* int get(int key):
    Return the value of the `key` if the key exists, otherwise return -1
* int put(int key, int value):
    Update the value of the key if the key exists, Otherwise, add the
    key-value pair to the cache. If the number of keys exceeds the
    `capacity` from this operation, `evict` the least recently used key.

The functions `get` and `put` must both run in O(1) average time complexity!
"""

"""
Okay, so the Key-Value Put/Get operations lend themselves well to a hashtable
and the "Least Recently Used" lend themselves to any sort of ordered datastructure.

Put/Gets without keeping track of LRU/evictions is easy to do in O(1) time.
But now we're keeping track of recency with some sort of ordered data structure.
The hard part is either insertions/deletions.

If we were using a list, maybe an insertion involves an appendLeft (O(N))
and a pop (O(1)) in the case of a full cache. Oh no!

What we need to use is both a hashtable and a doubley linked list that makes for easy appends to
the left side of the list, and easy pops (somewhere in the list, or the tail)!

It seems like only a successfuly retrieval of .get counts as an LRU operation
whereas any put counts as an LRU operation

***
There's one interesting edge case that I'm running into.
Imagine we have a full LRUCache and we're adding a new key:value into
the cache that isn't already in the cache.

We first have to evict the LRU Node, meaning we have to both
remove it from our key: Node hashtable AND from our DLL of Nodes.

Okay, so we find the to-be-evicted Node because it's the "tail" node in our DLL.
It's easy to "stitch-out" that Node from the Linked List.
But we need to remove that entry from the hashtable too!
I don't think we need have a way to delete that KEY from the hashtable!
Does that mean that our nodes also have to have a key property on them?
I think so. 
"""


class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        if type(capacity) != int:
            raise TypeError("LRU Cache capacity must be an integer")
        if capacity <= 0:
            raise ValueError("LRU Cache capacity must be positive")

        self.capacity = capacity

        self.n = 0  # Number of nodes currently in Cache

        # Hastable of key:Node
        self.nodes = {}

        # Doubly Linked List
        self.head = Node(-1, -1)  # Dummy Head. Not present in nodes
        self.tail = Node(-1, -1)  # Dummy Tail. Not present in nodes
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        # Return value @ key if present, else -1
        if key in self.nodes:

            # Update key to MRU key
            node = self.nodes[key]
            # Update the "recency" of that key to most recent
            # Remove it from its current spot in recency list: "stitch up" the list (2 corrections)
            node.prev.next = node.next
            node.next.prev = node.prev
            # Add to head of recency list (4 corrections)
            node.next = self.head.next
            node.prev = self.head
            self.head.next.prev = node
            self.head.next = node

            return node.value

        # Otherwise, node not found
        return -1

    def put(self, key: int, value: int) -> None:
        """
           Cases:
               Key already in self.nodes and either [at capacity, not at capacity]
                   * Just change the value in the Node (-)
               Key not in self.nodes...
                   ... and at capacity
                       * Evict (dec), Insert (inc)
                   ... and not at capacity
                       * Insert (inc)
        """
        # Case 1: "Update" of existing key
        if key in self.nodes:
            self.nodes[key].value = value
            return

        # Case 2: Insert [at capacity] If we're at Capacity... (and new key) Evict
        if self.n == self.capacity:
            # Evict LRU key (non-dummy "tail" node) from LL
            eviction_node = self.tail.prev
            eviction_node.prev.next = eviction_node.next
            eviction_node.next.prev = eviction_node.prev

            # Evict eviction_node from hashtable
            del self.nodes[eviction_node.key]

            self.n -= 1


        # Case 3: Insert [under capacity]: Insert Node into HT and DLL
        node = Node(key, value)
        self.nodes[key] = node

        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

        self.n += 1


# Test Zone
cache = LRUCache(2)
assert cache.put(1, 1) == None
assert cache.put(2, 2) == None
assert cache.get(1) == 1
assert cache.put(3, 3) == None
assert cache.get(2) == -1
assert cache.put(4, 4) == None
assert cache.get(1) == -1
assert cache.get(3) == 3
assert cache.get(4) == 4
print("Done!")