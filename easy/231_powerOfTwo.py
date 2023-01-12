"""
Given an integer n, retrun true if it is a power of two.
Otherwise, return false.

An integer n is a power of two; if there exists an integer X such that
n == 2^x.
"""

def is_power_of_two(n: int) -> bool:
    """O(logN)"""
    if n < 0:
        return False

    exp = 0
    ans = 0
    while ans < n:
        ans = 2 ** exp
        if ans == n:
            return True
        exp += 1

    return False


"""
Challenge: Can you do this without loops or recursion?

When someone asks you this, you're probably like... fuck.
Either there's some special property of powers of 2 that 
you need to know about to be able to solve it...

...or... is it something about bit manipulation?

Let's look at some powers of two and see what
might be in common between power of two:

0  -> ...0
2  -> ...10
4  -> ...100
8  -> ...1000
16 -> ...10000
32 -> ...100000
64 -> ...1000000
128-> ...10000000

Ah. That makes it... a little more straightforward, huh?
So you just convert the number into binary, and then make sure 
that there's just zeroes past the only one.

So we know that n will only have one bit set if it's a power of 2.
If you ave a number like      8 :  1000
And you subtract one from it  7 :  0111
See that all of the bits are 1s, other than the 0 that used to be a 1?
It's like a mirror! And if we do 0b1000 & 0b0111 in Python, 
the bitwise "and", we get 0!
So any number n whose bitwise AND (&) with n-1 is 0... is a power of two! 
"""

assert is_power_of_two(1) == True
assert is_power_of_two(16) == True
assert is_power_of_two(3) == False