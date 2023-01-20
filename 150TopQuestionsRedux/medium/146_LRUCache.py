from typing import Optional
"""
LRU Cache

Design a data structure that follows the constraints of a LRU Cache

Implement the LRUCache class:

- LRUCache(int capacity)
    - Initialize the LRU cache with positive size capacity.
- int get(int key)
    - Return the value of the key if the key exists, otherwise return -1.
- void put(int key, int value)
    - Update the value of the key if the key exists.
    - Otherwise, add the key-value pair to the cache.
    - If the # keys exceeds the capacity from this operation, evict the least recently used key.
"""

"""
Okay, so to solve LRU Cache, we need a few things:

1) A HashMap mapping keys to values -- this is used to retrieve the value @ keys
for the get operation.
2) A CurrentCapacity of the HashMap and a CapacityLimit
3)  Some notion of "recency order of key access". This needs to be some totally
ordered collection containing every key. This is used for evictions when
the hashmap is at capacity and we're asked to put another key.

Hashmap: {key: Node}
DLL: Nodes, where the leftmost node is the most recently accessed, and 
the rightmost node is the latest accessed.
    - When a key is successfully "get"'d , move it in the DLL to the left
    side of the DLL
    - When a key is successfully put, set a new node to the left side of the DLL
    if it doesn't already exist, else move it there
"""

"""
One of the keys here that you'll learn about when looking to see how
you can evict a value from the LRU Cache is the 
"""
class Node:
    """ A dumb container for a value, for use in DLL"""
    def __init__(self, key: Optional[int], value: Optional[int]):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    """
    A container for values, with no notion of capacity. Has dumb mechanisms,
    but none of the higher-level intelligence needed to operate it for LRU purposes

    DLL is going to be passed Nodes, not values
    """
    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert_left(self, node: Node) -> None:
        """Insert a node into the left side of the list"""
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head

    def remove(self, node: Node) -> None:
        """Given a node in the DLL, remove it"""
        node.prev.next = node.next
        node.next.prev = node.prev

    def remove_last(self) -> Node:
        last = self.tail.prev
        if last != self.head:
            self.remove(last)
        return last


    def move_to_left(self, node: Node) -> None:
        """
        Given a Node in the DLL, move it to the left
        """
        self.remove(node)
        self.insert_left(node)

    def as_list(self):
        acc = []
        cur = self.head
        while cur:
            acc.append(cur.value)
            cur = cur.next
        return acc[1:-1]


# -- Test Zone --
dll = DoublyLinkedList()
n1 = Node(5, 5)
n2 = Node(6, 6)
n3 = Node(7,7)
for n in [n1,n2,n3]:
    dll.insert_left(n)
assert dll.as_list() == [7,6,5]
dll.move_to_left(n2)
assert dll.as_list() == [6,7,5]
dll.remove(n3)
assert dll.as_list() == [6,5]


class LRUCache:
    def __init__(self, capacity_limit: int):
        self.nodes = {}
        self.capacity_limit = capacity_limit
        self.capacity = 0
        self.dll = DoublyLinkedList()

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        node = self.nodes[key]
        self.dll.move_to_left(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        # Update: Change key's current value to value and update recency
        if key in self.nodes:
            node = self.nodes[key]
            self.dll.move_to_left(node)
            node.value = value
            return

        # Insert new node with max recency, increase capacity + evict if needed
        node = Node(key, value)
        self.nodes[key] = node
        self.dll.insert_left(node)
        self.capacity += 1
        while self.capacity > self.capacity_limit:
            removed = self.dll.remove_last()
            self.capacity -= 1
            del self.nodes[removed.key]



# -- Test LRU Cache --
lru = LRUCache(2)
lru.put(1,1)
lru.put(2,2)
assert lru.get(1) == 1
lru.put(3,3)
assert lru.get(2) == -1
lru.put(4,4)
lru.get(1) == -1
lru.get(3) == 3
lru.get(4) == 4