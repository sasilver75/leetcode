"""
An ugly number is a positive integer whose prime factors
are limited to 2, 3, and 5.

Given an integer N, return TRUE if N is an UGLY NUMBER.
"""

"""
Thinking:
How can we prove that a number is only divisible by prime numbers
in the set [2, 3, 5] (or no prime factors)?

We could...
check every prime number between 1 ... N? and see if it evenly divides num?
But how do we know if a number is prime?
I know the answer is to use the "sieve of eratosthenes," whch can be used
for finding all prime numbesr up to a given limit.

Sieve of Eratostehenes:
* Iteratively mark as composite the multiples of each prime, starting 
with the first prime number 2.
"""

def is_ugly(num: int) -> bool:
    primes = set(get_primes(num))

    # For each prime
    for prime in primes:
        # If it equally divides num and it isn't in [2,3,5] or num itself...
        if (num % prime == 0) and prime not in [2,3,5, num]:
            # Ugly!
            return False

    return True


def get_primes(limit: int) -> list[int]:
    """
    SIEVE OF ERATOSTEHENES
    The Sieve of Eratostehenes is a method for finding all primes
    up to (and possibly including) a given natural number num

    Insight:
    * A prime number is a number divisble by only ONE and ITSELF

    so...
    * Generate a list of "True" (Prime... for now) indices from [0, N]
    * Walk from [0, N], skipipng a number if it's already been marked as
    "False" in the boolean list.
    * For each number we don't skip, mark all multiples of it as "False" (Composite)
    in the range from (num, N]
    * Return the indices of the remaining True elements in your boolean list

    But here's a speedup trick, if you want to. Since we're going to be taking multiples of numbers,
    and the first multiple of a number is N*2, then we don't need to check
    any numbers above N/2  (that is, check all numbers <= N/2).

    But really all those numbers above N/2 are going to be ~no-ops anyways, so I dont know
    if you're saving too much anyways.
    """
    primes = [True]*(limit+1)
    primes[0] = False
    primes[1] = False

    composites = set()
    primes = []

    for num in range(2, limit+1):
        if not num in composites:
            primes.append(num)
            for multiple in range(num, limit+1, num): # For counting up by num
                composites.add(multiple)

    return primes


def another_sieve_implementation(n: int):
    # You can use either a list of booleans, or a primeList+compositeSet
    prime_list = [True] * (n+1)
    prime_list[0] = False
    prime_list[1] = False

    for candidate in range(2, n+1):
        if prime_list[candidate] == True:
            """The squaring of each prime is an optimization that makes use of the fact that all smaller multiples of each new prime will have been eliminated in previous rounds. Only the prime numbers will be left as you count and eliminate non-primes using this process."""
            for multiple in range(candidate**2, n+1, candidate):
                prime_list[multiple] = False

    primes = [idx for idx,val in enumerate(prime_list) if val]
    return primes






get_primes(89)
another_sieve_implementation(89)

# Case 1
assert is_ugly(6) == True
assert is_ugly(1) == True
assert is_ugly(14) == False