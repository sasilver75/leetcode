"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

def longest_common_prefix(strs: list[str]) -> int:
    """
    I don't think that there's a huge trick to this one. We just use a pointer at the beginning of each of the strings,
    and increment that pointer until either one of our words runs out of length, or we get an IndexError after running out

    We don't even really need to keep track of the prefix as we go, we really just care about the first index at which
    """
    if not strs: return ""

    idx = 0
    while True: # !!! Will either run out of chars in a ss or hit a nonmatchin index across sss
        charset = set()
        for s in strs:
            try:
                charset.add(s[idx])
            except IndexError as e:
                # If we encounter an indexerror, one of our strings has ran out of length; We should return the current LCP
                return strs[0][:idx]
        if len(charset) > 1:
            # If there's more than one common character at the current position, we've already found our LCP
            return strs[0][:idx]
        idx += 1


cases = (
    (["flower","flow","flight"], "fl"),
    (["dog", "racecar", "car"], ""), # No common prefix
)

for i, o in cases:
    assert longest_common_prefix(i) == o
    print(i, o)
