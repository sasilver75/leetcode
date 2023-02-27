"""
Word Break

Given a string s and a dictionary of strings wordDict, return TRUE if s can be segmented into a space-separated
sequence of one or more dictionary words

Note that the same word in the dictionary may be reused multiple times in the segmentation
"""


def word_break_naive(s: str, wordDict: list[str]) -> bool:
    def dfs(idx: int) -> bool:
        # Base Case: We've exhausted s using word_dict chomps
        if idx == len(s):
            return True

        word_options = [
            word for word in wordDict
            if s[idx: idx + len(word)] == word
        ]

        if not word_options:
            return False

        return any(
            dfs(idx + len(word))
            for word in word_options
        )

    return dfs(0)


# DP?
def word_break(s: str, wordDict: list[str]) -> bool:
    # dp[x] = can s[x:] be word_broken using word_dict?
    dp = [False] * (len(s) + 1)
    dp[-1] = True

    for idx in range(len(s), -1, -1):
        for word in wordDict:
            if idx + len(word) <= len(s) and word == s[idx:idx + len(word)] and dp[idx + len(word)] == True:
                dp[idx] = True

    return dp[0]


def test(fn):
    assert fn(s="leetcode", wordDict=["leet", "code"]) == True
    assert fn(s="applepenapple", wordDict=["apple", "pen"]) == True
    assert fn(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]) == False


test(word_break_naive)
test(word_break)
