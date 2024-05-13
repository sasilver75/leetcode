"""
Insert Delete GetRandom O(1)

Implement the `RandomizedSet` class:
    * RandomizedSet() initializes the RandomizedSet object
    * bool insert(int val) inserts an item `val` into the set if not present.
        Returns true if the item was NOT present, false otherwise
    * bool remove(int val) removes an item `val` from the set if the item was
    present, `false` otherwsie.
    * int getRandom() returns a random element frmo the current set of elements.
        It's guaranteed that at least one element exists when this method is called.
        Each element must have the same probability of being returned!

You must implement hte functions of the class such that each function works
in AVERAGE O(1) time complexity...
"""
import random

"""
Sam Note: 
Interesting, O(1) AVERAGE time complexity?
It's definitely interesting that the word AVERAGE was used.
So insert and remove function very similarly to just a normal hashset, it seems to me.

What about getRandom would be difficult if we wanted to just built this on Set? I mean
the Python set interface doesn't expose anything useful to us in this respect... 
"""

class DLLNode:
    def __init__(self, value: int) -> int:
        self.value = value
        self.prev = None
        self.next = None

    def as_list(self):
        acc = []
        cur = self
        while cur:
            acc.append(cur.value)
            cur = cur.next
        return acc



"""
I'm thinking about a sideways roulette that generates a large number
and moduluses it around a list

Ex: BigNumber = randomNumberMaker() = 12345
nums = [5,8,10,12,15]
return nums[BigNumber % len(nums)]

Okay cool, so my values are stored in a list? 
Except a list wouldn't support efficient DELETES, which would be O(N).
An ordered data structure that supports both my roulette idea AND deletes
would be the combination of a DoublyLinkedList and a DICT of key: Node.

Want to add a value?
    -> Is it in the dict?
        Yes? It's already in the set, No-Op
        No? Create a node, add it to dict, and insert it at the tail of the list

Want to delete a value?
    -> Is it in the dict?
        No? No-Op
        Yes?
        Grab a reference to that node from teh dict, and stitch it out of the DLL

Want to get a random node?
    -> Generate a large number and do that many .next's from the head :)
        BUT make sure not to end on Head or Tail!
"""

class RandomizedSet:
    def __init__(self):
        self.nodes = dict() #Dict: Int:(Nodes)
        self.head = DLLNode(None)
        self.tail = DLLNode(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, val: int) -> bool:
        if val in self.nodes:
            return False

        node = DLLNode(val)
        # Insert into Dict
        self.nodes[val] = node
        # Insert into end of DLL (4 operations)
        node.prev = self.tail.prev
        self.tail.prev.next = node
        node.next = self.tail
        self.tail.prev = node

        return True




    def remove(self, val: int) -> bool:
        if val not in self.nodes:
            return False

        # Remove from DLL - 2 operations
        node = self.nodes[val]
        node.prev.next = node.next
        node.next.prev = node.prev
        # Remove entry from Dict
        del self.nodes[val]

        return True

    def get_random(self) -> int:
        # "At most 2 * 10**5 calls will be made to insert, remove, and getRandom."
        # Guaranteed that at least SOME values are between head/tail
        steps = random.randint(1, 2 * 10**5)
        cur = self.head
        while steps:
            # Take a Step to a valid next node! (Not Head or Tail))
            cur = cur.next

            if cur is self.tail:
                cur = self.head.next

            steps -= 1

        return cur.value





# Test Zone
rs = RandomizedSet()
assert rs.insert(1) == True
assert rs.remove(2) == False
assert rs.insert(2) == True
assert rs.get_random() in (1, 2)
assert rs.remove(1) == True
assert rs.insert(2) == False
assert rs.get_random() == 2
