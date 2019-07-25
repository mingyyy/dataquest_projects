""" 
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
import time
from math import ceil


def isprime(x):
    result = True
    for i in range(2, x):
        if x % i == 0:
            result = False
            return result
    return result


def max_prime_factor(n):
    if isprime(n) is True:
        return n
    factor = 0

    if n % 2 == 0:
        m = n/2
    else:
        m = (n+1)/2

    for i in range(2, int(m)):
        if n % i == 0 and isprime(i) is True:
            factor = i
    return factor

    # backward loop
    # for i in range(n-1, 1, -1):
    #     if n % i == 0 and isprime(i) is True:
    #         factor = i
    #         return factor
    # return factor


start_time = time.time()
print(max_prime_factor(6008514751))
print(f'--{time.time() - start_time} seconds--')

# forward 6008514751
# 3439333
# --1120.0235137939453 seconds--

# backward
# 3439333
# --1107.7401769161224 seconds--

# half
# 3439333
# --541.6724359989166 seconds--

# sqrt isprime
# 3439333
# --526.5467047691345 seconds--
