def longest_common_prefix(strings: list[str]) -> str:
    prefix = []
    i = 0
    while True:
        match_char = None
        for s in strings:
            # Try to access the i'th char in the current string. If we can't, then return the prefix so far
            try:
                current_char = s[i]
            except IndexError:
                return "".join(prefix)
            # If there isn't a match char set yet for ith iteration, set it (first string)
            match_char = match_char or current_char
            # If there isn't a match between currentChar and matchChar, return prefix so far
            if current_char != match_char:
                return "".join(prefix)
        # Got through all the strings! Add to prefix and increment
        prefix.append(match_char)
        i += 1


def test(fn):
    cases = [
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
    ]
    for inp, soln in cases:
        ans = fn(inp)
        print(f"input: {inp}")
        print(f"ans: {ans}")
        print(f"correct: {ans == soln} \n")


test(longest_common_prefix)
