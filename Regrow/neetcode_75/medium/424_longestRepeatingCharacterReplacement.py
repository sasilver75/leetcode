"""
Longest Repeating Character Replacement
Category: String

You are given string `s` and an integer `k`.
You can choose any character of the  string and change it to any other uppercase English character.
You can perform this operation at most `k` times.

Return the LENGTH of the longest substring containing the same letter you can
get after performing the above operation.
"""
import collections

"""
Thinking:

I'm thinking... Is there a way that we can preprocess the string
into a list counts = int[] where counts[i] is the number of identical characters
including and following the char @ s[i]?

AABABBA  -->  [2, 1, 1, 1, 2, 1, 1] 
Or it could be the inverse, where counts[i] is the count of successive characters
        --> [1, 2, 1, 1, 1, 2, 1]
        Second one perhaps seems more useful...

And the idea would be to try to bridge the largest numbers we can using the 
k characters that we have?
Ah, but this wouldn't work very well, because while the examples have only
[A, B] as characters, the instructions say that ANY uppercase english letter
might be used.
"""


def character_replacement_brute(s: str, k: int) -> int:
    max_length = 0

    def window_expander(left: int, right: int, char: str, k_remaining: int):
        nonlocal max_length
        if k_remaining == 0:
            # AABAA, k=1 --> We might have started on one side and used our k=1 to change B. Though we don't have k left, we should still expand l/r as much as we
            # can so we return 5 instead of 3

            # Expand freely left as appropriate
            while left - 1 >= 0 and s[left - 1] == char:
                left -= 1

            # Expand freely right as appropriate
            while right + 1 < len(s) and s[right+1] == char:
                right += 1

            max_length = max(max_length, right - left + 1)
            return

        # Expand either right or left
        if left - 1 >= 0:
            window_expander(
                left - 1, right, char, k_remaining - 1 if s[left - 1] != char else k_remaining
            )

        if right + 1 < len(s):
            window_expander(
                left, right + 1, char, k_remaining - 1 if s[right + 1] != char else k_remaining
            )

    for idx in range(len(s)):
        window_expander(idx, idx, s[idx], k)

    return max_length

"""
Can we do better than O(N^2) Time, O(1) Memory?

I don't think it's appropriate do any sort of sorting on the string.
How can we somehow do this in O(N) time? I imagine that would involve some subprobleming/DynamicProgramming, probably with
the use of more memory?

If we have CR(AABABBA, k=1), would knowing CR(ABABBA, k=1) help us? Only if we knew how many of k we actually used in the subproblem, right? Because both subproblems are 
sharing the same k budget. I don't know if this is appropriate either.
"""


"""
Here we go! :) 
So the idea here is that we're going to be sliding a window
characterized by [left, right] across the string by both:
    * expanding the right side (right += 1)
    * contracting the left side (left += 1)
    
We keep track of the counts of characters that are included 
in the current span. We do this with a dictionary.

Starting with [end, start] at 0,0... for end in range(len(s)):
    * Process the current character by adding it to char_counts
    
    * What's the charact
"""
def character_replacement(s: str, k: int) -> int:
    start = 0
    max_span_length = 0
    char_counts = collections.defaultdict(int)
    max_character_count = 0

    for end in range(len(s)):
        char = s[end]
        char_counts[char] += 1

        # Count of the most common character in span
        max_character_count = max(max_character_count, char_counts[char])

        span_length = end - start + 1

        # SpanLength can be AT MOST MaxCharacterCount + k...
        # Som if needed, shrink the span until that is true.
        while span_length - max_character_count > k:
            # Remove the left character from the character set
            char_counts[s[start]] -= 1
            start += 1

            # Q: Why do we not need to reevaluate max_character count too?
            span_length = end - start + 1

        # Update max span length
        max_span_length = max(max_span_length, span_length)

    return max_span_length







# -- Test --
def test(fn):
    # Replace the two As with two Bs or vice versa
    assert fn("ABAB", k=2) == 4

    # Replace one 'A' in the middle with 'B' and form AABBBBA.
    # The substring BBBB has the longest repeating letters, which is 4.
    assert fn("AABABBA", k=1) == 4

    assert fn("AABBA", k=1) == 3

test(character_replacement_brute) # O(N^2, O(1)
test(character_replacement)