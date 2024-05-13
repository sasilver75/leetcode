"""
Longest Substring without Repeating Characters

Given a string s, find the length of the LONGEST SUBSTRING without repeating characters!
"""


def lss_naive(s: str) -> int:
    # Generate all Substrings
    substrings = []
    for starting_index in range(len(s)):
        for ending_index in range(starting_index, len(s)):
            substrings.append(s[starting_index: ending_index + 1])

    # Filter Substrings to those without repeating characters (len(set(chars)) == len(chars))
    filtered_substrings = [
        ss for ss in substrings
        if len(set(ss)) == len(ss)
    ]

    # Return length of longest of Filtered Substrings
    return max([len(fs) for fs in filtered_substrings])

"""
How can we do this in better than N^3 time
Can we do it in N^2 time, perhaps by using more memory? Actually, I think we can do O(N)/O(N)!

It seems clear to me that longest substring is all about some {set of characters}, and that we might be growing this set/window of characters while we can, and then shrinking it when
we have to. 
So if we were to use some sort of sliding window approach, we'd start with two pointers (l, r) likely at 0,0. 
Let's say that we're going to use a set to keep track of the characters in our window (window).

while RightEdgeOfWindow can be expadned:
    # Can we expand the window rightward? Would doing so put our window in an invalid state (of having two of the same characters)?
        # If so, shrink the left side of the window until the addition of the right character would no longer put it into a violated state
    # Add the right character
    # Update the Max Length
    
    
Intuition for why `while r < len(s) - 1:`
- Once we get to the right edge of the window touching the right side of the string, we know that there aren't any future windows that will have a length greater than the current max_ss_length.
- Consider that we only grow the window size when that would increase the current substring length
- So we've already processed a window of length (eg) 5, which is now touching the rightward edge of the substring
- Every future position of the window (length 4, 3, 2, 1) are uninteresting, as we've already processed one of length 5 (including updating max_ss_length, if appropriate) 

"""
def lss(s: str) -> int:
    # Window of l,r is going to be INCLUSIVE
    # Charset includes the characters that are now in the window
    if not s:
        return 0
    l, r = 0, 0
    charset = set(s[0])
    max_ss_length = 1

    while r < len(s) - 1:
        # Expand Rightward
        r += 1
        right_char = s[r]

        # Before we add it, would adding this new right_char put our charset into violation?
        if right_char in charset:
            # If so, before we add rightchar, let's slide the left side of the window until the addition wouldn't put us in violation
            while right_char in charset:
                # Remove the leftmost char, inc l
                left_char = s[l]
                charset.remove(left_char)
                l += 1

        # Now add the right_char
        charset.add(right_char)

        # Does this put us
        max_ss_length = max(max_ss_length, len(charset))

    return max_ss_length




def test(fn):
    assert fn("abcd") == 4  # abcd
    assert fn("abcabcbb") == 3  # abc
    assert fn("bbbbb") == 1  # b
    assert fn("pwwkew") == 3  # wke/kew


test(lss_naive)
test(lss)
