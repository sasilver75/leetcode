"""
Longest substring with at least K repeating characters

Given a string `s` and an integer `k`, return the LENGTH of the longest substring
of s such that the FREQUENCY OF EACH CHARACTER in the substring is greater than
or equal to K.
"""
from collections import Counter


def longestSubstringBrute(s: str, k: int) -> int:
    # 1) Generate all Substrings
    substrings = []
    for start in range(len(s)):
        for endInclusive in range(start, len(s)):
            substrings.append(s[start:endInclusive + 1])

    # 2) Select longest ss satisfying condition
    def satisfies(s: str, k: int):
        char_counts = Counter(s)
        return all(char_counts[char] >= k for char in char_counts)

    max(
        filter(lambda ss: satisfies(ss, k), substrings),
        key=len
    )


"""
How can we do better than N^3?
Can we do bottom-up DP?

dp[i] = longest substring starting at dp[i] that wouldn't violate rules?
dp[last] = 1
dp[i] = max(dp[i+1], dp[i+2], ...) + 1 if adding this character to that one wouldn't violate
OOPS, wrong -- that would be talking about a SUBSEQUENCE, which would also be a good problem :)


"aaabb", k=3 --> 3 ("aaa", as "a" is repeated 3 times
"ababbc", k=2 --> 5 ("ababb", since "a" appears 2 and "b" 3 times)


"ababbcaabc", k=2

What we do is... we count the occurrence of each character in the whole string
a: 4
b: 5
c: 1

For each character: Check if the value in the counts dict is 
"""


def longestSubstring(s: str, k: int) -> int:
    if not s:
        return 0

    # # Given a string, does it satisfy the charCount rule?
    char_counts = Counter(s)
    satisfies_rule = all(
        char_counts[char] >= k for char in char_counts
    )

    if satisfies_rule:
        return len(s)

    # Otherwise, use all the infrequent elements as "splits", and record the max-length split!
    start, end = 0, 0
    max_length = 0
    while end < len(s):
        if char_counts[s[end]] < k:
            # Split found!
            max_length = max(
                max_length,
                longestSubstring(s[start:end], k)  # excluding current index
            )
            start = end + 1  # We want to ignore the current end character in the next span
        end += 1

    # There's still one more span from start:[end of s] that we havent consdiered
    max_length = max(
        max_length,
        longestSubstring(s[start:], k)
    )
    return max_length


def test(fn):
    fn("aaabb", 3) == 3
    fn("ababbc", 2) == 5


test(longestSubstringBrute)
test(longestSubstring)
