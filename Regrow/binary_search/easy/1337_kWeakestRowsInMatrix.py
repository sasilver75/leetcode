"""
K Weakest Rows in Matrix

Given an m * n binary matrix `mat` of:
    - 1's representing SOLDIERS
    - 0's representing CIVILIANS

These soldiers are positioned in FRONT of the civilians.
That is, all the 1s will appear to the LEFT of all the 0s in each row

A row `i` is WEAKER than row `j` if one of the following is true:
    - The number of soldiers in row i is less than the number of soldiers in row j
    - Both rows have the same number of soldiers and i < j

Return the INDICES o the k weakest rows in the matrix, ordered from weakest
to strongest.
"""
def count_soldiers_naive(city: list[int]) -> int:
    # O(N) Time
    return sum(city)

def count_soldiers_bs(city: list[int]) -> int:
    # O(LogN) Time
    left, right = 0, len(city) - 1

    # Find the leftmost 0; that index is how many soldiers there are
    # If it remains -1, it's all soldiers, so return len(city)

    last_seen_zero = -1
    while left <= right:
        mid_idx = left + (right - left) // 2
        mid_val = city[mid_idx]

        if mid_val == 0:
            # civilian
            last_seen_zero = mid_idx
            right = mid_idx - 1
        else:
            # soldier
            left = mid_idx + 1

    # If we haven't found any civillians, they're all soldiers!
    return last_seen_zero if last_seen_zero != -1 else len(city)



def kWeakestRows(mat: list[list[int]], k: int) -> int:
    # Process the rows into (rowNumber, n_soldiers)
    city_stats = [
        (idx, count_soldiers_bs(city))
        for idx, city in enumerate(mat)
    ]
    print(city_stats)
    # Sort by n_soldiers ASC
    city_stats.sort(key=lambda tup: tup[1])

    # Return indices of first k
    ans = [tup[0] for tup in city_stats[:k]]
    print(ans)
    return ans



def test(fn):
    assert fn([
        [1, 1, 0, 0, 0],
        [1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [1, 1, 1, 1, 1]
    ], k=3) == [2, 0, 3]

    assert fn([
        [1, 0, 0, 0],
        [1, 1, 1, 1],
        [1, 0, 0, 0],
        [1, 0, 0, 0]
    ], k=2) == [0, 2]

test(kWeakestRows)