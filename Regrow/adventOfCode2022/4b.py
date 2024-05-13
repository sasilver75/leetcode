"""
It seems like there's a lot of duplicate work planned.

Instead, the elves would like to know the number of pairs that overlap AT ALL!

In how many assignment pairs do the ranges overlap?
"""

def parse(rap: str) -> list[list[int]]:
    # "2-4,5-7" -> [[2,4], [5,7]]
    assignemnts = rap.split(",")
    ranges = [assignment.split("-") for assignment in assignemnts]
    int_ranges = [[int(el) for el in rnge] for rnge in ranges]
    return int_ranges

# print(parse("2-4,5-7"))

def touches(a: list[int], b: list[int]):
    partial_containment = (
        (b[0] <= a[0] <= b[1])
        or
        (b[0] <= a[1] <= b[1])
    )

    full_containment = (
        (a[0] >= b[0] and a[1] <= b[1])
        or
        (b[0] >= a[0] and b[1] <= a[1])
    )

    return partial_containment or full_containment

with open("inputs/4a.txt", "r") as f:
    raw_assignment_pairs = f.read().splitlines()
    assignments = [parse(rap) for rap in raw_assignment_pairs]
    count = 0
    for assignment in assignments:
        if touches(*assignment):
            count += 1

    audit = [[assignment, touches(*assignment)] for assignment in assignments]
    for a in audit:
        print(a)

    print(count)