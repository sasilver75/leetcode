
def mergeSortedLists(l1: list[int], l2: list[int]) -> list[int]:
    sorted = []
    idx1 = 0
    idx2 = 0
    # While neither list are exhausted
    while idx1 < len(l1) and idx2 < len(l2):
        el1 = l1[idx1]
        el2 = l2[idx2]
        if el1 <= el2:
            sorted.append(el1)
            idx1 += 1
        else:
            sorted.append(el2)
            idx2 += 1
    # One of the two lists are now exhausted. Append the remaining items from the remaining sorted list
    sorted.extend(l1[idx1:])
    sorted.extend(l2[idx2:])
    print("Sorted: ", sorted)
    return sorted





def test(fn):
    assert fn([1, 2, 4], [1, 3, 4]) == [1, 1, 2, 3, 4, 4]
    assert fn([], []) == []
    assert fn([], [0]) == [0]

test(mergeSortedLists)