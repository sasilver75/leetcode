"""
One elf is the rucksack-packing elf.
He needs to pack these backpacks effectively!

Each rucksack has two large `compartments`.
All elements of a given `type` are meant to go into one of the two compartments.

The packing elf made a mistake:
The elf failed to follow the above rule for EXACTLY ONE ITEM TYPE per rucksack!

The elves have made a list of all of the items currently in each rucksack
(Your input)
But need help finding the errors.
Every item type is identified by a single letter (a and A are distinct types)

The list of items for a rucksack is given by a line of characters.
A rucksack has the same number of items in each of its two compartments,
so the FIRST HALF of the characters represents the contents of the first
compartment, while the second half represents the contents of the second
compartment.

So for each rucksack:
1) Find the item that appears in both compartments of the rucksack
2) Sum the priorities of these elements across rucksacks, where
priorities are: a=1, b=2, ... z=26, A=27, B=28, ...Z=52
"""
import math
import string

PRIORITIES = {k:v for k,v in zip(
    string.ascii_lowercase+string.ascii_uppercase, range(1, 53)
)}

with open("inputs/3a.txt", "r") as f:
    sum = 0
    for rucksack in f.read().splitlines():
        seen = set()
        for idx, item in enumerate(rucksack):
            if idx < math.floor(len(rucksack)/2): # How do we treat middle elements?
                seen.add(item)
            else:
                if item in seen:
                    sum += PRIORITIES[item]
                    break

    print(sum)



