"""
Find the Duplicate Number

Given an array of integers `nums` containing n+1 integers
where each integer is in the range [1, n] inclusive...

There is only ONE repeated number in nums; return the repeated number!

** You must solve this problem WITHOUT modifying the array `nums` and uses ONLY
constant extra space.
"""

def find_duplicate_dumb(nums: list[int]):
    # O(N^2) duplicate finder with O(1) constant space
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return nums[i]

"""
We can't modify the array or use O(N) extra space, so a sorting then selecting
option isn't going to work for us.

I think there's some bitwise solution...
https://leetcode.com/discuss/general-discussion/1073221/All-about-Bitwise-Operations-Beginner-Intermediate

Bitwise Operations:

AND (&):
    X & Y  -> This keeps the bits set for both X and Y
    
    
OR (|):
    X | Y  -> This keeps the bits set in either X or in Y
    
    
NOT (~):
    ~ X -> This inverts all the bits present in the binary representation of X
    
    
XOR (^):
    X ^ Y  -> This checks if a position has a bit set in either one of X or Y. 
            If so, then the result also has a set bit there, eg:
            X = 1011010
            Y = 0101010
            -----------
          X^Y = 1110000

    Some properties of XOR:
        * Commutativity: x ^ y == y ^ x
        * Associativity: (x ^ y) ^ z == x ^ (y ^ z)
    
    
Right and Left Shift (>> / <<):
    Left ship multiplies a number by 2, whereas right shift divides it by 2 (with possible flooring)
    These are called left/right shift operations because of how they shift the numbers when represented in binary format.
    
    19: 10011
    19>>2: 100  (lost 11 off the end)
    This divides 19 by 4
    

Applications and Common Problems:

1) Bit Masking
    * For problems (like generating subsets) where you have to iterate over all 2^k possibilities, we can
    take advantage of the fact that when we write binary numbers from 0...2^k-1, these numbers will have all combinations
    of 1s and 0s that can be present in an array of size k. So we can iterate through ALL the numbesr starting from
    0...2^k-1 and check their binary representations. For each number, if the ith bit
    contains a 1, we can add the element present at that location to our current vector (and if
    it's a 0, we ignore it).
    
2) XOR Swap Algorithm
    * What's the minimum number of vairalbes to swap two numbers? We can do it without
    a "temp" swap variable in languages that aren't as nice as Python!
    a, b --> integers to be swapped
    a = a ^ b # Now a contains a ^ b
    b = a ^ b # Now b contains a
    a = a ^ b # Now a contains b
    
3) Finding Parity of a Number
    * Parity of a number based on the number of 1s present in the binary equivalent
    of that number. When the count of 1's present is odd, it returns an "odd parity".
    When the # of 1s is even, it returns an "even parity". 
    Rather than casting to binary and iterating over bits to count, we can use an annoying bitwise solution
    using XOR and Right-Shifts to get the answer.
    
4) XOR Queries
    Since a^a == 0, we can solve problems like xor-queries-of-a-subarray in O(N) time
    using prefix XOR arrays.
"""

def find_duplicate(nums: list[int]):
    pass

def test(fn):
    assert fn([1,3,4,2,2]) == 2
    assert fn([3,1,3,4,2]) == 3

test(find_duplicate_dumb)
test(find_duplicate)