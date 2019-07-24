""" 
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
import time


def isprime(x):
    result = True
    for i in range(2, x):
        if x % i == 0:
            result = False
            return result
    return result


def max_prime_factor(n):
    factor = 0
    for i in range(2, n):
        if n % i == 0 and isprime(i) is True:
            factor = i
    return factor
    # for i in range(n-1, 1, -1):
    #     if n % i == 0 and isprime(i) is True:
    #         factor = i
    #         return factor
    # return factor

start_time = time.time()
print(max_prime_factor(6008514751))
print(f'--{time.time() - start_time} seconds--')
