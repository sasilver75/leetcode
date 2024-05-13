"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings

If there is no commmon prefix, return an empty string ""
"""

"""
I think this can just be accomplished by having a pointer for earch string and advancing them linearly across
each string, exiting when we don't 
"""
def longest_common_prefix(strs: list[str]) -> str:
    if not strs:
        return 0

    idx = 0
    min_length = min(len(s) for s in strs)

    # Move idx forward while we're still in common-length territory and all s[idx] equal eachother (using the first string as a reference to compare to)
    while idx < min_length and all(
        s[idx] == strs[0][idx]
        for s in strs
    ):
        idx += 1

    return strs[0][:idx]



assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"
assert longest_common_prefix(["dog", "racecar", "car"]) == ""