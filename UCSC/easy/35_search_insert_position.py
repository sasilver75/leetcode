"""
Given a sorted array of distinct integers and a target value, return the index if the target is found.
 If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104

"""

def search_insert(nums: list[int], target: int) -> int:
    print("CALLED WITH ", nums, target)
    """
    This is basically a binary search problem
    Given a sorted list of nums, find a specific number

    BUT if the desired number isn't available, you should search for the point at which to insert them

    binary search works by taking a left and right index, finding the middle, considering the element at that idnex, and then updating teh left or right
    pointer appropriately.
    The termination is having l > r (I think l == r is fine)
    """
    l = 0
    r = len(nums)-1

    while l <= r:
        middle_index = l + ((r - l) // 2)  ## If r-l is 1, then 1//2 == 0
        middle_value = nums[middle_index]

        print(f"MIddle value: {middle_value}")

        if middle_value == target:
            return middle_index
        elif target > middle_value:
            l = middle_index + 1
        else:
            r = middle_index - 1

    return l


assert search_insert([1,3,5,6], 5) == 2, "Failed one"
assert search_insert([1,3,5,6], 2) == 1, "Failed two"
assert search_insert([1,3,5,6], 7) == 4, "Failed three"
    



def binary_search(nums: list[int], target:int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:

        mid = l + (r-l)//2
        mid_v = nums[mid]

        if mid_v == target:
            return mid
        elif mid_v > target:
            r = mid - 1
        else:
            l = mid + 1
    
    return l

print(binary_search([2], 3)) # 1
print(binary_search([1,2,3,4,5], 4)) # 3