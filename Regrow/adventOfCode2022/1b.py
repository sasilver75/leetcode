"""
Day One (Calorie Counting) - Part 2
https://adventofcode.com/2022/day/1#part2
"""


def sort(nums: list[int]) -> list[int]:
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    return merge(
        sort(nums[0:mid]),
        sort(nums[mid:])
    )


def merge(l1: list[int], l2: list[int]):
    acc = []
    p1, p2 = 0, 0
    while p1 < len(l1) and p2 < len(l2):
        e1, e2 = l1[p1], l2[p2]
        if e1 >= e2:
            acc.append(e1)
            p1 += 1
        else:
            acc.append(e2)
            p2 += 1

    acc.extend(l1[p1:])
    acc.extend(l2[p2:])

    return acc


with open("inputs/1a.txt", "r") as f:
    data = f.read().splitlines()

    elves = []
    total = 0
    # Get the per-elf calories!
    for cal in data:
        if cal == "":
            elves.append(total)
            total = 0
        else:
            total += int(cal)

    # Any Remaining?
    if total:
        elves.append(total)

    # Sort the calories, DESC!
    elves = sort(elves)

    print(sum(elves[0:3]))

