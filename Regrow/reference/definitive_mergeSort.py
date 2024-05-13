"""
Intended to be my definitive, correct versions
of the mergesort algorithm
"""


def merge_sort(nums: list[int]) -> list[int]:
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    left_partition = merge_sort(nums[:mid])
    right_partition = merge_sort(nums[mid:])

    return merge(left_partition, right_partition)


def merge(l1: list[int], l2: list[int]) -> list[int]:
    merged = []

    p1 = 0
    p2 = 0

    while p1 < len(l1) and p2 < len(l2):
        e1 = l1[p1]
        e2 = l2[p2]

        if e1 <= e2:
            merged.append(e1)
            p1 += 1
        else:
            merged.append(e2)
            p2 += 1

    merged.extend(l1[p1:])
    merged.extend(l2[p2:])

    return merged


assert merge_sort([3,1,6,3,5,7,8,3]) == [1, 3, 3, 3, 5, 6, 7, 8]
assert merge_sort([1,3,51,2,54]) == [1,2,3,51,54]
assert merge_sort([]) == []


"""
Merge Sort can also be adapted to be an in-place sorting algorithm
"""

def in_place_merge_sort(nums: list[int]) -> None:
    def merge_in_place(arr: list[int], l_start: int, l_end: int, r_end: int) -> None:
        """
        :param arr:
        :param l_start: Index of start of left array
        :param l_end: Index of end of left array
        :param r_end: Index of end of right array
        :return: None
        """
        r_start = l_end + 1

        # The lists may already be sorted - check easily by comparing edges
        if nums[l_end] <= arr[r_start]:
            return

        # While both lists are not exhausted
        while l_start <= l_end and r_start <= r_end:
            if nums[l_start] <= nums[r_start]:
                l_start += 1
            else:
                # We need to insert r_start's value before l_start
                tmp = arr[r_start]
                idx = r_start

                # Shift all elements between element 1 and element 2 right by one
                while idx != l_start:
                    # "Shift elements right"
                    arr[idx] = arr[idx - 1]
                    idx -= 1

                arr[l_start] = tmp

                # Update all pointers (we've moved an element from the right list into the left one)
                l_start += 1
                l_end += 1  # Think about why this makes sense, given that we've increased the size of the left array
                r_start += 1

    def merge_sort_in_place(nums: list[int], left: int, right: int) -> None:
        if left < right:
            mid = left + (right - left) // 2

            # Sort the first and second halves
            merge_sort_in_place(nums, left, mid)
            merge_sort_in_place(nums, mid + 1, right)

            # Merge the results
            merge_in_place(nums, left, mid, right)

    merge_sort_in_place(nums, 0, len(nums) - 1)

arr1 = [3,1,6,3,5,7,8,3]
in_place_merge_sort(arr1)
assert arr1 == [1, 3, 3, 3, 5, 6, 7, 8]

arr2 = [1,3,51,2,54]
in_place_merge_sort(arr2)
assert arr2 == [1,2,3,51,54]

arr3 = []
in_place_merge_sort(arr3)
assert arr3 == []