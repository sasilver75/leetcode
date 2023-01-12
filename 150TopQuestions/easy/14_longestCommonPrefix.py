"""
Longest Common Prefix

Write a function to find the longest common prefix string amongst
an array of strings.

If there is no common prefix, return an empty string ""
"""

def longest_common_prefix(strings: list[str]) -> str:
    built = []
    # Insight: longest common prefix can only be as the shortest string
    shortest = min(strings, key=lambda s: len(s))

    for idx, char in enumerate(shortest):
        for s in strings:
            if not s[idx] == char:  # This index access should always be safe
                return "".join(built)
        built.append(char)
    return "".join(built)


assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"
assert longest_common_prefix(["dog", "racecar", "car"]) == ""
