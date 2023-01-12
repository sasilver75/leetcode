"""
Pascal's Triangle

Given an integer `numRows`, return the first numRows of Pacal's Triangle


                        1
                    1       1
                1       2       1
            1       3       3       1
        1       4       6       4       1


"""


def pascals_triangle(n_rows: int) -> list[list[int]]:
    rows = [[1], [1,1]]
    if n_rows <= 2:
        return rows[:n_rows]

    """
    Insight: Each row is the pair-wise sums of the previous row BOOKENDED by 1's
    """
    for n_row in range(2, n_rows):
        previous_row = rows[n_row-1]
        row = [1]
        for i in range(len(previous_row)-1):
            row.append(previous_row[i] + previous_row[i+1])
        row.append(1)
        rows.append(row)

    return rows

assert pascals_triangle(5) == [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
assert pascals_triangle(1) == [[1]]

