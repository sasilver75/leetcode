"""
13: Roman to Integer

Roman numerals are represented by seven different symbols:
I, V, X, L, C, D, M
with corresponding values
1,5,10,50,100,500,1000

For example:
2 is written as II in RomanNumeral
12 is written as XII
27 is written as XVII

Roman numerals are USUALLY written largest to smallest from left to right
However the number for 4 is not IIII -- instead, it's IV!
Because the one is before it five, we subtract it, making four.

The same principle applies ot the number 9 (IX)

There are 6 instances where subtraction is used:
I can be placed before V (5) and X (10) to make IV (4) and IX (9)
X can be placed before L (50) and C (100) to make XL (40) and XC (90)
C can be placed before D (500) and M (1000) to make CD (400) and CM (900)

Given a roman numeral, convert it to an integer!
"""

"""
So in the easy case (LXI), we could just iterate
through the letters L, X, and I, and sum their values.
Same for numbers like XII and XVII.
There's no 'interaction' between those values. That's the very easy case!

The tricky part seems to be understanding how to handle those multiple-character
interactions.

I think the key to understanding those interactions is to understand that 
there's actually only a small number of such interactions, and we can 
enumerate them!
IV, IX, XL, XC, CD, CM
These function pretty much like their own unique character set!
On top of the usual character sets of I, V, X, L, C, D, M  (1,5,10,50,100,500,1000)

So can our processing pretty much be the element-wise lookup + sum that we described
earlier, just the lookup involves FIRST looking to see if we have a compound character,
and then if we don't, checking if we have a simple character?

Let's try it out
"""

def roman_to_numeral(roman: str) -> int:
    # Assuming that it's a valid roman string
    simple_lookup = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    composite_lookup = {
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900
    }
    roman = [char for char in roman.upper()]
    sum = 0
    i = 0
    while i < len(roman):
        composite_char_candidate = "".join(roman[i:i+2]) # II, IX, XC, XV, ... May or may not be composite
        if composite_char_candidate in composite_lookup:
            sum += composite_lookup[composite_char_candidate]
            i += 2
        else:
            sum += simple_lookup[roman[i]]
            i += 1
    return sum


fns = [roman_to_numeral]

for fn in fns:
    assert fn("III") == 3
    assert fn("LVIII") == 58
    assert fn("MCMXCIV") == 1994