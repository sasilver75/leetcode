from collections import defaultdict
"""
Longest Substring without Repeating Characters

Given a string s, find the length of the LONGEST substring WITHOUT REPEATING CHARACTERS!

Sam Note: It looks like there's actually a difference between "substring" and "subsequence"
It seems like substrings must be contiguous, whereas subsequences don't have to be - but do have to be ordered, at least?
"""

"""
Thinking:
I think this is one of the ones where... We have a sliding window of some sort, but the size of the window is dynamic.

1) Grow the window rightward while {condition} is satisfied
2) Once {condition} is violated, shrink the window from the left side until the condition is no longer violated
3) Continue to Grow the window rightward while {condition} is satisfied
...
4) We can stop when the rightward edge of the window hits the end of the array. Why? Because at that point we'll only be shrinking the window.
And the window was only ever as large as the largest [condition-satisfying substring] in the past -- and we won't top that by shrinking the window.
"""


def longest_substring_without_repeating_characters(s: str) -> int:
    def has_repeats(chars: str):
        return len(chars) != len(set(chars))

    l, r = 0, 0
    longest = 0
    while r < len(s):
        slice = s[l:r + 1]

        if has_repeats(slice):
            # Shrink left
            l += 1
        else:
            # Update longest? + Grow right
            longest = max(longest, len(slice))
            r += 1

    print(longest)
    return longest

"""
Okay, the above worked... but I didn't love that we had to do a linear scan of the slice at every iteration. That's O(N^2) in the worst 
case where we just expand the right all the way to the end without moving left. I don't think we can get around the O(N) memory requirement 
of maintaining some sort of window.

What sort of data structure can we maintain? It's pretty much a set that allows for TWO elements and errors or something when a third is attempted to 
be added?
Could we just use a defaultdict with a list?

So when we expand it, we add a number to the list?
How would we check for violations? We'd have to check every key in the dict, which still in the worst case could be 26+ checks...
Unless we kept track of the key that was violating?
Oh, we actually don't need to even keep a list -- just the count, right?
"""

def longest_substring_without_repeating_characters_2(s: str) -> int:
    if not s:
        return 0

    l, r = 0, 0
    # window = defaultdict(lambda: 0)
    window = set(s[0])
    violating_char = None
    longest_window = 1

    while r < len(s) - 1:

        while violating_char:
            # Remove l character, increment l, check if we've un-violated
            l_char = s[l]

            if l_char != violating_char: # If we just expanded rightward to a violating state, we don't want to remove that character from the window when we shrink on the left side -- becuase that character IS contained in the left side of the window,.
                window.remove(l_char)
            l += 1

            if l_char == violating_char:
                violating_char = None

        # Collapse Left in
        while not violating_char:
            r += 1
            r_char = s[r]

            # Did the expansion cause a violation?
            if r_char in window:
                violating_char = r_char
            else:
                # If not, we can add to window and update longest_window
                window.add(r_char)
                longest_window = max(longest_window, len(window))

    print(longest_window)
    return longest_window

assert longest_substring_without_repeating_characters("abcabcbb") == 3  # abcabcbb
assert longest_substring_without_repeating_characters("bbbbb") == 1  # bbbbb
assert longest_substring_without_repeating_characters("pwwkew") == 3  # wke

print("---")

assert longest_substring_without_repeating_characters_2("abcabcbb") == 3  # abcabcbb
assert longest_substring_without_repeating_characters_2("bbbbb") == 1  # bbbbb
assert longest_substring_without_repeating_characters_2("pwwkew") == 3  # wke
