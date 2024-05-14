"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]


Input: list1 = [], list2 = []
Output: []

Input: list1 = [], list2 = [0]
Output: [0]
"""


from statistics import median_grouped


def merge(l1: list[int], l2: list[int]) -> list[int]:
    i, j = 0, 0
    merged_list = []
    # While neither list is exhausted
    while i < len(l1) and j < len(l2):
        e1 = l1[i]
        e2 = l2[j]
        if e1 <= e2:
            merged_list.append(e1)
            i += 1
        else:
            merged_list.append(e2)
            j += 1
    if i < len(l1):
        merged_list.extend(l1[i:])
    if j < len(l2):
        merged_list.extend(l2[j:])
    return merged_list


cases = (
    ([1,2,4], [1,3,4], [1,1,2,3,4,4]),
    ([], [], []),
    ([], [0], [0])
)

for l1, l2, ans in cases:
    # print(merge(l1, l2), ans)
    assert merge(l1, l2) == ans
    print("True")
