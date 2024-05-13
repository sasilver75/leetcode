"""
Word Break
Category: DP

Given a string `s` and a dictionary of strings `wordDict`, return
`true` if `s` can be segmented into a space-separated sequence of one
or more dictionary words.

NOTE: The same word in the dictionary may be reused multiple
times in the segmentation.
"""


def word_break_naive(s: str, words: list[str]):
    def helper(idx: int = 0):
        if idx >= len(s):  # Is the word exhausted? Yay!
            return True

        return any(
            helper(idx + len(word))
            for word in words
            if word == s[idx:idx + len(word)]
        )

    return helper()


def word_break_prefix_tree(s: str, words: list[str]) -> bool:
    # Same idea as above, but if we processed words into a trie, we wouldn't
    # have to do O(N) work every recursive action... Just O(longest word)
    # This woudl be better perhaps in some cases, unless a word were VERY long
    pass


"""
How can we do better?

Formulating this as a dynamic programming question...

Say we had "leetcode" and ["leet", "code"]

For WB("leetcode", ["leet", "code"])


"""


def word_break(s: str, words: list[str]):
    # "ABC" -> [?, ?, ?, True]
    dp = [False] * (len(s) + 1)  # Where dp[i] whether you could break s[i:]
    dp[-1] = True  # Representing "" --> That's already exhausted! :)

    # Now let's do the bottom-up approach, going through every index in reverse
    for i in range(len(s) - 1, -1, -1):
        for w in words:
            # starting at position i, does the string s even have enough characters?
            # If we can take a bite from the tail using this word and the bit substring matches word
            if (i + len(w)) <= len(s) and s[i: i + len(w)] == w:
                dp[i] = dp[i + len(w)]

            # If we already set dp[i] = True, we don't need to check the rest of the words (Optional)
            if dp[i]:
                break;

    return dp[0]



# -- Test --
def test(fn):
    fn("leetcode", ["leet", "code"]) == True
    fn("applepenapple", ["apple", "pen"]) == True
    fn("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False


test(word_break_naive)
test(word_break)
