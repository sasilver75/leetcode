"""
Longest Substring without Repeating Characters

Given a string s, find the LENGTH of the longest substring without
repeating characters.
"""

def length_of_longest_substring_without_repeats_naive(s: str) -> int:
    def is_without_repeats(s: str) -> bool:
        return len(s) == len(set(s))

    longest = 0

    for start_idx in range(len(s)):
        for end_idx in range(start_idx, len(s)):
            ss = s[start_idx: end_idx+1]
            if is_without_repeats(ss):
                longest = max(longest, len(ss))

    print(longest)
    return longest


"""
Okay, how could we do better than O(N^2)?
Sliding/Expanding Window?

Okay, like... we have a window... and we expand it while some condition is true (that we don't have any repeats)
When the condition is violated, we shrink the window.
This could be in O(N) time, if we can pull it off.

So how do we keep track of the elements that are in our window?
Can we use a set?
"""
def length_of_longest_substring_without_repeats(s: str) -> int:
    left = 0
    chars = set()
    max_length = 0
    for right in range(len(s)):

        # Consider the right character
        char = s[right]
        # TODO: Actually update max_length

        # Would adding right character put using a non-violating state? If so, adjust window such that it won't be violating
        if char in chars:
            # Remove UP TO the offending character
            while s[left] != char:
                chars.remove(s[left])
                left += 1
            # Remove the offending character
            chars.remove(s[left])
            left += 1

        # Add right character to our valid windows
        chars.add(s[right])

        # Update Window Length
        window_length = right - left + 1
        max_length = max(max_length, window_length)

    return max_length

"""
Noting: There's another way that we could do this where we keep track of the last occurrence of each character that we'rve esen, rather than keeping a set
of all of the characters in our window. If the last occurrence of the character currently being examined is at, say, 6, we just immediately move the "left" pointer to 
position 7.
I don't think this is asymptotically different than using a hashset.
"""

def test(fn):
    assert fn("abc") == 3
    assert fn("abcabcbb") == 3
    assert fn("bbbbb") == 1
    assert fn("pwwkew") == 3

# test(length_of_longest_substring_without_repeats_naive)
test(length_of_longest_substring_without_repeats)

