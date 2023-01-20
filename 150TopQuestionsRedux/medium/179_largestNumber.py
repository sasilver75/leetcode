"""
Largest Number

Given a list of non-negative integers `nums`, arrange them such
that they form the largest number, and return it.

Since the result may be very large, you need to return a string instead
of an integer.
"""


"""
Is this as simple as sorting the list, using a certain criteria?

Imagine we have [9, 8, 97, 99]
The correct ordering would be [99,9,97,8]

So we compare character by character
    - If a[idx] > b[idx], choose a first
        This gives us things like 9 > 8
    - If a[idx] == b[idx], continue
    - If one has been exhausted, and the other has a next element value >= the last 
        item of the exhausted one, choose the nonexhausted one, else choose the exhausted one
"""

def compare(a: int, b: int) -> bool:
    """
    Returns True if a is considered "greater" than b, else False
    """
    a_chars = str(a)
    b_chars = str(b)
    a_idx, b_idx  = 0, 0
    while a_idx < len(a_chars) and b_idx < len(b_chars):
        a_int = int(a_chars[a_idx])
        b_int = int(b_chars[b_idx])

        if a_int > b_int:
            return True
        elif b_int > a_int:
            return False

        a_idx += 1
        b_idx += 1

    if len(a_chars) == len(b_chars):
        return True # a and b are the same; choose a

    if a_idx == len(a_chars):
        # B is not exhausted. Compare the current element in B to the last in A.  # 34>3 but 32<3
        a_char = int(a_chars[-1])
        b_char = int(b_chars[b_idx])
        if b_char >= a_char:
            return False
        else:
            return True

    # Thus b_idx == len(b_chars)
    # A is not exhausted. Compare the current element in A to the last in B
    a_char = int(a_chars[a_idx])
    b_char = int(b_chars[-1])
    if a_char >= b_char:
        return True
    else:
        return False

def merge(nums1: list[int], nums2: list[int]) -> list[int]:
    # Uses the compare function to merge two lists
    acc = []
    p1, p2 = 0, 0
    while p1 < len(nums1) and p2 < len(nums2):
        e1, e2 = nums1[p1], nums2[p2]
        if compare(e1, e2):
            acc.append(e1)
            p1 += 1
        else:
            acc.append(e2)
            p2 += 1

    acc.extend(nums1[p1:])
    acc.extend(nums2[p2:])
    return acc


def merge_sort(nums: list[int]) -> list[int]:
    # Sorts the numbers in appropriate order according to problem statement
    if len(nums) <= 1:
        return nums

    mid_idx = len(nums) // 2

    return merge(
        merge_sort(nums[:mid_idx]),
        merge_sort(nums[mid_idx:])
    )


def largest_number(nums: list[int]) -> str:
    sorted_nums = merge_sort(nums)
    return "".join(str(num) for num in sorted_nums)



assert largest_number([10,2]) == "210"
assert largest_number([3, 30, 34, 5, 9]) == "9534330"