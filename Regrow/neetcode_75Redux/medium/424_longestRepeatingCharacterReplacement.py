"""
Longest Repeating Character Replacement

You are given a string s and an integer k.

You can choose any character of the string and change it to
any other uppercase English character.

You can perform this operation at most k times.

Return the LENGTH of the longest substring containing the same letter that you can
get after performing the above operations!
"""
import collections

"""
I'm thinking about "expanding a window" out from each character

This would take O(N) time in the worst case for each on the N characters
for a total of O(N^2) time, I think.

What do I mean by expanding a window out from each character?

For each character, consider our target character as the starting character.
The window is starting at length 1, centered on the kth character
We have K characters that we can spend on either side of our current window

for _ in range(k):
    Expand the window either left or right (recurse in either direction)

"""

def longestRepeatingCharacterReplacementNaive(s: str, k) -> int:
    longest = 1

    def recursive(l_idx: int, r_idx: int, s_arr: list[str], starting_char: str, k_remaining: int) -> None:
        nonlocal longest

        # Extend left/right as possible for free, if we're in contiguous matching chars
        while l_idx > 0 and s[l_idx - 1] == s[l_idx]:
            l_idx -= 1
        while r_idx < len(s) - 1 and s_arr[r_idx + 1] == s_arr[r_idx]:
            r_idx += 1

        # If we have no more room to expand to or if we're out of characters, determine the length and update, then exit
        if k_remaining == 0 or (l_idx == 0 and r_idx == len(s_arr) - 1):
            longest = max(longest, r_idx - l_idx + 1)
            return

        # Spend a K to move left or right, if we can
        if l_idx > 0:  # If we can even extend left,
            next_s_arr = s_arr.copy()
            next_s_arr[l_idx-1] = starting_char
            recursive(l_idx - 1, r_idx, next_s_arr, starting_char, k_remaining - 1)
        if r_idx < len(s) - 1:  # If there's room to expand right
            next_s_arr = s_arr.copy()
            next_s_arr[r_idx + 1] = starting_char
            recursive(l_idx, r_idx + 1, next_s_arr, starting_char, k_remaining - 1)

    s_arr = [c for c in s]
    for idx in range(len(s_arr)):
        recursive(idx, idx, s_arr, s[idx], k)

    print(longest)
    return longest


""""
Neetcode Longest Window Strategy

The idea is that we're goign to be sliding a window characterized by
[left, right] across the string by both:
* Expanding the right side (right += 1)
* Contracting the left side (left += 1)

We keep track of the COUNTS of characters that are included in the current span
using a dictionary

"""
def longestRepeatingCharacterReplacement(s: str, k:int) -> int:
    start = 0
    max_span_length = 0
    char_counts = collections.defaultdict(int)
    max_character_count = 0

    for end in range(len(s)):
        # Adding the current char to our range
        char = s[end]
        char_counts[char] += 1

        # Get the count of the most common character in span;
        # Instead of doing an O(N) check on the dict every time, we just keep a track of the highest we've seen, and check if the current char is greater
        max_character_count = max(max_character_count, char_counts[char])

        span_length = end - start + 1

        # SpanLength can be AT MOST MaxCharacterCount + k
        # Shrink the span until that is true
        while span_length - max_character_count > k:
            # Remove the left character from the character set
            char_counts[s[start]] -= 1
            start += 1

            # Q: Why do we not need to reevaluate max_character count too?
            span_length = end - start + 1

        # Update max span length
        max_span_length = max(max_span_length, span_length)

    return max_span_length


"""
Neetcode Explanation

Consider ABABBA
For the substring _BABB_
Which character above would we want to replace in order to get the longest
substring with the same character?
- We'd want to replace A, the character that's the LEAST FREQUENT

In other words: 
We want all characters in a particular window to match THE MOST COMMON/FREQUENT
character in that window!

We're going to use a hashmap to count the number of occurrences of each character
in the substring

For _BABB_ , and K=2, this would be {B: 3, A: 1}

Now, how do we know that this _BABB_ substring is valid or can be made valid,
given K?

The length of this window is 4
The count of the most-common character is 3 (B)
Because 4-3 <= k, we know that this substring is/can be made valid by swapping!

Again: Our substring is "valid" IFF:
WINDOW_LENGTH - COUNT_OF_MOST_FREQUENT_CHAR <= K 

In our case, 4-3=1 
Tells us that there is 1 character that we need to replace in our window range
in order to make the window range all a single character.
Because 1 is less than or equal to K (our budget), we know that we can make this 
substring valid. 
"""
def longestRepeatingCharacterReplacementNaiveNeetcode(s: str, k: int) -> int:
    """Using the insight described above as a test rule"""
    longest = 0
    # Generate all substrings; Test for rule defined in Neetcode solution belo
    for start_index in range(len(s)):
        most_frequent_count = 0
        char_counts = collections.defaultdict(int)
        for end_index in range(start_index, len(s)):
            # Increment the count of char
            char = s[end_index]
            char_counts[char] += 1
            most_frequent_count = max(most_frequent_count, char_counts[char])
            # most_frequent_count = max(char_counts.values()) # This would also work, and is only O(26), since it's uppercase alphabetic

            # Test: Could we possibly change the substring s[start_index:end_index+1] to be all one character, based onthe count of the most common character
            ss_length = end_index - start_index + 1
            if ss_length - most_frequent_count <= k:
                # Then we could make this into a substring of the same char
                longest = max(longest, ss_length)

    return longest

"""
Okay, but can we use that same logic test of 

IF (SubstringLength - MostFrequentCount <= k)
    Success!
    
In a way that's faster than O(N^2), where we consider every possible substring?

We can do it in an O(N) sliding window approach, in fact! 

_BABB_
- We want to replace one character (WindowLength - Count[B])
- Because one is less than K=2, then our current window is valid, meaning
    we have enough replacements
    
Question: How are we going to know which character is the most frequent?
    - We can do an O(26) search of the char_counts dictionary (which will be of max size 26)
    - We could do a sliding window approach
    
ABABBA

- We take our window and start it at the beginning, and expand it for 
as long as we can by moving the right pointer ->, while the substring is valid
- Once the substring is NOT valid, we shrink the window until it is valid again,
by advancing the left pointer, checking for the valid condition each time.
"""
def longestRepeatingCharacterReplacementSlidingWindow(s: str, k: int) -> int:
    longest_window_length = 0
    char_counts = collections.defaultdict(int)

    start_idx = 0
    for end_idx in range(0, len(s)):
        # Add the character at s[end_idx] to our window
        char = s[end_idx]
        char_counts[char] += 1

        def is_window_valid() -> bool:
            window_length = end_idx - start_idx + 1
            # Can we spend <= k characters to get the window all to the same character (the most common one)?
            return window_length - max(char_counts.values()) <= k


        # If our window is violating the rule, shrink it until it's not
        while not is_window_valid():
            # Move left side of window to the right, decrmenting the count of the starting character
            start_char = s[start_idx]
            char_counts[start_char] -= 1
            start_idx += 1

        # Now that the window is valid, update the longest_window_length
        print("Valid Window: ", s[start_idx:end_idx+1])
        longest_window_length = max(longest_window_length, end_idx - start_idx + 1)

    print(longest_window_length)
    return longest_window_length



def test(fn):
    assert fn("ABAB", k=2) == 4  # AAAA or BBBB
    assert fn("AABABBA", k=1) == 4  # AABBBBA -> BBBB=4


# test(longestRepeatingCharacterReplacementNaive)
# test(longestRepeatingCharacterReplacementNaiveNeetcode)
test(longestRepeatingCharacterReplacementSlidingWindow)