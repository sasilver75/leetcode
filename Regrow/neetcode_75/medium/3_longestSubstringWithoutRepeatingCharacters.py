"""
Longest Substring without Repeating Characters
Category: String

Given a string `s`, find the LENGTH of the longest substring without repeating
characters!
"""


def length_of_longest_unique_substring_brute(s: str) -> int:
    # Generate all substrings:
    substrings = []
    for start in range(len(s)):
        for end in range(start, len(s)):
            substrings.append(s[start:end + 1])

    # for each substring, if it's unique, consider its length
    max_length = 0
    for ss in substrings:
        if len(ss) == len(set(ss)):
            max_length = max(max_length, len(ss))

    return max_length


"""
How can we do better?
Would knowing subproblems help us out?

If we wanted to know:
    LLUS(pwwkew), would know LLUS(wwkew) help us out? It could, I suppose!
    LLUS(pwwkew) = 1 + LLUS(wwkew) if p is not in wwkew else LLUS(wwkew)

So I think there are two options -- one more memory intensive, one more time intensive

Option 1: Memory Intensive
    dp[(1 s[i]), ...] of length len(s)
    dp[i] = (length of longest unique substring in s[i:], {characters in substring})
    dp[i] = (dp[i+1][0]+1, {*dp[i+1][1], s[i]}) if s[i] not in dp[i+1][1] else dp[i]

Option 2: Compute Intensive 
    dp[1, ...] of length(s)
    d[i] = length of longest unique substring in s[i:]
    d[i] = d[i+1] +1 if s[i] not in s[i+1:i+1+d[i+1]] else d[i]

"""


def length_of_longest_unique_substring_memory(s: str) -> int:
    # O(N) Time, O(N^2) Memory
    dp = [(1, {s[i]}) for i in range(len(s))]
    for i in range(len(s) - 2, -1, -1):
        # Can we extend the following subsequence?
        if s[i] not in dp[i + 1][1]:
            new_substring_set = dp[i + 1][1].copy()
            new_substring_set.add(s[i])
            dp[i] = (dp[i + 1][0] + 1, new_substring_set)

    return max(tup[0] for tup in dp)


def length_of_longest_unique_substring_time(s: str) -> int:
    # O(N^2) Time, O(N) Memory
    dp = [1] * len(s)
    for i in range(len(s) - 2, -1, -1):
        adjacent_substring_length = dp[i + 1]
        if not any(
                s[i + step] == s[i]
                for step in range(1, adjacent_substring_length + 1)
        ):
            dp[i] = dp[i + 1] + 1

    return max(dp)


"""
Are there any other ways from the Leetcode solutions?

We can use a sliding window approach, where we expand the window as we
encounter characters that we haven't seen in the [start, end] interval.

We don't explicitly keep track of the members of the interval. Instead, we keep
track of the "last seen index" of every character that we've seen. When we 
want to check whether a character is in the [start, end] interval 
"""
def length_of_longest_unique_substring(s: str) -> int:
    """
    O(N) time and O(N) space
    """
    max_length = 0
    char_last_seen_at = {}
    start_idx = 0

    for end_idx in range(len(s)):
        char = s[end_idx]
        # If the current character being considered was seen in the [start_idx ... end_idx] span
        if char in char_last_seen_at and start_idx <= char_last_seen_at[char]:
            # then our [start, end] substring is "over" - advance start to the next position
            start_idx = char_last_seen_at[char] + 1
        else:
            # Otherwise, we haven't seen this character in the current substring.
            substring_length = end_idx - start_idx + 1
            max_length = max(max_length, substring_length)

        # No matter what, we update the "last seen at" of the char
        char_last_seen_at[char] = end_idx

    return max_length


def length_of_longest_unique_substring_set(s: str) -> int:
    """
    Would we be able to use just a set, instead of the complicated dict?
    Yes! This is still O(N)/O(N), but I think it's a bit cleaner than having to
    deal with a bunch of index pointers.

    *** OH NO! This ACTUALLY **DOES NOT WORK**!
    Consider the "ABACD" example. The longest here is the BACD at the end.
    This code will, once it encounters the second A, just DUMP its progress
    on the ground. That's not what we want!

    And it's not like we can only drop "A" from the set...
    because it's possible that the set contains elements from "prior to A."
    The notion of order IS important, it seems?

    Example:
    FABACDE

    By the time we get to the second A, we have {FAB} (3)
    How do we know that we should be dropping BOTH F and A?
    We would need some notion of ordering.
    So we would need to keep both something like a queue AND a set

    {FAB}
    would also be [F,A,B]
    And when we run into A, we would set.remove(popLeft()) until we get to A,
    leaving just {B} and [B]
    But that sequence of Pops would perhaps increase the time complexity above O(N).

    So how does the example above with the dict avoid this situation?


    At the interesting point:
    FABACDE
       ^

    {
        F:  0
        A:  1
        B:  2
    }
    start=0
    end=3

    We see that A is in our interval, since
        LastSeenAt(A) == 1
        and 1 >= start

    So... we don't have to do anything out of the usual to our "membership set",
    because we aren't maintaining one -- just last seen indices. The membership
    set is implicit because its size is just end - start + 1.

    We just update the beginning of our interval to start at
    the index "just after" the "last seen at" for the already-in-interval character.

    start = 2
    end = 3
    i.e. for FABACDE, the interval goes from FAB to BA...soon to grow to BACDE

    """
    max_length = 0
    substring_chars = set()

    for char in s:
        # If char is not in interval, add it to interval and update max_length
        if char not in substring_chars:
            substring_chars.add(char)
            max_length = max(max_length, len(substring_chars)) # We can use len(substring_chars) here instead of end-start+1
        else:
            substring_chars = set()

    return max_length




def test(fn):
    assert fn("abcabcbb") == 3  # abc
    assert fn("bbbbb") == 1  # b
    assert fn("pwwkew") == 3  # wke
    assert fn("abacd") == 4


test(length_of_longest_unique_substring_brute)
test(length_of_longest_unique_substring_memory)
test(length_of_longest_unique_substring_time)
test(length_of_longest_unique_substring)
# test(length_of_longest_unique_substring_set) # Does not work, see comment in function for learning!