"""
Roman to Integer
"""


"""
Insight: It's listed that there are SIX instances where subtraction is used:
- I can be placed before V and X to make 4 and 9
- X can be placed before L and C to make 40 and 90
- C can be placed before D and M to make 400 and 900

We just ADD these combined characters (X, IX, C) together
So we check if we can take a two bite, else we take a one bite, and move the index appropriately.
"""
def roman_to_integer(s: str) -> int:
    LOOKUP = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900
    }
    sum = 0
    i = 0
    while i < len(s):
        # Can we take a multi-bite? Or just a single bite?
        two_bite = s[i:i+2]
        one_bite = s[i: i+1]

        if two_bite in LOOKUP:
            sum += LOOKUP[two_bite]
            i += 2
        elif one_bite in LOOKUP:
            sum += LOOKUP[one_bite]
            i += 1

    return sum


assert roman_to_integer("III") == 3
assert roman_to_integer("LVIII") == 58
assert roman_to_integer("MCMXCIV") == 1994
