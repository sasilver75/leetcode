"""
Longest Common SUBSEQUENCE

Given two strings `text1` and `text2`, return the LENGTH of their longest
common subsequence! If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string
with some characters (can be none) deleted without changing teh relative
order of the remaining characters
"""


def lcs_naive(text1: str, text2: str) -> int:
    def generate_subsequence(s: str) -> list[str]:
        subsequences = []

        def helper(idx: int, built: str):
            if idx == len(s):
                subsequences.append(built)
                return

            # Include or don't include the current character
            helper(idx+1, built+s[idx])
            helper(idx+1, built)

        helper(0, "")
        return subsequences

    subsequences_1 = generate_subsequence(text1)
    subsequences_2 = generate_subsequence(text2)
    max_length = 0

    for ss1 in subsequences_1:
        for ss2 in subsequences_2:
            if ss1 == ss2:
                max_length = max(max_length, len(ss1))

    return max_length


    """
    2-Dimensional DP!

    So what's the relationship between cells in DP?

    LCS(ace, abcde)

        a   b   c   d   e
    a   0   0   0   0   0
    c   0   0   0   0   0
    e   0   0   0   0   0

    Going row by row...
        dp[row][col] = 1 + dp[row-1][col-1]
                        if text1[row] == text2[col]
                         else max(dp[row-1][col], dp[row][col-1])

        a   b   c   d   e
    a   1   1   1   1   1
    c   1   1   2   2   2
    e   1   1   2   2   3

    dp[-1][-1] == 3 Yay :)

    So why is this DP relationship the case?

    If the characters "match", imagine that we're pairing them together and
    taking them out of the equation entirely. In that case, both strings are -1 in
    length, putting us back at [row-1][col-1].

    If the characters don't match, it'd be as if the "one" we just added (whether we were moving from the left
    or moving from the top)

     I think it's perhaps illustrative to look at LSS(AC, ACC) to see:

        c   c
    a   0   0
    c   1   1
    c   1   2

    Note that in these examples we were only ever referencing the "row above" (or the same row)
    when determining what we needed to fill in the cell. That means that we don't even need a
    whole DP table; we can get away with just a row! And if we can get away with just a row,
    then the SHORTER of the two text1/text2 should be used as that row.
    """
def lcs(text1: str, text2: str) -> int:
    dp = [[0] * len(text2) for _ in range(len(text1))]
    for row in range(len(dp)):
        for col in range(len(dp[0])):
            if text1[row] == text2[col]:
                dp[row][col] = 1 + (dp[row-1][col-1] if row-1 >= 0 and col-1 >= 0 else 0)
            else:
                left = dp[row][col-1] if col-1 >= 0 else 0
                above = dp[row-1][col] if row-1 >= 0 else 0
                dp[row][col] = max(left, above)

    return dp[-1][-1]

def test(fn):
    assert fn("abcde", "ace") == 3  # ace
    assert fn("abc", "abc") == 3  # abc
    assert fn("abc", "def") == 0  # no common substring

test(lcs_naive)
test(lcs)