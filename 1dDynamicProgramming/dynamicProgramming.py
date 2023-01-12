"""
Dynamic Programming
Vid: https://www.youtube.com/watch?v=mBNrRy2_hVs&list=WL&index=6
Sheet: https://docs.google.com/spreadsheets/d/1pEzcVLdj7T4fv5mrNhsOvffBnsUH07GZk7c2jD-adE0/edit#gid=0

Dynamic Programming is pretty much a combination of recursion and memoization

---------------------------------------------------------

1. Fibonacci Numbers
(Climbing Stairs, House Robber, Fibonacci Number, Maximum Alternating...)

F(0) = 0
F(1) = 1
F(N) = F(N-1) + F(N-2)
...
F(2) = F(1) + F(0) = 0 + 1 = 1
F(3) = 1 + 1 = 2
F(4) = 2 + 1 = 3
F(5) = 3 + 2

Why is DP a good fit for Fibonacci? Let's say that we wanted to compute the F(6)
We could naively consider this to be a decision tree-like problelm:

            f(6)
           /       \
        f(5)       f(4)
        /\          /  \
    f(4)  f(3)    f(3)  f(2)

But wait, there's a lot of repeated work being done there, isn't there!
We're calculating things like f(4) multiple times!
We should be able to cache that value!

If we want to compute f(6), we should just compute f(5), which wants to
compute f(4), f(3), f(2), ... f(0)
So we've computed all of f(6...0).

[F(6), F(5), F(4), F(3), F(2), F(1), F(0)]

Instead of starting at F(6), we can instead start at the bottom - F(0).
This is the "BOTTOM UP" dynamic programming approach -- but we should mention
that fibonacci numbers is a ONE-DIMENSIONAL dynamic programming problem.

There are many problems that fall into this one-dimensional DP pattern.
One of those is Climbing Stairs, which is pretty much exactly this Fib problem.

Note that we don't even have to have all of the F(n) numbers in memory -- at
any one time, we only need to store the LAST TWO numbers. Cool!

---------------------------------------------------------
2. The O/1 Knapsack Problem
(Partition Equal Subset Sum, Target Sum)

The 0/1 Knapsack problem... The 0/1 comes from us being given some quantity of things
available to us, like Coins of different value, and we want to use these coins to sum
to some sort of particular target -- we might ask the minimum number of coins to hit the target,
or maybe even simpler "is it possible to hit this target using these coins." The 0/1 comes
from the fact that we can use each of the (e.g.) coins either 0 or 1 times. We have
a fixed quantity of the coins.

Dynamic programming is all about subproblems. If our target is 5, we can use each
of these coins once... And we can use one fo three coins.

Traget =5, Coins=[1,2,3]

                        5, [1,2,3]
                1/       2|       3\
            4, [2,3]    3, [1,3]   2, [1,2]
            /\              /\          /\
            ...             ...          ...

This is a little more complicated than our "one dimensional" DP that we saw
in fibonacci -- because we're keeping track of two "dimensions" here -- both
the size of the Target and the remaining Coins.

You could visualize this as so:

        Target  5   4   3   2   1   0
Coins
1               _   _   _   _   _   T
2               _   _   _   _   _   T
3               _   _   _   _   _   T

(Personally I think I would use the list of [1,2,3], [1,2], [1,3], [2,3], [1], [2], [3], etc I think

---------------------------------------------------------
3. Unbounded Knapsack
(Coin Change, Coin Change II, Minimum Cost for Tickets)

What does unbounded refer to? Imagine in the previous coin example, we could use
each coin an infinite number of times instead of just 0/1 times. The goal is still the
same -- to sum up to some target value.
We can actually reuse the exact same grid for the above problem.

        Target  5   4   3   2   1   0
Coins
1               _   _   _   _   _   T
2               _   _   _   _   _   T
3               _   _   _   _   _   T

See the video for his intuition on the state transition possibilities

---------------------------------------------------------
4. Longest Common Subsequence
(Longest Common Subsequence, Longest Increasing Subsequence, Edit Distance, Distinct Subsequences)

There any many dynamic programming problems related to subsequences.
Basically the trick to this is how subsequences work.
If we have a string like "abc", a subsequence of the string is a non-(necessarily)-contiguous element
of the possible orderings. The order of the original string does matter -- you can do "ac", but not "ca", for
instance.

---------------------------------------------------------

5. Palindromes
(Longest Palindromic Substring, Palindromic Substrings, Longest Palindromic Subsequence)

What we're going to mainly focus on is how Palindromes relate to dyamic programming, and get a little trick that's required to solve many
problems efficiently.

Assume we get "racecar" and we're asked to count all the palendromes in the entire string.

A naive way:
We get to "raceca" and we want to know whether something is a palindrome or not.
We do a two-pointer check from the outsdie and do an O(N) traversal of the substring. That's not great!

Let's say we were looking at the entire string: "racecar" -- Is this entire string a palindrome?
We would again naively start with two pointers at each side and walk them inwards, comparing. In worst case, O(N)!

How do we cut down on repeated work?
We can change the way that e build upon our strings. We start at any given string of size 1, then expand outwards!

So start looking at "e"
We know that's a palindrome
Let's say we want to expand to "cec". Do we need to check the entire "cec"? No! Because we already know
that we checked e, so we really have "c{knownPalindrome}c" -- we only need to check that c == c, which is an O(1) operation.

If we knew that "aceca" were a palindrome,
when we expand to "racecar", we only need to check that r == r in constant time. Great.

So instead of generating all substrings (O(N^2)) and then checking whether each are palindromes (additional O(N) for each = O(N^3) ...
We can just expand a window outwards from every character, in O(N) time (meaning O(N^2) operations), doing a constant time check (for a total of O(N^2))!

As we're expanding the window, if we get a r == c or something, we can stop the expansion. If we hit an edge (outside the edge), we can stop our expansion.

---------------------------------------------------------

As you might know...there are also problems that don't fall into any of these 5 categories. There are many types of dynamic programing problems
out there.
"""