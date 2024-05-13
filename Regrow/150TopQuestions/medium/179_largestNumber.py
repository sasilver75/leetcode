"""
Largest Number

Given a list of non-negative integers `nums`, arrange
them such that they form the largest number and return it.

Since the result may be very large, you need to return a STRING
instead of an integer.
"""

"""
Okay, so the naive idea might be 
"Oh, just order the numbers DESC and then smash them together!"
But that isn't quite right.

It's really ordering the numbers by their first char, then second char,
then third char, etc.

So 9 > 21, in this case.
And 23 > 21

So it's the digit-wise comparison between two numbers that we should be using
to sort them.
"""

def compare(s1: str, s2: str) -> str:
    # Given two strings, return the GREATER of the two using digit-wise string comparisons
    # One important note is that 3 > 32 because 332 > 323. Think about that, see assert examples below
    idx = 0
    while idx < min(len(s1), len(s2)):
        # Is there a strict dominance at the current index? Return that string!
        if s1[idx] > s2[idx]:
            return s1
        if s1[idx] < s2[idx]:
            return s2

        idx += 1

    # One string OR BOTH are exhausted; which was it?
    if idx == len(s1):
        return s1 if s1[-1] >= s2[idx] else s2
    if idx == len(s2):
        return s2 if s2[-1] > s1[idx] else s1

# assert compare("9", "32") == "9"
# assert compare("9", "89") == "9"
# assert compare("9", "91") == "91"
# assert compare("3", "30") == "3" # Because 330 > 303
# assert compare("3", "305") == "3" # Because 3305 > 3053
# assert compare("3", "32") == "3" # Because 332 > 323
# assert compare("3", "34") == "34"# Because 343 > 334
# assert compare("3", "33") == "3" # 333 either way; doesn't matter - pick A



def merge(n1: list[str], n2: list[str]) -> str:
    # Given two lists of "sorted" strings, return a single list of sorted strings
    acc = []
    p1, p2 = 0, 0

    while p1 < len(n1) and p2 < len(n2):
        s1 = n1[p1]
        s2 = n2[p2]

        winner = compare(s1, s2)
        if s1 == winner:
            acc.append(s1)
            p1 += 1
        else:
            acc.append(s2)
            p2 += 1

    acc.extend(n1[p1:])
    acc.extend(n2[p2:])

    return acc

# assert merge(["91", "9", "88"], ["89", "84", "8"]) == ["91", "9", "89", "88", "84", "8"]

def wordsort(nums: list[str]) -> list[str]:
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    return merge(
        wordsort(nums[0:mid]),
        wordsort(nums[mid:])
    )

# assert wordsort(["10", "2"]) == ["2", "10"]



def largest(nums: list[int]) -> str:
    sorted = wordsort([str(n) for n in nums])
    print(sorted)
    return "".join(sorted)


assert largest([10,2]) == "210"
assert largest([3, 30, 34, 5, 9]) == "9534330"
