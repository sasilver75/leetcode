"""
Sort Colors

Given an array `nums` with `n` objects colored red/white/blue,
sort them IN PLACE so that objects of the same color are adjacent,
with the colors in the order red, white, and blue.

We'll use the integers 0, 1, and 2 to represent the colors red/white/blue,
respectively.

You must solve this without using the library's sort function.
"""

"""
Bubble Sort:

The algorithm starts by comparing the first two elements of the list. If the first element is larger than the second, they are swapped.

The algorithm then moves to the next pair of elements and compares them. If the second element is larger than the third, they are swapped. This process continues until the end of the list is reached.

After one pass through the list, the largest element will have "bubbled" to the end of the list. The algorithm then repeats step 2, but ignores the last element of the list since it is already in the correct position.

The process of comparing and swapping elements is repeated for each element of the list, with one less element considered each time, until the entire list is sorted.

The algorithm's time complexity is O(n^2) in the worst and average case, which makes it less efficient for large lists. However, it has the advantage of being a simple and easy-to-understand algorithm, making it a good choice for small lists or as an educational tool.
"""


def sort_colors_naive(nums: list[int]) -> None:
    # Using Bubblesort to Sort In-Place in O(N^2)/O(1)
    n = len(nums)

    # Do n passes of this: Compare elements pair-wise, bubbling up (swapping) the larger one. For every 1 of the n passes, this results in the largest element making its way to the top.
    for i in range(n):
        # The last i elements are already in place
        for j in range(n - i - 1):
            # Traverse the list from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


"""
There are several performant in-place sorting algorithms available.
Even merge sort can be adapted to be an in-place, too!
"""


def sort_colors(nums: list[int]) -> None:
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


def test(fn):
    nums = [2, 0, 2, 1, 1, 0]
    fn(nums)
    assert nums == [0, 0, 1, 1, 2, 2]

    nums = [2, 0, 1]
    fn(nums)
    assert nums == [0, 1, 2]


test(sort_colors_naive)
test(sort_colors)
