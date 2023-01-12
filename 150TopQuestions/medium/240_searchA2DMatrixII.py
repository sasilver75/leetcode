"""
Search a 2D Matrix II

Write an efficient algorithm that searches for a value `target` in
an `m x n` integer matrix `matrix`. This matrix has the following properties:

* Integers IN EACH ROW are sorted in ascending from left to right
* Integers IN EACH COLUMN are sorted in ascending from left to right
"""

"""
Okay, this seems pretty straightforward from looking at the example
pictures that you can see here:
https://leetcode.com/problems/search-a-2d-matrix-ii/

So say in the first picture we're looking for 5, but we can't really
"see" the grid until we evaluate it.

A simple O(M*N) solution would just be to scan the entire grid, looking
for the value.

Can we go faster?

Say we had:

    1   4   7   11  15
    2   5   8   12  19
    3   6   9   16  22
    10  13  14  17  24
    18  21  23  26  30      Target: 5

We know that rows are ASC and columns are ASC

What rule should we use to constrain which columns we're looking through?
What rule should we use to constrain which rows we're looking through?

The columns are all of the columns with top values <= 5
The rows are all of the rows with left values <= 5

So I think we should do this with four pointers:

    TL              TR
LT  1   4   7   11  15
    2   5   8   12  19
    3   6   9   16  22      m rows: 5, n cols: 5
    10  13  14  17  24
LB  18  21  23  26  30      Target: 5


So we do an O(n) traversal to constrain the TL and TR
Then we do an O(m) traversal to constrain the  LT and LB

I get that we can search for an appropriate TR and LB limit, since we have
a target in mind... But can we actually move TL and LT?

If we can't... this is still going to be an O(MN) solution in the worst
case where we can't move TR and LB.

Or really, it'd be O(M*logN) or O(logM*N) if we b-search along either rows
or columns within the allowed ranges...


Actually, would this work?

1)  Constrain TR and LB using a binary search (or whatever)

    TL  TR            
LT  1   4   7   11  15
    2   5   8   12  19
LB  3   6   9   16  22      m rows: 5, n cols: 5
    10  13  14  17  24
    18  21  23  26  30      Target: 5
    

We're pretty much constrained us to:

    TL  TR            
LT  1   4   
    2   5   
LB  3   6   

Should we linearly scan, or can we do better?
Imagine this constrained grid is actually still very large...

We can constrain LT by:
Looking at the LAST element in each row.
    If the first element is <= target and the last element is >= target,
    then the row could contain our value...
    

LB: looking at FIRST value in row, search for the last one that's <= target.
    -> This is binary-searchable
LT: looking at FIRST AND LAST value in row, is it in range? 

TR: looking at FIRST value in col, search for last one that's <= target
TL: looking at FIRST AND LAST value in col, is it in range?

B-search remaining rows (or columns), whichever is longer (ie if you have two long rows remaining, binary search in teh horizontal direction) 
"""


def bsearch_for_limit(nums: list[int], target: int) -> int:
    # Search for the index of the last value <= target in list
    l, r = 0, len(nums) - 1

    while l <= r:
        mid_i = l + (r - l) // 2
        mid_v = nums[mid_i]

        # What does success look like? Where we're <= target and idx+1 > target. OR when mid_i is length-1 and mid_i < target
        if mid_i == len(nums) - 1 or (mid_v <= target < nums[mid_i + 1]):
            return mid_i
        elif target < mid_v:
            r = mid_i - 1
        else:
            l = mid_i + 1

    return mid_i


nums = [1, 3, 4, 5, 5, 7, 10]
target = 0
ans = bsearch_for_limit(nums, target)


# print(f"Ans: Value {nums[ans]} @ Index {ans}")

def bsearch_for_value(nums: list[int], target: int) -> int:
    # Return index of value, or -1 if it doesn't exist
    l, r = 0, len(nums) - 1

    while l <= r:
        mid_idx = l + (r - l) // 2
        mid_val = nums[mid_idx]

        if mid_val == target:
            return mid_idx
        elif target < mid_val:
            r = mid_idx - 1
        else:
            l = mid_idx + 1

    return -1


