"""
Count and Say

The COUNT AND SAY sequence is a sequence of digit strings defined by
the recursive formula:

CountAndSay(1) = "1"
CountAndSay(n) is the way you would "say" the digit string from countAndSay(n-1),
which is then converted into a different digit string.

To determine how you would "say" a digit string, split it into the minimal number
of substrings such that each substring contains exactly ONE unique digit.

Then, for each substring, say the number of digits, then say the digit.
Finally, concetenate every said digit.

Ex:

"3322251" -> "two 3s, three 2's, one 5, and one 1
          -> 2 3 + 3 2 + 1 5 + 1 1
          -> "23321511"

"""

def count_and_say_naive(n: int) -> str:
    cas = {1: "1"}

    for current_term in range(2, n+1):
        previous_term_string = cas[current_term - 1]

        term_string = ""
        char_count = 0
        for idx, char in enumerate(previous_term_string):
            previous_char = previous_term_string[max(idx-1, 0)]

            if char == previous_char:
                char_count += 1
            else:
                # Append the previous {char_count}{previous_char} into built + reset count (then inc it)
                term_string += (str(char_count)+previous_char)
                char_count = 1

        # Dump any remaining char/counts we might have
        term_string += str(char_count)
        term_string += previous_term_string[-1] # "previous_char" would not be accurate here

        cas[current_term] = term_string

    return cas[n]

"""
# Now note that we don't actually have to build up the whole table -- we
only have to keep track of the last countAndSay term.
"""

def count_and_say(n: int) -> str:
    previous_term_string = "1"


    """
    Previous Term String: 21
    
    idx: 0
    char: "2"
    charcount: 1
    prev_char: 2
    term_string:   
    """

    for term in range(2, n+1):
        char_count = 0
        term_string = ""

        for idx, char in enumerate(previous_term_string):
            previous_char = previous_term_string[max(idx-1, 0)]
            if char == previous_char:
                char_count += 1
            else:
                # Dump
                term_string += str(char_count)
                term_string += previous_char
                # Reset
                char_count = 1

        # Might still be charcount left
        term_string += str(char_count)
        term_string += previous_term_string[-1]

        previous_term_string = term_string



    return previous_term_string






# -- Test --

def test(fn):
    assert fn(1) == "1"
    assert fn(4) == "1211"

test(count_and_say_naive)
test(count_and_say)

# Explanation:
# countAndSay(1) = "1"
# countAndSay(2) = say "1" = one 1 = "11"
# countAndSay(3) = say "11" = two 1's = "21"
# countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"