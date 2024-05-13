"""
After we identified the misplaced items... there's another issue:

For their safety, elves are divided into groups of three.

Every elf carries a BADGE that identifies their group.
For efficiency, within each group iof three elves, the badge is the
only item type carried by all three elves!

That is, if the group's badge is item type B, then all three
elves will have item type B somewhere in their rucksack... and at most
two of the elves will be carrying any other item type.

We need to pull all of the badges out of the rucksacks.
The only way to tell which item is the right one is by finding
the one item type that is common between all three elves in each group!

Every set of three lines in your list corresponds to a single group, but
each group can have a different badge item type.

Priorities for these items must still be found to organize the badge system.
Find the sum of the badge priorities across all groups!
"""
import collections
import string

LOOKUP = {k:v for k,v in zip(
    string.ascii_lowercase+string.ascii_uppercase, range(1,53)
)}

with open("inputs/3a.txt", "r") as f:
    rucksacks = f.read().splitlines()
    groups = [rucksacks[i:i+3] for i in range(0, len(rucksacks), 3)]
    sum = 0
    for group in groups:
        # Populate group counts
        counts = collections.defaultdict(lambda: 0)
        for ruck in group:
            for item in set(ruck): # To avoid double-counting if the same item is carried multiple times in a ruck
                counts[item] += 1


        # Inc sum by badge value
        for badge_candidate in counts:
            if counts[badge_candidate] == 3:
                sum += LOOKUP[badge_candidate]

    print(sum)