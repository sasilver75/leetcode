"""
Space needs to be cleared before the last supplies can be unloaded from the
ships, and so several Elves have been assigned the job of cleaning up sections of the camp.

Each section of the camp has a unique `ID Number`, and each elf is assigned
some RANGE of section IDs!

But the elves have noticed that many of the assignments OVERLAP!
To avoid double=cleaning sections of the camp, the Elves PAIR UP to
make a big list of the section assignments for each elf.

ie
2-4,6-8
...
means that elf "A" was assigned sections 2,3,4 and elf "B" was assigned 6,7,8

Some of the pairs have noticed that some of their assignments FULLY CONTAIN
the other. For example, 2-8 fully contains 3-7, and 6-6 is fully contained by
4-6.
In pairs where one assignment fully contains the other,
one Elf in the pari would be exclusively cleaning sections their parter will
already be cleaning, so it seems like the most in need of reconsideration.

In how many assignment pairs does on range fully contain the other?
"""

def parse(s: str) -> list[list[int]]:
    # "2-4,6-8" -> [[2,4], [6,8]]
    assignments = s.split(",")
    start_ends = [assignment.split("-") for assignment in assignments]
    return [[int(el) for el in lst] for lst in start_ends]

def full_containment(a: list[int], b: list[int]) -> bool:
    return (
        (a[0] <= b[0] and a[1] >= b[1])
        or
        (b[0] <= a[0] and b[1] >= a[1])
    )

with open("inputs/4a.txt", "r") as f:
    containment_count = 0
    pairs = f.read().splitlines()
    print(f"There are {len(pairs)} total pairs")
    for pair in pairs:
        assignments = parse(pair)
        if full_containment(*assignments):
            containment_count += 1

    print(f"{containment_count} full containments detected")
