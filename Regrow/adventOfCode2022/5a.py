"""
The supplies need to be unloaded from the ship!

Supplies are stored in stacks of marked `crates`, but because the needed
supplies are buried under many other crate,s the crates need to
be rearranged!

The ship has a giant cargo crane capable of moving crates between stacks.

Given a direction page like this:

    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2

In each step of the procedure, a quantity of crates is moved from one
 stack to a different stack.
 In the first step of the above rearrangement procedure,
 one crate is moved from stack 2 to stack 1, resulting in this configuration:

[D]
[N] [C]
[Z] [M] [P]
 1   2   3


Crates are moved one at a time, so the first crate to be moved (D) ends up below the second and third crates:

        [Z]
        [N]
    [C] [D]
    [M] [P]
 1   2   3


Then, both crates are moved from stack 2 to stack 1.
Again, because crates are moved one at a time, crate C ends up below crate M:



        [Z]
        [N]
[M]     [D]
[C]     [P]
 1   2   3


Finally, one crate is moved from stack 1 to stack 2:

        [Z]
        [N]
        [D]
[C] [M] [P]
 1   2   3


The Elves just need to know which crate will end up on top of each stack;
 in this example, the top crates are C in stack 1, M in stack 2, and Z in stack 3,
 so you should combine these together and give the Elves the message CMZ.


After the rearrangement procedure completes,
 what crate ends up on top of each stack?



"""
import string

with open("inputs/5a.txt", "r") as f:
    lines = f.read().splitlines()

    # Break into Header section and Instruction section
    header_lines = lines[:9] # Line 9 is just whitespace seperator
    instruction_lines = lines[10:]

    length = int([char for char in header_lines[-1] if char in string.digits][-1])
    stacks = [[] for _ in range(length)]

    # Populate the Stack
    char_indexes = range(2, 2+(4*(length-1))+1, 4)  # [1, 5, 9, 13, 17, 21, 25, 29, 33]
    for line_number in range(len(header_lines)-2, -1, -1):
        raw_line = header_lines[line_number]
        # Parse line into ['J', 'V', 'W', 'M', 'F', ' ', 'J', ' ', 'J']
        parsed_line = [char for idx, char in enumerate(raw_line) if idx in range(1, 1+(4*(length-1))+1, 4)]
        for idx, char in enumerate(parsed_line):
            if char != ' ':
                stacks[idx].append(char)

    print(stacks)
    # Process the Instructions into [n, source, target]

    # Evaluate the Instructions

    pass