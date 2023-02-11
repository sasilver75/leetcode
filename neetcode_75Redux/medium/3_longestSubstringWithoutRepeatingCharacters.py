"""
Longest Substring without Repeating Characters

Given a string `s`, find the LENGTH of the LONGEST SUBSTRING
WITHOUT repeating characters.

"""

"""
Sam Note:
Notice:
    - We're talking about SUBSTRINGS, so the spans need to be contiguous
    - We're talking about the LENGTH of the longest substring
"""

def lsswrc_naivest(s: str) -> int:
    # Generate all and store substrings
    substrings = []
    for start_index in range(0, len(s)):
        for end_index in range(start_index, len(s)):
            substrings.append(s[start_index: end_index+1])

    # Process them
    longest = 0
    for ss in substrings:
        if len(set(ss)) == len(ss):
            longest = max(longest, len(ss))

    return longest

def lsswrc_naive(s: str) -> int:
    # Generate and process in one go
    longest = 0
    for start_index in range(len(s)):
        for end_index in range(start_index, len(s)):
            ss = s[start_index:end_index+1]
            n_elements = len(ss)
            n_uniq_elements = len(set(ss))
            if n_elements == n_uniq_elements:
                # All elements are unique; no repeating chars; update longest
                longest = max(longest, n_elements)
    return longest


"""
Can we do better than O(N^2), perhaps by using additional memory?
We know that at a minimum, each substring of length 1 exists and has no repeating chars
Can we use that as a base for our SSWRC?
And do a DP table?
I think each spot would have to have a tuple of (CountLSSWRC, CharsUsedSet)

This is O(N), but is a little memory-intensive.
"""
def lsswrc_dp(s: str) -> int:
    dp = [(1, set([char])) for char in s]

    # Populate it backwards
    for idx in range(len(dp)-2, -1, -1):
        # Can we improve the current one by extending the SS to the right of it?
        char = s[idx]
        if char not in dp[idx+1][1]:
            # Extend the SS to the right copying it and then incrementing the count and adding to set
            dp[idx] = (dp[idx+1][0]+1, dp[idx+1][1])
            dp[idx][1].add(char)

    return max(position[0] for position in dp)


"""
There's a sort of crackhead leetcode solution:

We can use a sliding window approach, where we expand the window as we
encounter characters that we haven't seen in the [start, end] interval.

We don't explicitly keep track of the members of the interval. Instead, we keep
track of the "last seen index" of every character that we've seen. When we 
want to check whether a character is in the [start, end] interval 

---- EXPANDING WINDOW EXPLANATION ----

The idea is that we're moving an end_index (think: end of the substring) pointer
across the string characters. Most of our attention is focused on the character that the 
end_idx is on. I'll call that character the "current character". 

Our question is whether we can add this character to current substring or not,
with the current substring being characterized as the [start_idx:end_idx+1] substring

In order to determine if we can actually add the current character to our substring,
we want to know if that same character already exists in our substring.
The way we do this is we keep a dict of char_last_seen_at, which has the last occurrence
of each character, as we've seen them.
So if we're currently at "r", we look to see if char_last_seen_at["r"] (if that entry exists)
has an index location that's in our current from start_idx to last_index. 

IF IT IS:
    Then we CANNOT INITIALLY include the character at end_idx in our substring -- 
    But we can include it if we slide the left side of our substring (start_idx)
    up to PAST the occurrence of this current_char.
    To do this, we set start_idx = char_last_seen_at["r"] + 1
IF IT'S NOT:
    Then we CAN include the character at end_idx in our substring 

We can then determine the new length of the substring, and update the max length
of the substring.
- Note: There's an optimization that doesn't change the asymptotic complexity
that just says that we don't need to determineLength/updateMax when we had to
shrink the window, because there's no way that this shrunken window length is 
going to update the max.

Then, no matter what, we want to update the char_last_seen_at[current_char] to
end_index, the current index that we're considering.

Then, we move to the next end_index and repeat the process.
 
"""
def lsswrc_neetcode(s: str) -> int:
    """
    O(N) time and O(N) space
    """
    max_length = 0
    char_last_seen_at = {}
    start_idx = 0

    for end_idx in range(len(s)):
        char = s[end_idx]

        # If the current character being considered was seen in the [start_idx, end_idx] span
        if char in char_last_seen_at and start_idx <= char_last_seen_at[char]:
            # Then our [start, end] substring is "over: -- advance start to the next position
            start_idx = char_last_seen_at[char]+1
            # Our length has gotten shorter, so no need to update the max length
        else:
            # Otherwise, we HAVEN'T seen this character in the current substring from start...end
            # So we're including it in the substring
            substring_length = end_idx - start_idx + 1
            max_length = max(max_length, substring_length)

        # No matter what, we update the "last_seen_at" of the current char at end
        char_last_seen_at[char] = end_idx

    return max_length



def test(fn):
    assert fn("abc") == 3 #abc
    assert fn("abcabcbb") == 3 #abc
    assert fn("bbbbb") == 1 #b
    assert fn("pwwkew") == 3 #wke

test(lsswrc_naivest)
test(lsswrc_naive)
test(lsswrc_dp)
test(lsswrc_neetcode)