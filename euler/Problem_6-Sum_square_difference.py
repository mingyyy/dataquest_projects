""" 
The sum of the squares of the first ten natural numbers is,
The square of the sum of the first ten natural numbers is,
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def sum_sqrt(n, p):
    s = 0
    for i in range(1, n+1):
        s += i**p
    return s


def sqrt_sum(n, p):
    s = 0
    for i in range(1, n+1):
        s += i
    return s**p

if __name__ == "__main__":
    print(sqrt_sum(10, 2)-sum_sqrt(10, 2))
    print(sqrt_sum(100, 2)-sum_sqrt(100, 2))

# 25164150