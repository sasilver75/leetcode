"""
Maximum Product Subarray

Given an integer array `nums`, find a SUBARRAY that has the
largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit
integer.
"""
from functools import reduce


def max_product_brute(nums: list[int]) -> int:
    # Generate all subarrays
    subarrays = []
    for start in range(0, len(nums)):
        for end in range(start, len(nums)):
            subarrays.append(nums[start:end+1])

    print(subarrays)

    # Determine maximum product of all subarrays
    max_product = float('-inf')
    for subarray in subarrays:
        product = reduce(lambda a, b: a * b, subarray)
        max_product = max(max_product, product)


    ## Note that the generation of the subarrays and the determination
    # of the subarray product could be concurrent, use less memory, getting
    # us into O(1) memory and O(N^2) time

    return max_product


"""
How can we do better?
What's the "insight" to this question?

So we're multiplying numbers together
-> If all nubmers were positive, it would just be the whole subarray
    -> There is no reason to NOT include a positive number in the subarray
-> If there were negative numbers, things get harder -- because two negatives multiply to a positive
-> We know that the max_product subarray cannot include any 0s, since those irrevocably set us to zero.

[1,2,4,0,-3,2,-4]           Ans: 24 from [-3,2,-4]

Theory: What if we did it a little "greedy" (?) where we started with a product of 
1, and multiplied it by the current element, for each element in the list? But whenever
we hit a 0, we reset our product to 1. We also kept track of a max product on the side,
which maybe is initialized to -inf, or something.

1
2
4
1
-3
-6
24
Final answer: 24

Okay, that worked... What about for something like below, though, where 
we actually have to "CHOOSE" to not include a negative number in the subarray?

[1,2,-4,12,3,0,-3,2,-4]     Ans: 26 from [12,3]

1
2
-8
-96
-288
1
-3
-6
24
Final Answer: 24
Well that isn't correct.

Is there a way that we can avoid "splitting" our logic when we run into a 
negative number?
What if we were keeping track of TWO numbers as we iterated across? Where
at evey number we reset ONE of them to 1, as if we didn't take it?

1,1
2,2
-8,1
-96,12
-288, 36
1,1
-3,1
-6,2
-24,-8
Final Answer: 36
Okay, that worked for this example... But is that expressing all possible 
options, where we have one side that ALWAYS multiplies by a negative number, and the 
other than NEVER does? What if, in the optimal solution, there were three negative
numbers, but the last two of them were the ones that needed to be included in our
max product subarray?

[2,-5,10,-6,3,-2,30]
Where the maximum product is going to be the [10,-6,3,-2,30] subarray (10,800)
I don't think our answer would work for that, right?
2,2
-10,1
-100, 10
600, 1
1800, 3,
-3600, 1,
-108000, 30
Answer: 1800 --> Wrong! 

Hmmm...

Is there some sort of dynamic programming solution that we could do?
What about a bottom-up solution?

For the example
[2,3,-2,4]   --> Ans: [2,3] -> 6

The easy solution is to generate all subarrays and test for the max product
in O(N^2) time

Can we do better? Are there any patterns to this problem that we can use
to our advantage to get a better solution than N^2?

Let's look at an example:

[1,2,3]

All elements are positive. What does that mean for us?
It means that we want to take the whole subaray!
If we get positive numbers, the subarray product is always going to be increasing

What about with all negative elements?

Elements: [-1, -2, -3]
Running Product:  [-1, 2, -6] 
Max Product: 6 from [-2,-3]

We see that the product vascillates between positive and negative numbers.
And that the maximum subarray here isn't the whole array as a subarray.
***TIP: Though we're looking for the max product subarray, we'll also need to
keep track of the minimum as well!***

(and side note)
And if there were a zero?
Elements: [2,3,0,-2,6,24,-2]
Product:  [2,6,0,0,0,0,0,0]
Including a zero torpedoes any subarray products that run through them!

Let's give this a shot (still the idea of keeping track of two numbers, but 
it's keeping track of the min and the max!).

Test:
[1,2,4,0,-3,2,-4]
[1,1]
[2,2]

"""

# fn([7, 0, -2, -4])
def max_product(nums: list[int]) -> int:
    max_product = -float('inf')
    min_p, max_p = 1, 1
    for num in nums:
        if num == 0:
            min_p, max_p = 0, 0
            continue

        a = num * min_p
        b = num * max_p

        # Either start a new subarray at the current num, or extend a previous subarray
        min_p = min(a,b, num)
        max_p = max(a,b, num)

        max_product = max(max_product, max_p)

    print(max_product)
    return max_product


def neetcode_solution(nums: list[int]) -> int:
    res = max(nums)
    curMin, curMax = 1,1

    for n in nums:
        if n == 0:
            curMin, curMax = 1, 1
            continue


        # Possible Bug Opportunity Here! :O Using a tmp variable to "freeze" curMax*n before changing curMax for use in curMin calculation
        tmp = curMax * n
        curMax = max(n * curMax, n * curMin, n)
        curMin = min(tmp, n * curMin, n)

        res = max(res, curMax)

    return res


# -- Test Zone --
def test(fn):
    # assert fn([2, 3, -2, 4]) == 6 # Testing for mix pos/negs
    assert fn([7, 0, -2, -4]) == 8 # Testing for mix pos/negs/zeroes
    # assert fn([-2, 0, -1]) == 0 # Testing for negatives and zeroes
    # assert fn([-2, 12, 0]) == 12 # Testing for single-number

test(max_product_brute)
test(max_product)
test(neetcode_solution)