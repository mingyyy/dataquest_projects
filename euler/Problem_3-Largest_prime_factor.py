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

# slower than 1
def max_prime_factor_2(n):
    if isprime(n) is True:
        return n
    for i in range(2, int(n)):
        if n % i == 0 and isprime(i) is True:
            n = n / i
            res = i
    return res


start_time = time.time()
print(max_prime_factor_2(60085147))
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

# method 2  6008514
# 58907
# --0.7148058414459229 seconds--

# method 1 6008514
# 58907
# --0.32723093032836914 seconds--