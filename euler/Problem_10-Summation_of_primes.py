""" 
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""
import time


def isprime(x):
    result = True
    for i in range(2, x):
        if x % i == 0:
            result = False
            return result
    return result


def prime_sum(m, n):
    s = 0
    for i in range(m, n):
        if isprime(i):
            s += i
    return s


if __name__ == "__main__":
    start_time = time.time()
    print(prime_sum(1800001, 2000000))
    print(f'--{time.time() - start_time} seconds--')

# from 2 a 50,000
# 121013308
# --11.624578714370728 seconds--

# from 50,001 a 100,000
# 333383229
# --31.92916774749756 seconds--

# from 100,001 a 200,000
# 1255204276
# --119.49474620819092 seconds--

# from 200,001 a 500,000
# 8204635382
# --773.7777619361877 seconds--

# from 500,001 a 1,000,000
# 27636165828
# --12838.361411094666 seconds--

# from 1,000,001 a 1,100,000
# 7575351672
# --2791.387584924698 seconds--

# from 1,100,001 a 1,200,000
# 8307652436
# --782.2548451423645 seconds--

# from 1,200,001 a 1,500,000
# 28641037125
# --3168.2791271209717 seconds--


# from 1,500,001 a 1,700,000
# 22376515448
# --7964.4253051280975 seconds--

# from 1,700,001 a 1,800,000
# 12130179143
# --1193.2335731983185 seconds--

# from 1,800,001 a 2,000,000
# 26332691075
# --25933.93080186844 seconds--