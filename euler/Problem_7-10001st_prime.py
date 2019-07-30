""" 
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10001st prime number?
"""

def isprime(x):
    result = True
    for i in range(2, x):
        if x % i == 0:
            result = False
            return result
    return result

def prime_nth(n):
    counter, total = 1, 1
    while counter <= n:
        total += 1
        if isprime(total):
            counter += 1
        # print(counter, total)
    return total


if __name__ == "__main__":
    print(prime_nth(10001))

# 104743