def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    if not matrix:
        return False

    # Assuming TL and LT will both be 0...

    # Stage 1: Constrain tr and lb
    col_heads = matrix[0]  # Top val of each column
    tr = bsearch_for_limit(col_heads, target)

    row_heads = [matrix[rowIdx][0] for rowIdx in range(len(matrix))]  # Left val of each row
    lb = bsearch_for_limit(row_heads, target)

    if tr >= lb:
        # Bsearch through each row, since they're longer (because tr > lb)
        for row_idx in range(lb + 1):
            row = matrix[row_idx]
            col_result = bsearch_for_value(row, target)
            if col_result != -1:
                return True

    else:
        # Bsearch through each column, since they're longer (because lb > tr)
        for col_idx in range(tr + 1):
            col = [matrix[row_idx][col_idx] for row_idx in range(lb)]
            row_result = bsearch_for_value(col, target)
            if row_result != -1:
                return True

    return False


"""
Hey, that worked! So we did an O(N) + O(M) scan of the head values
And then did either N*log(M) or M * log(N) binary scans of either rows or cols.
That's okay... But frankly it's not any better than just doing a binary scan
of every single row/col from the outset in worst-case.

How can we do better?
There's an O(N+M) solution, I believe.

                    C            
R   1   4   7   11  (15)
    2   5   8   12  19
    3   6   9   16  22      m rows: 5, n cols: 5
    10  13  14  17  24  
    18  21  23  26  30      target: 5 
    

We just have two pointers R(ow) and C(ol).

Consider the matrix[r][c] value, 15.
What can we say about this value?
    * Because 15 > 5, we know that 5 will not be contained in the current column, which only conatins values >= 15
        -> Therefore we'll next consider the column to the left
        
                C                
R   1   4   7  (11) _
    2   5   8   12  _
    3   6   9   16  _      m rows: 5, n cols: 5
    10  13  14  17  _  
    18  21  23  26  _       target: 5 

Consider the matrix[r][c] value, 11
What can we say about this value?
* Because 11 > 5, we know that 5 will not be contained in the current column, which only contains values >= 11
    -> Therefore we'll next consider the column to the left. 

            C            
R   1   4  (7)  _  _
    2   5   8   _  _
    3   6   9   _  _      m rows: 5, n cols: 5
    10  13  14  _  _  
    18  21  23  _  _      target: 5 

Consider the matrix[r][c] value, 11
What can we say about this value?
* Because 7 > 5, we know that 5 will not be contained in the current column,
    -> Therefore we'll next consider the column to the left
    
    
        C            
R   1  (4)  _   _  _
    2   5   _   _  _
    3   6   _   _  _      m rows: 5, n cols: 5
    10  13  _   _  _  
    18  21  _   _  _      target: 5 
    

Consider the matrix[r][c] value, 4
What can we say about this value?
* Because 4 < 5, we know that 5 could possibly be contained in this column, since all values in the column are >= 4
* Because 4 < 5, and we're considering the last element in the current orw, we know that the value won't be contained in the current row!
    -> Therefore we'll consider the row below
    

         C            
    _    _  _   _  _
R    2   (5)   _   _  _
    3   6   _   _  _      m rows: 5, n cols: 5
    10  13  _   _  _  
    18  21  _   _  _      target: 5
    
Target found! :) 
"""


def searchMatrixSmart(matrix: list[list[int]], target: int) -> bool:
    nrow = len(matrix)
    ncol = len(matrix[0])

    r = 0
    c = ncol - 1

    # While we're considering a valid matrix cell...
    while r < nrow and c >= 0:
        # The cell we're considering is the FIRST value of a column, and the LAST value of a row
        cell = matrix[r][c]

        if cell == target:
            return True

        # If target < cell, we know that target cannot be in this column, since column is all greater than cell
        if target < cell:
            c -= 1
        else:  # target > cell: Since cell is the largest value in the row, target cannot be in this row.
            r += 1

    return False


# -- Test Zone --

def test(fn):
    assert fn([[1, 4, 7, 11, 15],
               [2, 5, 8, 12, 19],
               [3, 6, 9, 16, 22],
               [10, 13, 14, 17, 24],
               [18, 21, 23, 26, 30]], target=5) == True

    assert fn([[1, 4, 7, 11, 15],
               [2, 5, 8, 12, 19],
               [3, 6, 9, 16, 22],
               [10, 13, 14, 17, 24],
               [18, 21, 23, 26, 30]], target=20) == False


test(searchMatrix)
test(searchMatrixSmart)
