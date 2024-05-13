"""
Counter and Say

The CountAndSay sequence is a sequence of digit strings defined by the recursive formula:

- countAndSay(1) = "1"
- countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1)
which is then converted into a different digit string

To determine how you "say" a digit string:
 1) Split it into the minimal number of substrings such that each substring
 contains exactly one unique digit.
2) Then, for each substring, say the number of digits, then say the digit.
3) Finally, concatenate every said digit.

For example: "3322251"
= two 3's, three 2's, one 5, one 1
= 2 3 + 3 2 + 1 5 + 1 1
= "23321511"

Given a positive integer n, rethrn the nth term of the count-any-say sequence
"""

def count_and_say(s: str):
    acc = ""
    count = 0
    match_char = s[0]
    for char in s:
        if char != match_char:
            acc += f"{count}{match_char}"
            count = 1
            match_char = char
        else:
            count += 1

    if count:
        acc += f"{count}{match_char}"

    return acc


def nth_count_and_say(n: int) -> str:
    if n == 1:
        return "1"

    register = "1"
    for _ in range(2, n+1):
        register = count_and_say(register)

    return register


assert nth_count_and_say(1) == "1"
assert nth_count_and_say(4) == "1211"
