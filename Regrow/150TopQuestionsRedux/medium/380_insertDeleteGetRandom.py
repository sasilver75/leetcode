"""
Insert Delete GetRandom O(1)

Implement the RandomizedSet class:
- RandomizedSet() initializes
- insert(val: int) -> bool
    - Inserts an item val into the set if not present, returning true if the
    item was not present, and false otherwise.
- remove(val: int) -> bool:
    - Removes an item val from the set if present. Returns true if the item
    was present, and false otehrwise.
- getRandom() -> int:
    - Returns a RANDOM ELEMENT from the current set of elements. It's guaranteed
    that at least one element exists when this element is called.
    - Each element must have the SAME PROBABILITY of being returned.

You must implement the functions of the class such that each function works in
average O(1) time complexity.

"""
import random

"""
Thinking:

How do we insert an element in O(1) time?
    - Append to an ordered collection like a list
    - Insert to an unordered collection like a set
    
How do we remove an element in O(1) time?
    - Remove from an unordered collection like a set in O(1) time with
    the help of a hashtable.
    - Remove from an ordered collection like a DLL in O(1) time with the
    help of a hashtable

How do we get a random element from a collection in O(1)?
    - Selecting a random index from an indexable collection like a list
    - CheatingIdea: Given that at most 2*10^5 elements will be in the list, we 
    could generate a random number in the range [1, 2*10^5] and take that many steps
    around a doubly linked list. It's not performant, but it's an O(1) strategy in the 
    sense that it's always not especially performant.

It seems like we need the help of a hash function in some way, even if it comes
in the form of a set...

INSIGHT:
- I'd really like the "getRandomElement" ability of a list, but the downside
of a list is that removing an element is O(N)... EXCEPT if it's a pop() off the 
end of the list! Can we turn all removes into list pops?
- We can if we combine a list of elements, and a hashtable of elements to their indices
in the list.
- Whenever we want to delete an element, we swap it with the last element in 
the list, and then pop it. Keep the hashtable updated while you do this.

"""
class RandomizedSet:
    def __init__(self):
        self.items = []
        self.lookup = {}

    def insert(self, val: int) -> bool:
        if val in self.lookup:
            return False
        self.items.append(val)
        self.lookup[val] = len(self.items)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.lookup:
            return False
        val_idx = self.lookup[val]
        # Swap with end
        end_val = self.items[-1]
        end_val_idx = self.lookup[end_val]

        # Swap in items
        self.items[val_idx], self.items[end_val_idx] = self.items[end_val_idx], self.items[val_idx]
        # Swap in lookup (Don't really need to swap val's info, tbh)
        self.lookup[val] = end_val_idx
        self.lookup[end_val] = val_idx
        # Delete val
        self.items.pop()
        del self.lookup[val]

        return True


    def getRandom(self) -> int:
        """There is guaranteed to be at least one element in the RS when getRandom is called"""
        # Get a random index
        idx = random.randint(0, len(self.items) - 1)
        # Return the value at it
        return self.items[idx]


rs = RandomizedSet()
assert rs.insert(1) == True
assert rs.remove(2) == False
assert rs.insert(2) == True
r = rs.getRandom()
assert r in [1,2]
assert rs.remove(1) == True
assert rs.insert(2) == False
assert rs.getRandom() == 2