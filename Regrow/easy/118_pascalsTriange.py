"""
Given an Integer numRows, return the first numRows of Pascal's Triangle!
In Pascal's Triangle, each number is the sum of hte two numbers directly above it
as shown:

                1
            1       1
        1       2       1
    1       3       3       1
1       4       6       4      1
"""

def numRows(n_rows: int) -> list[list[int]]:
    acc = []
    for row_n in range(n_rows):
        if row_n == 0:
            acc.append([1])
        elif row_n == 1:
            acc.append([1, 1])
        else:
            row_acc = []
            last_row = acc[-1]

            # Append 1 on left edge
            row_acc.append(1)

            # Two pointer Sums over previous row values to get interior values
            lead_idx = 1
            while lead_idx < len(last_row):
                child_sum = last_row[lead_idx] + last_row[lead_idx - 1]
                row_acc.append(child_sum)
                lead_idx += 1

            # Append 1 on right edge
            row_acc.append(1)

            # Append row_acc to acc
            acc.append(row_acc)
    return acc




# Case 1
"""
        1
      1   1
    1   2   1
  1   3   3   1
1   4  6   4   1
"""
print(numRows(5))
# AnsweR: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# Case 2
print(numRows(1))
# Answer: [[1]]

