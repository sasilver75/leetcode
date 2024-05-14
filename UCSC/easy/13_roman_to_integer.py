"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

NOTES:
- s.length <= 15
- s contains only IVXLCDM
- It's GUARANTEED that s is a valid roman numeral in the range [1, 3999]
"""

def roman_to_integer(roman: str) -> int:
    """
    The tricky bit about this is realizing that while normally roman numerals only go from
    "largest" to "smallest," sometimes a smaller comes before a larger, when we want to
    have something like "40".

    This can trip you up, but it's important to realize that there are actually only a few
    cases in which this can happen.

    If we ignored the special cases of (eg) IV, IX, XL, XC, CD, CM ("reverse bites")
    Then we could just greedily accumulate a sum of the integer values
    eg
    XVII
    Can just be seen at 10+5+1+1

    And it's a nice benefit that each of these special cases are just 2 long!

    So at every step, there are only two things that we have to consider:
    Given our sum and our current position in the sequence: Can we take one of these "reverse bites"?
    If so, we should do it and accumulate it/move our index appropriately! Otherwise just
    do a normal accumulation.

    So a weird case like XLIII (43) can just be done as 40 + 1 + 1 + 1
    """
    cases = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    special_cases = {
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900
    }
    idx = 0
    acc = 0

    # Can we take an appropriate 2-bite chomp?
    while idx < len(roman):
        chomp = roman[idx: idx+2]
        if chomp in special_cases:
            acc += special_cases[chomp]
            idx += 2
            continue
        # Otherwise, just take a length-1 bite
        bite = roman[idx]
        acc += cases[bite]
        idx += 1
    return acc






# -----

cases = (
    ("III", 3),
    ("LVIII", 58),
    ("MCMXCIV", 1994)
)


for idx, (i,o) in enumerate(cases):
    try:
        assert roman_to_integer(i) == o
        print(f"Passed {idx}")
    except Exception as e:
        print(e)
