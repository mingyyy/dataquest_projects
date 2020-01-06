""" 
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
import time
import sys


class recursionlimit:
    def __init__(self, limit):
        self.limit = limit
        self.old_limit = sys.getrecursionlimit()

    def __enter__(self):
        sys.setrecursionlimit(self.limit)

    def __exit__(self, type, value, tb):
        sys.setrecursionlimit(self.old_limit)


def isprime(x):
    '''Returns True if n is prime. O(N)'''
    result = True
    for i in range(2, x):
        if x % i == 0:
            result = False
            return result
    return result


# good resources for prime number quick search
# https://stackoverflow.com/questions/1801391/how-to-create-the-most-compact-mapping-n-→-isprimen-up-to-a-limit-n#1801446
def isprime2(n):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w

    return True


def isprime3(n):
    """
    Returns True if n is prime. Assumes that n is a positive natural number. O(sqrt(N))
    """
    # We know 1 is not a prime number
    if n == 1:
        return False

    i = 2
    # This will loop from 2 to int(sqrt(x))
    while i*i <= n:
        # Check if i divides x without leaving a remainder
        if n % i == 0:
            # This means that n has a factor in between 2 and sqrt(n)
            # So it is not a prime number
            return False
        i += 1
    # If we did not find any factor in the above loop,
    # then n is a prime number
    return True


# method 1
def max_prime_factor(n):
    if isprime3(n) is True:
        return n
    factor = 0

    if n % 2 == 0:
        m = n/2
    else:
        m = (n+1)/2

    for i in range(2, int(m)):
        if n % i == 0 and isprime3(i) is True:
            factor = i
    return factor


# method 2 (slower than 1)
def max_prime_factor_2(n):
    if isprime(n) is True:
        return n
    for i in range(2, int(n)):
        if n % i == 0 and isprime(i) is True:
            n = n / i
            res = i
    return res


# method 3 (faster with recursion limitation)
def primeFact(i, f):
    if i < f:
        return []
    if i % f == 0:
        return [f] + primeFact(i / f, 2)
    return primeFact(i, f + 1)


start_time = time.time()
print(max_prime_factor(6008514751))
print(f'--{time.time() - start_time} seconds--')


# start_time = time.time()
# with recursionlimit(200000):
#     print(primeFact(600851, 2))
# print(f'--{time.time() - start_time} seconds--')


# forward 6008514751
# 3439333
# --1120.0235137939453 seconds--

# backward 6008514751
# 3439333
# --1107.7401769161224 seconds--

# half 6008514751
# 3439333
# --541.6724359989166 seconds--


# sqrt isprime 6008514751
# 3439333
# --526.5467047691345 seconds--

# with isprime2 method 6008514751
# 3439333
# --555.4595489501953 seconds--

# with isprime3 method 6008514751
# 3439333
# --540.4685451984406 seconds--