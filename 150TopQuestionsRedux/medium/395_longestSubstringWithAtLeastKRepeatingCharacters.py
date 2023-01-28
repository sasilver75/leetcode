"""
Longest Substring with at least K Repeating Characters

Given a string `s` and an integer `k`, return the length of the longest
substring of `s` such that the frequency of each character in the substring
is greater than or equal to k.
"""
import collections


def longestSubstringNaive(s: str, k: int) -> int:
    # 1. Generate all Substrings
    substrings = []
    for start_index in range(len(s)):
        for end_index in range(start_index, len(s)):
            substrings.append(s[start_index: end_index+1])

    # 2. Get character counts of each
    substrings_with_char_counts = [
        (ss, collections.Counter(ss)) for ss in substrings
    ]

    # 3. Filter to substrings with appropriate character counts
    appropriate_substrings = [
        ss
        for ss, counts in substrings_with_char_counts
        if all(
            counts[key] >= k
            for key in counts
        )
    ]

    # 4. Return the max length
    return max(len(ss) for ss in appropriate_substrings) if appropriate_substrings else 0


"""
Problem with this one is still that for every step, the 
"check if we've satisfied all counts" step still takes O(N) time, so
that turns this O(N^2) loop into an O(N^3) result.
This is still better than the first result, I think.
"""
def longestSubstringNaiveBetter(s: str, k: int) -> int:
    longest_substring_length = 0
    for start_index in range(len(s)):
        counter = collections.defaultdict(int)
        for end_index in range(start_index, len(s)):
            counter[s[end_index]] += 1
            if all(
                counter[key] >= k
                for key in counter
            ):
                longest_substring_length = max(longest_substring_length, end_index - start_index + 1)
    return longest_substring_length


"""
How can we speed this up, perhaps to O(N^2)?

Here's an example:

s= ababbcdeddf     k=2

The answer is ababb -> length = 5

The way we go about this is to iterate over the entire input string s, getting counts for characters

counts = {
    a: 2,
    b: 3,
    c: 1,
    d: 3,
    e: 1,
    f: 1
} 

Note that given that k=2... whatever substring we end up using as our longest one, it's necessarily NOT going to include
any of the elements with counts[element] < 2. In this case, this means that our longest substring satisfying our condition
cannot include any of [c, e, f].

In other words, none of the elements below that are bracketed can be included in the substring.

ababb[c]d[e]dd[f]

Consider now that the solution has to be within one of the "remaining" subarrays that result from SPLITTING on these
"failed" characters that I described and bracketed above.

ie the solution has to be within one of:

'ababb'
'd'
'dd'
''  (If we consider that splitting on the last element would result in an empty element in the "split" list of iterables

In this case, the solution (ababb) happens to be one of the resulting substrings, but it's possible that the solution
is simply "within" one of the resulting substrings. 
You might be able to guess that we're going to have to recurse into each of these with our same function, and take the max of eachh
as our longest substring satisfying condition.

"""
def longestSubstring(s: str, k: int) -> int:
    """
    Find the length of the longest substring in s where each element in s is repeated at least k times

    :param s: string being searched
    :param k: number of times each element must occur in selected substring
    :return: the length of the longest substring in s having >= k occurrences of each element
    """
    print(f"Called on = {s}")

    # Get character counts
    char_counts = collections.Counter(s)

    # Does the given string outright satisfy our condition?
    unsatisfying_chars = {char for char in char_counts if char_counts[char] < k}
    if not unsatisfying_chars:
        return len(s)

    print(f"{unsatisfying_chars = }")

    # We have some characters in s that don't have enough counts. We need to split on these characters.
    substring_candidates = []
    start = 0
    for idx, char in enumerate(s):
        if char in unsatisfying_chars:
            substring_candidates.append(s[start:idx])
            start = idx + 1

    # There's may still be one more span in s from start:idx+1
    substring_candidates.append(s[start:idx+1])

    print(f"{substring_candidates = }")

    return max(
        longestSubstring(substring, k)
        for substring in substring_candidates
    ) if substring_candidates else False




















def test(fn):
    assert fn("ababbcdeddf", k=2) == 5 # ababb
    assert fn("abc", k=2) == 0
    assert fn("aaabb", k=3) == 3  # aaa
    assert fn("ababbc", k=2) == 5  # ababb

# test(longestSubstringNaive)
# test(longestSubstringNaiveBetter)
test(longestSubstring)