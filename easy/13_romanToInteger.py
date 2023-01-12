def roman_to_integer(roman: str) -> int:
    lookup = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    sum = 0
    idx = 0
    while idx < len(roman):
        current_char = roman[idx]
        current_char_value = lookup[current_char]
        # Is it possible that there's a character to the right?
        is_right_char = idx + 1 < len(roman)
        # If there is, and that character is larger than our current one:
        if is_right_char:
            next_char = roman[idx+1]
            next_char_value = lookup[next_char]
            if next_char_value > current_char_value:
                sum += next_char_value - current_char_value
                idx += 2
                continue
        sum += current_char_value
        idx += 1
    return sum


def test(fn):
    cases = [
        ("III", 3),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
    ]

    for input, soln in cases:
        ans = fn(input)
        print(f"""
Input: {input}
Ans: {ans}
Correct: {ans == soln}
""")

test(roman_to_integer)
