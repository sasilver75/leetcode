"""
Pow

Implement pow(x,n) which calculates x raised ot the power n (i.e. x ** n)
"""

"""
Dumb idea: We just start with an acc of 1 and multiple acc*x n times?
This would probably work, except we also need to be able to do things
like

2 ** -2
2^(-2) is actually the same as 1/2**2, for what it's worth!
Note that this is also the same as (1/2)**2

It seems like there's some annyoing significant figure stuff going on.
I don't really care for this type of problem, frankly.
"""

def pow(x: int, n: int) -> int:
    acc = 1
    positive = n > 0
    sigfig = len(str(x).split(".")[-1])
    n = abs(n)
    while n > 0:
        acc *= (x if positive else 1/x)
        n -= 1
    print(acc)

    return acc

"""
Here's now some annoying solution that we can find in the leetcode solutions.

"The main idea of the solution is to use as much multiplications as possible...
How can we evaluate x^20? We just multiply x in a loop 20 times, right?

But x^20 = x^10*x^10 too!
So we could multiple x^10 by itself as well.
Similarly x^5 * x^5 = x^10
                                20
                    10      *           10
                5   *  5
                
But now we have an odd number how do we evaluate?
No problem -- just split this into 3 * 2

There are soem other border cases.

1) If we have n = 0, return 1
2) If we have a negative power, return the positive power of 1/x
3) Two cases: For Even N and for Odd N
"""

def recursiveMyPow(x, n):
    if n == 0:
        return 1

    if n < 0:
        return recursiveMyPow(1/x, -n)

    lower = recursiveMyPow(x, n//2)
    if n % 2 == 0:
        return lower * lower
    else:
        return lower * lower * x   # Basically x**5 = x**2 * (x**2 * x**1)



# -- Test Zone --
def test(fn):
    assert fn(2, 10) == 1024.0000
    assert fn(2.10000, 3) == 9.26100
    assert fn(2.0000, -2) == .25000 # This is where we can't just multiply x*x n times

test(recursiveMyPow)